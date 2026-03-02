/* call python function from javascript */

function callPython(function_name, ...params) {
    const __callPython = document.getElementById('call_python');
    __callPython.setAttribute('data-value',
        JSON.stringify([function_name, ...params]));
    __callPython.click();
}
