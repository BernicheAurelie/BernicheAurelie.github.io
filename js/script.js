const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

// auto google translate
// const lang = document.documentElement.getAttribute('lang') || 'en';
// console.log("constante lang initial: ", lang);
// function Init() {
//     console.log("constante lang in init: ", lang);
//   new google.translate.TranslateElement({ pageLanguage: `${lang}` });
//   console.log("constante lang post translate: ", lang)
// }

// const usrlang = navigator.language.substring(0, 2) || navigator.userLanguage.substring(0, 2);
// if (usrlang !== `${lang}`) {
//     console.log("constante usrlang/lang: ", usrlang, " / ", lang);
//     console.log("document.cookie initial: ", document.cookie)
//   document.cookie = `googtrans=/${lang}/${usrlang}; Expires=Session; SameSite=None; Secure`;
//   console.log("document.cookie googtrans: ", document.cookie)
//   const google = document.createElement('script');
//   console.log("const google: ", google)
//   google.type = 'text/javascript';
//   google.src = 'https://translate.google.com/translate_a/element.js?cb=Init';
//   document.body.append(google);
//   setTimeout(removePreloader, 1200);
// } else removePreloader();

// function removePreloader() {
//   const preloader = document.querySelector('#preloader');
//   if (preloader) preloader.remove();
// }