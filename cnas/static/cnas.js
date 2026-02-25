

/* call python function from javascript */

function callPython(function_name, param1, param2, param3) {
    const __callPython = document.getElementById('call_python');
    __callPython.setAttribute('data-value',
    JSON.stringify([function_name, param1, param2, param3]));
    __callPython.click();
}

function py_generateUrl(allSites, masterPassword) {
    callPython("generateUrl", JSON.stringify(allSites), masterPassword);
}

function py_decryptUrlData(encryptedUrlData, masterPassword) {
    callPython("decryptUrlData", encryptedUrlData, masterPassword);
}