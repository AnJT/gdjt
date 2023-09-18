const CryptoJS = require("crypto-js");

const KEY = "xiaofaai@act_id!"
const IV = "tongjixf@act_id!"

function encrypt (t) {
    if (!t) return !1;
    try {
        var e = JSON.stringify(t);
        e = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(e)).toString();
        var i = CryptoJS.enc.Utf8.parse(KEY), a = CryptoJS.enc.Utf8.parse(IV),
            s = CryptoJS.AES.encrypt(e, i, {
                iv: a,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.ZeroPadding
            }).toString();
        return CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(s)).toString()
    } catch (n) {
        console.error(n)
    }
}