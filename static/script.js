document.getElementById('time').addEventListener('input', function (e) {
    const input = e.target;
    let value = input.value.replace(/\D/g, '');
    if (value.length > 2) {
        value = value.slice(0, 2) + ':' + value.slice(2, 4) + ':' + value.slice(4, 8);
    }
    input.value = value;
});

document.getElementById('date').addEventListener('input', function (e) {
    const input = e.target;
    let value = input.value.replace(/\D/g, '');
    if (value.length > 2) {
        value = value.slice(0, 2) + '-' + value.slice(2, 4) + '-' + value.slice(4, 8);
    }
    input.value = value;
});