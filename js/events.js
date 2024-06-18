const host = 'http://0.0.0.0:4567';
const copyPasta = `title="Click to copy to clipboard" class="clipboard" onclick="clipboard(this)"`;
document.getElementById('selectLogFile').value = localStorage.currentLogFile;


const annotate = async (e, x, y) => {
  e.classList.add('scanned');
  scan(e.textContent, x, y);
}
const showEvidence = async (e, ip) =>  {
  let response = await fetch(`${host}/entries/${ip}`),
      entries = await response.json();
  e.innerHTML = `<pre ${copyPasta}>${entries.content}<pre>`;
}


//this vs adding via folium
/*
const selectMarkup = `
    <select onchange="changeSource(this)" id='selectLogFile'> 
      <option class="option"> auth.log.1.gz </option>
      <option class="option"> auth.log.2.gz </option>
      <option class="option"> auth.log.3.gz </option>
      <option class="option"> auth.log.4.gz </option>
      <option class="option"> ufw.log.gz    </option>
      <option class="option"> ufw.log.1.gz  </option>
    </select>
    <br>
`
*/

//cleaner and fewer calls to api
const scan = async(ip, x, y) => {
  document.getElementById('banner').innerHTML = `scanning...`;
  document.getElementById('banner').style.display = 'block';
  let response = await fetch(`${host}/scan/${ip}`),
      scanData = await response.json(),
      frequency = scanData.frequency,
      entries = scanData.entries,
      isp = scanData.isp,
      ports = scanData.ports;
      users = scanData.users;
      duration = scanData.duration;;
  
  document.getElementById('banner').style.display = 'none';
  document.getElementById('sidebar').innerHTML = `
    ip: <span ${copyPasta}>${ip}</span><br>
    Entries: <em ${copyPasta}>${frequency}</em> <br>
    Location: (<em ${copyPasta}>${x},${y}</em>) <br>
<!--
    duration: ${duration} <br>
-->
    invalid users: <div class="subset"><pre ${copyPasta}>${users}</pre></div>
    <div class="subset" onclick="showEvidence(this, '${ip}')">log entries</div><hr>
    <pre>${isp}</pre><hr>
    <pre>${ports}</pre>`;
    //hide invalid users if we are looking at ufw logs WIP

    //set select to current log file
    setTimeout(() => {
      document.getElementById('selectLogFile').value = localStorage.currentLogFile;
    }, 10);
}

const uploadFile = async () =>  {
  let fileInput = document.getElementById('fileInput');
  let file = fileInput.files[0];
  let formData = new FormData();
  formData.append('file', file);
  let options = {
    method: 'POST',
    body: formData
  };
  try {
    const response = await fetch(`${host}/upload`, options);
    if (response.ok) {
      document.getElementById('sidebar').innerHTML=`
        click on a map marker then click on an ip address in tooltip to obtain ISP, frquency & open ports
      `;
    } else {
      throw new Error('Error uploading file');
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

if(document.querySelector('.custom-file-upload')) {
  document.querySelector('.custom-file-upload').onclick = () => {
    document.getElementById('fileInput').click();  
  }
  document.querySelector('.custom-file-upload input').onchange = () => {
    let p = document.createElement('p');
    p.textContent = document.querySelector('#sidebar .custom-file-upload input').value;
    document.getElementById('sidebar').append(p);
  }
}

const clipboard = (e) => {
  var range = document.createRange();
  range.selectNode(e);
  window.getSelection().removeAllRanges(); // clear current selection
  window.getSelection().addRange(range); // to select text
  document.execCommand("copy");
  window.getSelection().removeAllRanges();// to deselect
  document.getElementById('banner').innerHTML = 'Copied!';
  document.getElementById('banner').style.display = 'block';
  setTimeout(()=> {
    document.getElementById('banner').style.display = 'none';
  }, 1000)
}

//changeSource

const changeSource = async (e) => {
  let options = {
    method: 'put',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
  };
  //ensure list here too :/
  document.getElementById('banner').innerHTML = `loading...`;
  document.getElementById('banner').style.display = 'block';
  const response = await fetch(`${host}/setLogFileTo/${e.value}`, options);
  if(response.ok) {
    let result = await response.json();
    console.log(JSON.stringify(result));
    localStorage.currentLogFile = result.currentLogFile.split("/")[1]
    location.reload();
  }
}
