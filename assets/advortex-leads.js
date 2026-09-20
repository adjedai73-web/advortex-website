/*
 * advortex-leads.js
 * Saves website leads (contact form, quiz, calculator, booking) into Supabase
 * table public.website_leads. Fire-and-forget: it never blocks or breaks the
 * WhatsApp flow, even if Supabase is unreachable.
 *
 * Usage (any page, before opening WhatsApp):
 *   saveLead('contact_form', { name, business, phone, pack, message });
 *   saveLead('quiz',         { payload: { answers, result } });
 *   saveLead('calculator',   { payload: { inputs, monthlyLoss } });
 *   saveLead('booking',      { name, phone, payload: { date, time } });
 *
 * Add to each page:  <script src="/assets/advortex-leads.js" defer></script>
 */
(function () {
  'use strict';

  var SUPABASE_URL = 'https://nkbxqeptvpwwonyzsmyt.supabase.co';
  var SUPABASE_KEY = 'sb_publishable_4PX3aMd6XOORInHDIayjrQ_OxV9-gr5'; // public key, safe in the browser (RLS protects the data)
  var ENDPOINT = SUPABASE_URL + '/rest/v1/website_leads';

  var SOURCES = ['contact_form', 'quiz', 'calculator', 'booking', 'whatsapp_cta', 'other'];
  var TOP_LEVEL = ['name', 'business', 'phone', 'email', 'pack', 'message'];
  var LIMITS = { name: 200, business: 200, phone: 40, email: 200, pack: 100, message: 4000 };

  function detectLang() {
    var p = location.pathname;
    if (/-en(\.html)?$/.test(p)) return 'en';
    if (/-ar(\.html)?$/.test(p)) return 'ar';
    return 'fr';
  }

  function clean(value, max) {
    if (value === undefined || value === null) return null;
    var s = String(value).trim();
    if (!s) return null;
    return s.slice(0, max);
  }

  function saveLead(source, fields) {
    try {
      fields = fields || {};

      // Honeypot: add <input name="website" style="display:none" tabindex="-1" autocomplete="off"> to forms.
      if (fields.honeypot) return Promise.resolve(false);

      var qs = new URLSearchParams(location.search);
      var row = {
        source: SOURCES.indexOf(source) === -1 ? 'other' : source,
        lang: detectLang(),
        page_url: clean(location.href, 500),
        referrer: clean(document.referrer, 500),
        utm_source: clean(qs.get('utm_source'), 200),
        utm_medium: clean(qs.get('utm_medium'), 200),
        utm_campaign: clean(qs.get('utm_campaign'), 200),
        payload: fields.payload && typeof fields.payload === 'object' ? fields.payload : {}
      };

      TOP_LEVEL.forEach(function (k) {
        row[k] = clean(fields[k], LIMITS[k]);
      });

      return fetch(ENDPOINT, {
        method: 'POST',
        keepalive: true, // survives the redirect to WhatsApp
        headers: {
          'Content-Type': 'application/json',
          apikey: SUPABASE_KEY,
          Prefer: 'return=minimal'
        },
        body: JSON.stringify(row)
      })
        .then(function (res) {
          return res.ok;
        })
        .catch(function () {
          return false;
        });
    } catch (e) {
      return Promise.resolve(false);
    }
  }

  window.saveLead = saveLead;
})();
