const btn = document.getElementById('go');
const cityInput = document.getElementById('city');
const result = document.getElementById('result');

btn.addEventListener('click', async () => {
  const city = cityInput.value.trim();
  if (!city) return alert('Enter a city');
  result.textContent = 'Loading...';
  try {
    const resp = await fetch('http://127.0.0.1:8000/weather', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ city }),
    });
    if (!resp.ok) throw new Error(await resp.text());
    const data = await resp.json();
    result.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (err) {
    result.textContent = 'Error: ' + err.message;
  }
});
