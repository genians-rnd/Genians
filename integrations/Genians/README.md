<!-- HTML_DOC -->
<div class="cl-preview-section">
<p>Use the Genians integration to block IP using assign tag and unassign tag.</p>
</div>

<div class="cl-preview-section">
<p>Genians’ network sensing technology powered by Device Platform Intelligence (DPI) discovers and presents all detected devices’ business contextual and risk-related information along with their technical information without disturbing existing network infrastructure. The resulting intelligence enhances visibility and allows operators to detect and respond to any non-compliant or compromised devices in real time.</p>
<p>With the result of comprehensive network visibility, Genians can ensure compliance from all connected devices by leveraging Virtual In-Line Packet Inspection which operates at Layer 2. This technology has complete control over endpoint device traffic over TCP and UDP by eliminating the need for complex configurations and network changes.</p>
</div>

<div class="cl-preview-section">
<h2>Genians Genian NAC Module Requirements</h2>
<p>Before you can use this integration in Demisto, you need to enable certain modules in your Genian NAC environment.</p>
<p><strong>Genian NAC Web Console</strong></p>
<ol>
<li>This is the network address of the Genian NAC Enterprise or standalone Appliance. (The host on which the the Genian NAC is hosted.) For example, if the Genian NAC is hosted at the IP address 192.168.100.100, then you enter https://192.168.10.100:8443/mc2 </li>
</ol>
<p><strong>Enforcement Mode</strong></p>
<ol>
<li>Go to System > System > Click IP of Sensor > Click Sensor Tab > Click Sensor on the right</li>
<li>Go to Sensor Operation > Sensor Mode and change the Sensor Mode to 'host'</li>
<li>Change Sensor Operationg Mode to 'Enforcement'</li>
<ul>
<li>Monitoring: (Default) Monitoring mode. No blocking.</li>
<li>Enforcement: Blocking mode</li>
</ul>
</ol>
<p><strong>Specifying the Tag to be assigned to the node under control.</strong></p>
<ol>
<li>Go to Preferences > Properties > Tag</li>
<li>Create new Tag or use existing Tag (e.g. THREAT)</li>
</ol>
<p><strong>Create Enforcement Policy</strong></p>
<ol>
<li>Reference the Enforcement Policy section in the Genians Docs</li>
</ol>
</div>

<div class="cl-preview-section">
<h2>Configuration Parameters</h2>
<p><strong>Server IP</strong></p>
<ol>
<li>If the Genian NAC is hosted at the IP address 192.168.100.100, enter 192.168.100.100.</li>
</ol>
<p><strong>API Key</strong></p>
<ol>
<li>You can generate an API Key in the Genian NAC Web Console.</li>
<li>Go to Management > User > Administrator tab > API Key to generate a key and save it.</li>
</ol>
<p><strong>Tag Name</strong></p>
<ol>
<li>Enter Tag Name to use for IP Block</li>
</ol>
</div>

<div class="cl-preview-section">
<h2>Configure Genians on Demisto</h2>
<ol>
<li>Navigate to Settings > Integrations > Servers & Services.</li>
<li>Search for Genians</li>
<li>Click Add instance to create and configure a new integration instance.</li>
<ul>
<li>Name: a textual name for the integration instance.</li>
<li>Server IP</li>
<li>API Key</li>
<li>Tag Name</li>
</ul>
<li>Click Test to validate the token.</li>
</ol>
</div>

<div class="cl-preview-section">
<h2>Commands</h2>
<p>You can execute these commands from the Demisto CLI, as part of an automation, or in a playbook. After you successfully execute a command, a DBot message appears in the War Room with the command details.</p>
<ol>
<li><a href="#Post IP address to a tag" target="_self">Post IP address to a tag: genian-nac-assign-ip-tag</a></li>
<li><a href="#Delete IP address from a tag" target="_self">Delete IP address from a tag: genian-nac-unassign-ip-tag</a></li>
</ol>
</div>

<div class="cl-preview-section">
<h3 id="Post IP address to a tag">1. Post IP address to a tag</h3>
<p>Assigns a tag to the Node specified.</p>
<h5>Base Command</h5>
<p><code>genian-nac-assign-ip-tag</code></p>
<h5>Input</h5>
<table style="width: 745px;">
<thead>
<tr>
<th style="width: 150px;"><strong>Argument Name</strong></th>
<th style="width: 520px;"><strong>Description</strong></th>
<th style="width: 70px;"><strong>Required</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="width: 150px;">ip</td>
<td style="width: 520px;">IP Address (e.g. 192.168.100.87)</td>
<td style="width: 70px;">Mandatory</td>
</tr>
</tbody>
</table>
<p> </p>
<h5>Context Output</h5>
<table style="width: 745px;">
<thead>
<tr>
<th style="width: 325px;"><strong>Path</strong></th>
<th style="width: 105px;"><strong>Type</strong></th>
<th style="width: 310px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="width: 325px;">genian.nac.tag.nodeId</td>
<td style="width: 105px;">String</td>
<td style="width: 310px;">nodeid of IP</td>
</tr>
<tr>
<td style="width: 325px;">genian.nac.tag.Name</td>
<td style="width: 105px;">String</td>
<td style="width: 310px;">Tag name</td>
</tr>
</tbody>
</table>
<p> </p>
<h5>Raw Output</h5>
<pre>
[
    {
        "Type": "node",
        "Description": "test",
        "IDX": 9,
        "nodeId": "dd9394cc-4495-103a-8010-2cf05d0cf498-537696fb",
        "Name": "THREAT"
    }
]
</pre>
</div>

<div class="cl-preview-section">
<h3 id="Delete IP address from a tag">2. Delete IP address from a tag</h3>
<p>Removes the tag(s) from the Node specified.</p>
<h5>Base Command</h5>
<p><code>genian-nac-unassign-ip-tag</code></p>
<h5>Input</h5>
<table style="width: 745px;">
<thead>
<tr>
<th style="width: 150px;"><strong>Argument Name</strong></th>
<th style="width: 520px;"><strong>Description</strong></th>
<th style="width: 70px;"><strong>Required</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="width: 150px;">ip</td>
<td style="width: 520px;">IP Address (e.g. 192.168.100.87)</td>
<td style="width: 70px;">Mandatory</td>
</tr>
</tbody>
</table>
<p> </p>
<h5>Context Output</h5>
<table style="width: 745px;">
<thead>
<tr>
<th style="width: 325px;"><strong>Path</strong></th>
<th style="width: 105px;"><strong>Type</strong></th>
<th style="width: 310px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="width: 325px;">genian.nac.tag.nodeId</td>
<td style="width: 105px;">String</td>
<td style="width: 310px;">nodeid of IP</td>
</tr>
<tr>
<td style="width: 325px;">genian.nac.tag.Name</td>
<td style="width: 105px;">String</td>
<td style="width: 310px;">Tag name</td>
</tr>
</tbody>
</table>
<p> </p>
<h5>Raw Output</h5>
<pre>
[]
</pre>
</div>
