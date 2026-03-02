/* show loading modal */
function showLoading() {
    const loading = document.getElementById('loading');
    addEventListener('py:ready', () => loading.close());
    loading.showModal();
}

/* call python function from javascript */
function callPython(function_name, ...params) {
    const __callPython = document.getElementById('call_python');
    __callPython.setAttribute('data-value',
        JSON.stringify([function_name, ...params]));
    __callPython.click();
}