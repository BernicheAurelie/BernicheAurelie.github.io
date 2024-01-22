const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

const lang = document.documentElement.getAttribute('lang') || 'en';
function Init() {
  new google.translate.TranslateElement({ pageLanguage: `${lang}` });
}

const usrlang = navigator.language.substring(0, 2) || navigator.userLanguage.substring(0, 2);
if (usrlang !== `${lang}`) {
  document.cookie = `googtrans=/${lang}/${usrlang}; Expires=Session; SameSite=None; Secure`;
  const google = document.createElement('script');
  google.type = 'text/javascript';
  google.src = 'https://translate.google.com/translate_a/element.js?cb=Init';
  document.body.append(google);
  setTimeout(removePreloader, 1200);
} else removePreloader();

function removePreloader() {
  const preloader = document.querySelector('#preloader');
  if (preloader) preloader.remove();
}