
const host = 'http://0.0.0.0:4567';
const annotate = async (e, x, y) => {
  scan(e.textContent, x, y);
}
const showEvidence = async (e, ip) =>  {
  let response = await fetch(`${host}/entries/${ip}`),
      attempts = await response.json();
  e.innerHTML = `<pre>${attempts.content}<pre>`;
}
//cleaner and fewer calls to api
const scan = async(ip, x, y) => {
  document.getElementById('sidebar').innerHTML = `<div><marquee>.•ª•. scanning ${ip} .•ª•.</marquee></div>`;
  let response = await fetch(`${host}/scan/${ip}`),
      scanData = await response.json(),
      frequency = scanData.frequency,
      entries = scanData.entries,
      isp = scanData.isp,
      ports = scanData.ports;
      users = scanData.users;
      duration = scanData.duration;;
  document.getElementById('sidebar').innerHTML = `
    ip: ${ip} <br>
    Entries: ${frequency} <br>
    Location: (${x},${y}) <br>
<!--
    duration: ${duration} <br>
-->
    users: <marquee class="subset">${users}</marquee>
    <div class="subset" onclick="showEvidence(this, '${ip}')">auth.log entries</div><hr>
    <pre>${isp}</pre><hr>
    <pre>${ports}</pre>`;
}
