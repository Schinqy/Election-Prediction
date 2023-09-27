import json
from bs4 import BeautifulSoup

# HTML code with multiple divs
html_code = '''
<div data-original-id="Bulawayo Central" data-content-type="roundMarkers" data-content-index="0" class="igm-map-content" id="bulawayocentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td>Bulawayo Central</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kapoikilu Surrender</td>
<td>CCC</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Charuka Tendayi</td>
<td>ZANU PF</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div>
<div data-original-id="Bulawayo North" data-content-type="roundMarkers" data-content-index="1" class="igm-map-content" id="bulawayonorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Bulawayo North</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumede Minehle Ntandoyenkosi</td>
<td>CCC</td>
<td>10,260</td>
<td></td>
</tr>
<tr>
<td>Khumalo Sibonokuhle</td>
<td>DOP</td>
<td></td>
<p>182</p>
<td></td>
</tr>
<tr>
<td>Mhlanga Frank</td>
<td>UZA</td>
<td>356</td>
<td></td>
</tr>
<tr>
<td>Mkandla Nkosana</td>
<td>ZANU PF</td>
<td>2,679</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div>
<div data-original-id="Bulawayo South" data-content-type="roundMarkers" data-content-index="2" class="igm-map-content" id="bulawayosouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Bulawayo South</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Watson Nicola Jane</td>
<td>CCC</td>
<td>10,470</td>
<td></td>
</tr>
<tr>
<td>Gomba Admore</td>
<td>DOP</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Modi Rajeshkumari</td>
<td>ZANU PF</td>
<td>3,742</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Cowdray Park" data-content-type="roundMarkers" data-content-index="3" class="igm-map-content" id="cowdraypark_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Cowdray Park</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Sibanda Pashor Raphael</td>
<td>CCC</td>
<td>8,411</td>
<td></td>
</tr>
<tr>
<td>Ncube Mthuli</td>
<td>ZANU PF</td>
<td>6,530</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Emakhandeni/ Luveve" data-content-type="roundMarkers" data-content-index="4" class="igm-map-content" id="emakhandeni2fluveve_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong>Emakhandeni/ Luveve</strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bajila Collins Discent</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Nicodemus M</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Khulumani</td>
<td>ZANC</td>
<td>0</td>
</tr>
<tr>
<td>Samuriwo Brian</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Entumbane/ Njube" data-content-type="roundMarkers" data-content-index="5" class="igm-map-content" id="entumbane2fnjube_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong>Entumbane/ Njube</strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Prince</td>
<td>CCC</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Tshuma Dingilizwe</td>
<td>CCC</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chinamano Linda</td>
<td>ZANU PF</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mugurasave Beauty</td>
<td>UZA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ndlovu Nqobizitha</td>
<td>ZANC</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Lobengula/ Magwegwe" data-content-type="roundMarkers" data-content-index="6" class="igm-map-content" id="lobengula2fmagwegwe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong>Lobengula/ Magwegwe</strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gono Ereck</td>
<td>CCC</td>
<td>10,114</td>
<td></td>
</tr>
<tr>
<td>Ndibali Innocent</td>
<td>EFF</td>
<td>142</td>
<td></td>
</tr>
<tr>
<td>Khanye Lwazi</td>
<td>MRP</td>
<td>782</td>
<td></td>
</tr>
<tr>
<td>Zivavose Godwin</td>
<td>UFP</td>
<td>187</td>
<td></td>
</tr>
<tr>
<td>Dube Arnold</td>
<td>UZA</td>
<td>101</td>
<td></td>
</tr>
<tr>
<td>Ncube Douglas</td>
<td>ZANC</td>
<td>139</td>
<td></td>
</tr>
<tr>
<td>Ndhlovu Butholezwe</td>
<td>ZANU PF</td>
<td>2,400</td>
<td></td>
</tr>
<tr>
<td>Ndlovu Nigel</td>
<td>ZAPU</td>
<td>438</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mpopoma/ Mzilikazi" data-content-type="roundMarkers" data-content-index="7" class="igm-map-content" id="mpopoma2fmzilikazi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Mpopoma/Mzilikazi</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Makaza Desmond</td>
<td>CCC</td>
<td>10,808</td>
<td></td>
</tr>
<tr>
<td>Sibanda Blessings</td>
<td>DOP</td>
<td>54</td>
<td></td>
</tr>
<tr>
<td>Muzenda Sihle</td>
<td>F.A</td>
<td>148</td>
<td></td>
</tr>
<tr>
<td>Mkandla Strike</td>
<td>INDEPENDENT</td>
<td>107</td>
<td></td>
</tr>
<tr>
<td>Tapfumaneyi Pardon</td>
<td>INDEPENDENT</td>
<td>570</td>
<td></td>
</tr>
<tr>
<td>Zvikwete Innocent Mbano</td>
<td>ZANC</td>
<td>43</td>
<td></td>
</tr>
<tr>
<td>Masikati Admire Tonderai</td>
<td>ZANU PF</td>
<td>2,433</td>
<td></td>
</tr>
<tr>
<td>Ncube Bekezela</td>
<td>ZAPU</td>
<td>346</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nketa" data-content-type="roundMarkers" data-content-index="8" class="igm-map-content" id="nketa_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong>Nketa</strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Manduna Obert</td>
<td>CCC</td>
<td>10,605</td>
<td></td>
</tr>
<tr>
<td>Ndlovu Vincent Bhala</td>
<td>INDEPENDENT</td>
<td>1,196</td>
<td></td>
</tr>
<tr>
<td>Dube Catherine</td>
<td>UZA</td>
<td>183</td>
<td></td>
</tr>
<tr>
<td>Zidya Tavengwa</td>
<td>ZANU PF</td>
<td>2,556</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nkulumane" data-content-type="roundMarkers" data-content-index="9" class="igm-map-content" id="nkulumane_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong>Nkulumane</strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Desire</td>
<td>CCC</td>
<td>9,880</td>
<td></td>
</tr>
<tr>
<td>Mhlanga Adelaide</td>
<td>FREEZIM CONGRESS</td>
<td>101</td>
<td></td>
</tr>
<tr>
<td>Mtetwa Floridah Deliah</td>
<td>UZA</td>
<td>151</td>
<td></td>
</tr>
<tr>
<td>Bhebhe Nompilo</td>
<td>ZANC</td>
<td>177</td>
<td></td>
</tr>
<tr>
<td>Murechu Freedom Phineas</td>
<td>ZANU PF</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ndlovu Andrew</td>
<td>ZAPU</td>
<td>465</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Pelandaba/ Tshabalala" data-content-type="roundMarkers" data-content-index="10" class="igm-map-content" id="pelandaba2ftshabalala_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Pelandaba/ Tshabalala</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Soneni</td>
<td>CCC</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Siziva Gift</td>
<td>CCC</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ndlovu Gift</td>
<td>DOP</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maplanka Sanpoulus</td>
<td>EFF</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Moureen</td>
<td>UZA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Verenga Cecilia Melody</td>
<td>ZANU PF</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Pumula" data-content-type="roundMarkers" data-content-index="11" class="igm-map-content" id="pumula_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Pumula</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mahlangu Sichelesile</td>
<td>CCC</td>
<td>7,546</td>
<td></td>
</tr>
<tr>
<td>Mhlanga Albert</td>
<td>CCC</td>
<td>2,349</td>
<td></td>
</tr>
<tr>
<td>Msipha Memory</td>
<td>UZA</td>
<td>64</td>
<td></td>
</tr>
<tr>
<td>Nsingo Pumulani</td>
<td>ZANU PF</td>
<td>2,606</td>
<td></td>
</tr>
<tr>
<td>Mkwananzi Trust Mazwi</td>
<td>ZAPU</td>
<td>516</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Budiriro North" data-content-type="roundMarkers" data-content-index="12" class="igm-map-content" id="budirironorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Budiriro North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bizaliel Kennedy</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Gomwe Simbarashe Godwin</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mupundu Simbarashe</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Matsunga Susan</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Budiriro South" data-content-type="roundMarkers" data-content-index="13" class="igm-map-content" id="budirirosouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Budiriro South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chigumbu Darlington Dzikamai</td>
<td>CCC</td>
<td>17,348</td>
</tr>
<tr>
<td>Husayihwevhu Wellington</td>
<td>UZA</td>
<td>148</td>
</tr>
<tr>
<td>Mukweya Tatenda</td>
<td>ZANU-PF</td>
<td>3,703</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chitungwiza North" data-content-type="roundMarkers" data-content-index="14" class="igm-map-content" id="chitungwizanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chitungwiza North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chitoro Nyashadzashe Enock</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Machangara Spencer</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Sithole Godfrey Karakadzayi</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Zambezi Shepherd Ignatius</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chitungwiza South" data-content-type="roundMarkers" data-content-index="15" class="igm-map-content" id="chitungwizasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chitungwiza South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dzvene Elvis</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Kariramombe Shepherd</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mafuratidze Goodwell</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mavhunga Maxwell</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Churu" data-content-type="roundMarkers" data-content-index="16" class="igm-map-content" id="churu_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Churu</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chikomo Traswell</td>
<td>CCC</td>
<td>16,004</td>
</tr>
<tr>
<td>Fundukwa Ephraim</td>
<td>ZANU-PF</td>
<td>14,205</td>
</tr>
<tr>
<td>Nyikadzino Tichaona</td>
<td>CCC</td>
<td>2,459</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Dzivarasekwa" data-content-type="roundMarkers" data-content-index="17" class="igm-map-content" id="dzivarasekwa_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Dzivarasekwa</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chamatowa Lovemore</td>
<td>ZANU-PF</td>
<td>9,227</td>
</tr>
<tr>
<td>Kanzimbe Petronellah</td>
<td>UZA</td>
<td>259</td>
</tr>
<tr>
<td>Mushoriwa Edwin</td>
<td>CCC</td>
<td>16,453</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Epworth North" data-content-type="roundMarkers" data-content-index="18" class="igm-map-content" id="epworthnorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Epworth North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidewu Njodzi</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Kandishaya Taurai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mhetu Togarepi Zivai</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Epworth South" data-content-type="roundMarkers" data-content-index="19" class="igm-map-content" id="epworthsouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Epworth South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bande Didymus</td>
<td>CCC</td>
<td>1,867</td>
</tr>
<tr>
<td>Baramasimbe Solomon</td>
<td>CCC</td>
<td>1,314</td>
</tr>
<tr>
<td>Chatambudza Kudakwashe Blessed</td>
<td>CCC</td>
<td>6,745</td>
</tr>
<tr>
<td>Mwabaya Priston</td>
<td>MDC-T</td>
<td>228</td>
</tr>
<tr>
<td>Taedzwa Honour Mbofana</td>
<td>ZANU-PF</td>
<td>8,112</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Glen Norah" data-content-type="roundMarkers" data-content-index="20" class="igm-map-content" id="glennorah_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Glen Norah</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chikombo Wellington</td>
<td>CCC</td>
<td>17,009</td>
</tr>
<tr>
<td>Chisango Tichaona</td>
<td>UZA</td>
<td>214</td>
</tr>
<tr>
<td>Mupindu Muchineripi</td>
<td>ZANU-PF</td>
<td>4,261</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Glenview North" data-content-type="roundMarkers" data-content-index="21" class="igm-map-content" id="glenviewnorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Glenview North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidziva Happymore</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Chinodya Best</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Mangachena Musekiwa</td>
<td>FREE ZIM CONGRESS</td>
<td>0</td>
</tr>
<tr>
<td>Munyoro Abigail Valerie Tsitsi</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Zamanga Witness Tumelo</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Glenview South" data-content-type="roundMarkers" data-content-index="22" class="igm-map-content" id="glenviewsouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Glenview South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chinyadza Justice</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Hakata Grandmore</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Muchuwe Offard</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Harare Central" data-content-type="roundMarkers" data-content-index="23" class="igm-map-content" id="hararecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Harare Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jimu Lovemore</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Nyaningwe Irvine Hatitye</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Zenda Nyasha Gift</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Harare East" data-content-type="roundMarkers" data-content-index="24" class="igm-map-content" id="harareeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Harare East</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumbo Mavis</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Markham Allan Norman</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mlambo Garikai</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Mutizwa Musarurwa Stewar</td>
<td>MDC-T</td>
<td>0</td>
</tr>
<tr>
<td>Razaru Malvin</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Harare South" data-content-type="roundMarkers" data-content-index="25" class="igm-map-content" id="hararesouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Harare South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hasha Trouble</td>
<td>CCC</td>
<td>4,009</td>
</tr>
<tr>
<td>Kanupula Trymore</td>
<td>ZANU-PF</td>
<td>13,560</td>
</tr>
<tr>
<td>Magweta George</td>
<td>CCC</td>
<td>1,573</td>
</tr>
<tr>
<td>Musonza Dorothy</td>
<td>CCC</td>
<td>7,420</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Harare West" data-content-type="roundMarkers" data-content-index="26" class="igm-map-content" id="hararewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Harare West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mamombe Joanah</td>
<td>CCC</td>
<td>18,141</td>
</tr>
<tr>
<td>Padzarondora Farai Michael</td>
<td>CCC</td>
<td>3,453</td>
</tr>
<tr>
<td>Zindoga Patrick Tendayi</td>
<td>ZANU-PF</td>
<td>3,453</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hatcliffe" data-content-type="roundMarkers" data-content-index="27" class="igm-map-content" id="hatcliffe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hatcliffe</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumbo Agency</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mangwanya David</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Mashongandoro Modock</td>
<td>DUZ</td>
<td>0</td>
</tr>
<tr>
<td>Mudambo Tongesayi</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Sande Lloyd</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hatfield" data-content-type="roundMarkers" data-content-index="28" class="igm-map-content" id="hatfield_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hatfield</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chapinduka Clara</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Griza Admire Adam</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Nyamakanga Paidamoyo</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Nyamuronda Reway</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Highfield" data-content-type="roundMarkers" data-content-index="29" class="igm-map-content" id="highfield_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Highfield</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mashonganyika Mike</td>
<td>ZANU-PF</td>
<td>3,789</td>
</tr>
<tr>
<td>Mavhudzi Donald</td>
<td>CCC</td>
<td>16,857</td>
</tr>
<tr>
<td>Mukunguma Luckson</td>
<td>MDC-T</td>
<td>248</td>
</tr>
<tr>
<td>Ndawana Edina</td>
<td>FREE ZIM CONGRESS</td>
<td>63</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hunyani" data-content-type="roundMarkers" data-content-index="30" class="igm-map-content" id="hunyani_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hunyani</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Baudi Pattence</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Chinoputsa Lovemore</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Khumbula Terrence</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Masunga Sarvory Pedzisai</td>
<td>ZNRP</td>
<td>0</td>
</tr>
<tr>
<td>Mnangagwa Tongai Mafidi</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Kuwadzana East" data-content-type="roundMarkers" data-content-index="31" class="igm-map-content" id="kuwadzanaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Kuwadzana East</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hwende Chalton</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Kayemba Tendayi</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Majavhura Tellme</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mangwiro Urayayi</td>
<td>MDC-T</td>
<td>0</td>
</tr>
<tr>
<td>Takawira Collen Munyaradzi</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Kuwadzana West" data-content-type="roundMarkers" data-content-index="32" class="igm-map-content" id="kuwadzanawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Kuwadzana West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chimbalanga Jossam</td>
<td>INDEPENDENT</td>
<td>272</td>
</tr>
<tr>
<td>Matambo Johnson</td>
<td>CCC</td>
<td>20,043</td>
</tr>
<tr>
<td>Mauka Tauya</td>
<td>ZANU-PF</td>
<td>5,251</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mabvuku/Tafara" data-content-type="roundMarkers" data-content-index="33" class="igm-map-content" id="mabvuku2ftafara_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mabvuku/Tafara</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kufahakutizwi Munyaradzi Febion</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Sakupwanya Pedzai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mbare" data-content-type="roundMarkers" data-content-index="34" class="igm-map-content" id="mbare_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mbare</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chamisa Starman</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Matinyanya Sunungukai Martin</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mount Pleasant" data-content-type="roundMarkers" data-content-index="35" class="igm-map-content" id="mountpleasant_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mount Pleasant</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gwasira Beadle Musatye</td>
<td>ZANU-PF</td>
<td>7,787</td>
</tr>
<tr>
<td>Machokoto Jonathan</td>
<td>CCC</td>
<td>5,510</td>
</tr>
<tr>
<td>Mahere Fadzayi</td>
<td>CCC</td>
<td>12,865</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Southerton" data-content-type="roundMarkers" data-content-index="36" class="igm-map-content" id="southerton_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Southerton</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kunaka Jim</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Nyandoro Bridget</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Nyemba Maureen</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="St Marys" data-content-type="roundMarkers" data-content-index="37" class="igm-map-content" id="stmarys_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>St Marys</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jinjika Norbet</td>
<td>ZANU-PF</td>
<td>77,28</td>
</tr>
<tr>
<td>Masarirevu Freddy Michael</td>
<td>CCC</td>
<td>5,519</td>
</tr>
<tr>
<td>Mazhindu Brighton</td>
<td>CCC</td>
<td>11,094</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Sunningdale" data-content-type="roundMarkers" data-content-index="38" class="igm-map-content" id="sunningdale_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Sunningdale</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Goremusandu Christmas</td>
<td>CCC</td>
<td>2,762</td>
</tr>
<tr>
<td>Kademaunga Maureen</td>
<td>CCC</td>
<td>13,360</td>
</tr>
<tr>
<td>Magweba Loice</td>
<td>ZANU-PF</td>
<td>6,236</td>
</tr>
<tr>
<td>Makaza Jonathan</td>
<td>UZA</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Warren Park" data-content-type="roundMarkers" data-content-index="39" class="igm-map-content" id="warrenpark_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Warren Park</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidawa Tafadzwa</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Hamauswa Shakespear</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>July Antony</td>
<td>UZA</td>
<td>0</td>
</tr>
<tr>
<td>Kutukwa Jonathan Fungayi</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Matika Energy Tanaka</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Musevenzi Julius</td>
<td>MDC-T</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zengeza East" data-content-type="roundMarkers" data-content-index="40" class="igm-map-content" id="zengezaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Zengeza East</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chimbaira Goodrich</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Marume Donald Tinashe</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Mutimbanyoka Kiven</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zengeza West" data-content-type="roundMarkers" data-content-index="41" class="igm-map-content" id="zengezawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Zengeza West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidakwa Simon</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Zvaipa Innocent</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Buhera Central" data-content-type="roundMarkers" data-content-index="42" class="igm-map-content" id="buheracentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Buhera Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kandenga Timothy</td>
<td>CCC</td>
<td>5,276</td>
</tr>
<tr>
<td>Matema Samson</td>
<td>ZANU PF</td>
<td>11,220</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Buhera North" data-content-type="roundMarkers" data-content-index="43" class="igm-map-content" id="buheranorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Buhera North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Guyo Phillip</td>
<td>ZANU PF</td>
<td>12,258</td>
</tr>
<tr>
<td>Magarangoma Julius</td>
<td>CCC</td>
<td>6,756</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Buhera South" data-content-type="roundMarkers" data-content-index="44" class="igm-map-content" id="buherasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Buhera South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hodhera Solomon</td>
<td>CCC</td>
<td>7,912</td>
</tr>
<tr>
<td>Mudekunye Ngonidzashe</td>
<td>ZANU PF</td>
<td>9,222</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Buhera West" data-content-type="roundMarkers" data-content-index="45" class="igm-map-content" id="buherawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Buhera West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mangwanya Herbert</td>
<td>CCC</td>
<td>6,967</td>
</tr>
<tr>
<td>Mugwadi Tafadzwa</td>
<td>ZANU PF</td>
<td>11,087</td>
</tr>
<tr>
<td>Tsvangirai Komborero</td>
<td>MDC-T</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chikanga" data-content-type="roundMarkers" data-content-index="46" class="igm-map-content" id="chikanga_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chikanga</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Charamba Garikayi</td>
<td>NCA</td>
<td>59</td>
</tr>
<tr>
<td>Gambureni Taurai</td>
<td>UZA</td>
<td>115</td>
</tr>
<tr>
<td>Karenyi Lynette</td>
<td>CCC</td>
<td>14,237</td>
</tr>
<tr>
<td>Muchina Kenneth</td>
<td>ZANU-PF</td>
<td>3,853</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chimanimani East" data-content-type="roundMarkers" data-content-index="47" class="igm-map-content" id="chimanimanieast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chimanimani East</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Innocent</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Sacco Joshua Kurt</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chimanimani West" data-content-type="roundMarkers" data-content-index="48" class="igm-map-content" id="chimanimaniwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chimanimani West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maposa Wilson</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Matiashe Canaan</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mushango Isaiah</td>
<td>NCA</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chipinge Central" data-content-type="roundMarkers" data-content-index="49" class="igm-map-content" id="chipingecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chipinge Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dhlumo Livingstone</td>
<td>CCC</td>
<td>11,148</td>
</tr>
<tr>
<td>Machingura Raymore</td>
<td>ZANU PF</td>
<td>13,133</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chipinge East" data-content-type="roundMarkers" data-content-index="50" class="igm-map-content" id="chipingeeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chipinge East</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dhliwayo Lincoln</td>
<td>ZANU-PF</td>
<td>12,186</td>
</tr>
<tr>
<td>Mlambo Mathias Matewu</td>
<td>CCC</td>
<td>8,582</td>
</tr>
<tr>
<td>Mupaji Samuel</td>
<td>NCA</td>
<td>213</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chipinge South" data-content-type="roundMarkers" data-content-index="51" class="igm-map-content" id="chipingesouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chipinge South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hlatywayo Clifford</td>
<td>CCC</td>
<td>11,039</td>
</tr>
<tr>
<td>Maunde Army</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Mlambo Ronald</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Mupakati Takawira</td>
<td>NCA</td>
<td>0</td>
</tr>
<tr>
<td>Porusungazi Enock</td>
<td>ZANU-PF</td>
<td>8,090</td>
</tr>
<tr>
<td>Sithole Nelson</td>
<td>DUZ</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Dangamvura" data-content-type="roundMarkers" data-content-index="52" class="igm-map-content" id="dangamvura_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Dangamvura</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jani Clide</td>
<td>ZANU PF</td>
<td>6,343</td>
</tr>
<tr>
<td>Mutseyami Prosper Chapfiwa</td>
<td>CCC</td>
<td>17,000</td>
</tr>
<tr>
<td>Mwandunguza Lameck Mark</td>
<td>NCA</td>
<td>221</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Headlands" data-content-type="roundMarkers" data-content-index="53" class="igm-map-content" id="headlands_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Headlands</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mapfumo Farai Walter</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Ziswa Valentine Tinodyanavo</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Lastone Julius</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Makoni Central" data-content-type="roundMarkers" data-content-index="54" class="igm-map-content" id="makonicentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Makoni Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Nyika Shepherd</td>
<td>ZANU-PF</td>
<td>8,503</td>
</tr>
<tr>
<td>Sagandira Patrick</td>
<td>CCC</td>
<td>9,644</td>
</tr>
<tr>
<td>Tekeshe David</td>
<td>MDC-T</td>
<td>1,760</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Makoni North" data-content-type="roundMarkers" data-content-index="55" class="igm-map-content" id="makoninorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Makoni North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chitena Shepherd</td>
<td>CCC</td>
<td>6,257</td>
</tr>
<tr>
<td>Muwombi Joseph</td>
<td>ZANU-PF</td>
<td>12,305</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Makoni South" data-content-type="roundMarkers" data-content-index="56" class="igm-map-content" id="makonisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Makoni South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chenai Danmore Tinashe</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Muchauraya Pishai</td>
<td>DUZ</td>
<td>0</td>
</tr>
<tr>
<td>Nyakuedzwa Albert</td>
<td>ZANU-PF</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Makoni West" data-content-type="roundMarkers" data-content-index="57" class="igm-map-content" id="makoniwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Makoni West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gonye Prince</td>
<td>INDEPENDENT</td>
<td>549</td>
</tr>
<tr>
<td>Govha Godfrey Makwasha</td>
<td>CCC</td>
<td>5,899</td>
</tr>
<tr>
<td>Muswere Jenfan</td>
<td>ZANU-PF</td>
<td>10,863</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutare Central" data-content-type="roundMarkers" data-content-index="58" class="igm-map-content" id="mutarecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutare Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>James Leslie Brian</td>
<td>CCC</td>
<td>15,628</td>
</tr>
<tr>
<td>Mupfumi Isau Fungai</td>
<td>ZANU-PF</td>
<td>5,010</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutare North" data-content-type="roundMarkers" data-content-index="59" class="igm-map-content" id="mutarenorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutare North</strong></strong></strong></strong></td>
<td>16,133</td>
<td></td>
</tr>
<tr>
<td>Mahachi Admire</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Takabika Tendai</td>
<td>CCC</td>
<td>7,878</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutare South" data-content-type="roundMarkers" data-content-index="60" class="igm-map-content" id="mutaresouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutare South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dumbarimwe Tawanda</td>
<td>ZANU-PF</td>
<td>12,886</td>
</tr>
<tr>
<td>Saunyama Fungai Mackenzie</td>
<td>CCC</td>
<td>10,386</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutare West" data-content-type="roundMarkers" data-content-index="61" class="igm-map-content" id="mutarewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutare West</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Marange Nyasha</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Munjoma Thomas Dr</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Nemasasi Prayer</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutasa Central" data-content-type="roundMarkers" data-content-index="62" class="igm-map-content" id="mutasacentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutasa Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Benza Innocent Dambudzo</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Chekecheke Dixson</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutasa North" data-content-type="roundMarkers" data-content-index="63" class="igm-map-content" id="mutasanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutasa North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bvute Obey</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Chitsara Godfrey</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutasa South" data-content-type="roundMarkers" data-content-index="64" class="igm-map-content" id="mutasasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutasa South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mugadza Misheck</td>
<td>ZANU-PF</td>
<td>11,608</td>
</tr>
<tr>
<td>Tsunga Regai</td>
<td>CCC</td>
<td>10,383</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutema-Musikavanhu" data-content-type="roundMarkers" data-content-index="65" class="igm-map-content" id="mutema-musikavanhu_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Mutema-Musikavanhu</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chauke Alexander</td>
<td>DUZ</td>
<td>354</td>
</tr>
<tr>
<td>Gata Angeline</td>
<td>ZANU-PF</td>
<td>13,717</td>
</tr>
<tr>
<td>Mudzamiri Thomas</td>
<td>NCA</td>
<td>269</td>
</tr>
<tr>
<td>Nyamudeza Sibonile</td>
<td>CCC</td>
<td>11,475</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nyanga North" data-content-type="roundMarkers" data-content-index="66" class="igm-map-content" id="nyanganorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Nyanga North</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chifodya Nyahando</td>
<td>CCC</td>
<td>8,540</td>
</tr>
<tr>
<td>Sanyatwe Chido</td>
<td>ZANU-PF</td>
<td>13,166</td>
</tr>
<tr>
<td>Mwonzora Munyaradzi</td>
<td>MDC-T</td>
<td>735</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nyanga South" data-content-type="roundMarkers" data-content-index="67" class="igm-map-content" id="nyangasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Nyanga South</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Madziwa Tonderai Joseph</td>
<td>MDC-T</td>
<td>619</td>
</tr>
<tr>
<td>Mandiwanzira Supa Collins</td>
<td>ZANU-PF</td>
<td>10,327</td>
</tr>
<tr>
<td>Mccormick Ruxandra Grigoreta</td>
<td>CCC</td>
<td>9,574</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bindura North" data-content-type="roundMarkers" data-content-index="68" class="igm-map-content" id="binduranorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Bindura North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kajokoto Zvidzai Ruzvidzo</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Kavhukatema Josephat</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Musanhi Kenneth Shupikai</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bindura South" data-content-type="roundMarkers" data-content-index="69" class="igm-map-content" id="bindurasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Bindura South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gwarada George</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Matangira Toendepi Remigious</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Guruve North" data-content-type="roundMarkers" data-content-index="70" class="igm-map-content" id="guruvenorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Guruve North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Pinduka Tendai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Tsikwa Benson</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Guruve South" data-content-type="roundMarkers" data-content-index="71" class="igm-map-content" id="guruvesouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Guruve South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Basa Shupiko</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Magomo Christopher</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Svembere Dominic</td>
<td>NPC-UBUNTU</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mazowe Central" data-content-type="roundMarkers" data-content-index="72" class="igm-map-content" id="mazowecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mazowe Central</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mushonga Shepherd Lenard</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Njanji Maxmore</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mazowe North" data-content-type="roundMarkers" data-content-index="73" class="igm-map-content" id="mazowenorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mazowe North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Makumbe Tsungai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Manyika Elison</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mazowe South" data-content-type="roundMarkers" data-content-index="74" class="igm-map-content" id="mazowesouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mazowe South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chari Rangarirai</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mazungunye Nobert T</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mazowe West" data-content-type="roundMarkers" data-content-index="75" class="igm-map-content" id="mazowewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mazowe West</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kazembe Kazembe</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mataranyika Elija</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mbire" data-content-type="roundMarkers" data-content-index="76" class="igm-map-content" id="mbire_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mbire</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Butau David</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Karembera Blessing</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mt Darwin East" data-content-type="roundMarkers" data-content-index="77" class="igm-map-content" id="mtdarwineast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mt Darwin East</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Butau Dzidzai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Manyika Petiaus</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mt Darwin North" data-content-type="roundMarkers" data-content-index="78" class="igm-map-content" id="mtdarwinnorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mt Darwin North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mapundu Vengai</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Munemo Labbany</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mt Darwin South" data-content-type="roundMarkers" data-content-index="79" class="igm-map-content" id="mtdarwinsouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mt Darwin South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gura Reason</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mupamhanga Kudakwashe</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Tsenengamu Godfrey</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mt Darwin West" data-content-type="roundMarkers" data-content-index="80" class="igm-map-content" id="mtdarwinwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mt Darwin West</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jonga Witness</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Musanhu Zivanai Peter</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Utete Mativenga</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Muzarabani North" data-content-type="roundMarkers" data-content-index="81" class="igm-map-content" id="muzarabaninorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Muzarabani North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kagura Agreement Takawira</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Soda Zhemu</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Muzarabani South" data-content-type="roundMarkers" data-content-index="82" class="igm-map-content" id="muzarabanisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Muzarabani South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gweru Wellington</td>
<td>CCC</td>
<td>1,984</td>
</tr>
<tr>
<td>Kabikira Benjamin</td>
<td>ZANU-PF</td>
<td>22,526</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Rushinga" data-content-type="roundMarkers" data-content-index="83" class="igm-map-content" id="rushinga_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Rushinga</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mutero Cuthbert</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Nyabani Tendai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Shamva North" data-content-type="roundMarkers" data-content-index="84" class="igm-map-content" id="shamvanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Shamva North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chinodakufa Isac</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Maringisanwa Mavis</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Shamva South" data-content-type="roundMarkers" data-content-index="85" class="igm-map-content" id="shamvasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Shamva South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mapiki Joseph</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mugwambi Patrick Tatenda</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chirumanzu" data-content-type="roundMarkers" data-content-index="86" class="igm-map-content" id="chirumanzu_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong>Chirumanzu</strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cheza Patrick</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Rwodzi Barbara</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chirumanzu-Zibagwe" data-content-type="roundMarkers" data-content-index="87" class="igm-map-content" id="chirumanzu-zibagwe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Chirumanzu-Zibagwe</strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chokururama Jacob</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Manyere Obert</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Chireya" data-content-type="roundMarkers" data-content-index="88" class="igm-map-content" id="gokwechireya_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Chireya</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumbo Joseph</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Torerayi</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ndhlukulani Jeremiah</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Gumumyu" data-content-type="roundMarkers" data-content-index="89" class="igm-map-content" id="gokwegumumyu_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Gumumyu</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chabata Misheck</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ngwenya Stephen</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Kabuyuni" data-content-type="roundMarkers" data-content-index="90" class="igm-map-content" id="gokwekabuyuni_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Kabuyuni</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Tshuma Givemore</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Tshuma Spencer</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Nembudziya" data-content-type="roundMarkers" data-content-index="91" class="igm-map-content" id="gokwenembudziya_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Nembudziya</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bangure Donwell</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Buka Flora</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Muswere Ndemera</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Central" data-content-type="roundMarkers" data-content-index="92" class="igm-map-content" id="gokwecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Central</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chitiyo Richard</td>
<td>ZAPU</td>
<td>408</td>
</tr>
<tr>
<td>Masvisvi Daveson</td>
<td>ZANU PF</td>
<td>12,315</td>
</tr>
<tr>
<td>Mears Spencer Valentine</td>
<td>INDEPENDENT</td>
<td>185</td>
</tr>
<tr>
<td>Shava Hope</td>
<td>CCC</td>
<td>11,317</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Kana" data-content-type="roundMarkers" data-content-index="93" class="igm-map-content" id="gokwekana_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Kana</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ncube Owen</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Owen</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Mapfungautsi" data-content-type="roundMarkers" data-content-index="94" class="igm-map-content" id="gokwemapfungautsi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Mapfungautsi</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Karikoga Tawanda</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Kulambone Tawanda</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Zhiva Rueben</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Sengwa" data-content-type="roundMarkers" data-content-index="95" class="igm-map-content" id="gokwesengwa_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Sengwa</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mavima Paul</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Padzakashamba Nhamo</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gokwe Sesame" data-content-type="roundMarkers" data-content-index="96" class="igm-map-content" id="gokwesesame_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Gokwe Sesame</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Matiza Madron</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Manyika Diamond</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiwundura" data-content-type="roundMarkers" data-content-index="97" class="igm-map-content" id="chiwundura_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Chiwundura</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kwidini Sleiman Timios</td>
<td>ZANU PF</td>
<td>10,890</td>
</tr>
<tr>
<td>Murondiwa Blessing</td>
<td>CCC</td>
<td>7,266</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gweru Urban" data-content-type="roundMarkers" data-content-index="98" class="igm-map-content" id="gweruurban_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong>Gweru Urban</strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Brian</td>
<td>MDC-T</td>
<td>672</td>
<td>0</td>
</tr>
<tr>
<td>Makombe Josiah</td>
<td>CCC</td>
<td>12,450</td>
<td>0</td>
</tr>
<tr>
<td>Mukwembi Alex</td>
<td>ZANU PF</td>
<td>5,422</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mkoba South" data-content-type="roundMarkers" data-content-index="99" class="igm-map-content" id="mkobasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mkoba South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chadoka Albert</td>
<td>MDC-T</td>
<td>0</td>
</tr>
<tr>
<td>Kuka John</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Magura Wellington</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Zimano Shelter</td>
<td>UZA</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mkoba North" data-content-type="roundMarkers" data-content-index="100" class="igm-map-content" id="mkobanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mkoba North</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Antonio Learmore</td>
<td>FREEZIM CONGRESS</td>
<td>68</td>
</tr>
<tr>
<td>Chibaya Amo</td>
<td>CCC</td>
<td>12,555</td>
</tr>
<tr>
<td>Gondo William</td>
<td>ZANU PF</td>
<td>4,906</td>
</tr>
<tr>
<td>Kandai Clifford</td>
<td>MDC-T</td>
<td>124</td>
</tr>
<tr>
<td>Mkandhla Tadios</td>
<td>UZA</td>
<td>56</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Vungu" data-content-type="roundMarkers" data-content-index="101" class="igm-map-content" id="vungu_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Vungu</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mgiyelwa Innocent</td>
<td>DOP</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Lawrene</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Brown</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Kwekwe Central" data-content-type="roundMarkers" data-content-index="102" class="igm-map-content" id="kwekwecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Kwekwe Central</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Manwere Dereck</td>
<td>UZA</td>
<td>113</td>
</tr>
<tr>
<td>Ncube Energy</td>
<td>ZANU PF</td>
<td>6,541</td>
</tr>
<tr>
<td>Ndlovu Mbekezeli</td>
<td>MDC-T</td>
<td>0</td>
</tr>
<tr>
<td>Tobaiwa Judith</td>
<td>CCC</td>
<td>10,993</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mbizo" data-content-type="roundMarkers" data-content-index="103" class="igm-map-content" id="mbizo_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Mbizo</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Madzivanyika Corban</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mambende Terrence</td>
<td>MDC-T</td>
<td>0</td>
</tr>
<tr>
<td>Mupereri Vongaishe</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Redcliff" data-content-type="roundMarkers" data-content-index="104" class="igm-map-content" id="redcliff_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Redcliff</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kasiriwori Unique</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Mukapiko Dzikamai Lloyd</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Moyo July</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Shamairai Lister</td>
<td>UZA</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Silobela" data-content-type="roundMarkers" data-content-index="105" class="igm-map-content" id="silobela_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Silobela</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jona Nyevera</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Munhazu Rafson</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Ndebele Ephraim Makhele</td>
<td>ZAPU</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Ephraim</td>
<td>CCC</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zhombe" data-content-type="roundMarkers" data-content-index="106" class="igm-map-content" id="zhombe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Zhombe</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ntini Benison Judah</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Samambwa Edmore</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mberengwa Central" data-content-type="roundMarkers" data-content-index="107" class="igm-map-content" id="mberengwacentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Mberengwa Central</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Shumba Tinashe</td>
<td>ZANU PF</td>
<td>17,689</td>
</tr>
<tr>
<td>Zhou Takavafira</td>
<td>CCC</td>
<td>3,867</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mberengwa East" data-content-type="roundMarkers" data-content-index="108" class="igm-map-content" id="mberengwaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Mberengwa East</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hungwe Tasara</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Shoko Davies</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mberengwa West" data-content-type="roundMarkers" data-content-index="109" class="igm-map-content" id="mberengwawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Mberengwa West</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Msipa Dambudzo</td>
<td>FREEZIM CONGRESS</td>
<td>559</td>
</tr>
<tr>
<td>Moyo Onias</td>
<td>CCC</td>
<td>4,815</td>
</tr>
<tr>
<td>Zhou Tafanana</td>
<td>ZANU PF</td>
<td>13,795</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Shurugwi North" data-content-type="roundMarkers" data-content-index="110" class="igm-map-content" id="shurugwinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Shurugwi North</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mhindu Phillip</td>
<td>CCC</td>
<td>9,094</td>
</tr>
<tr>
<td>Mpasi Joseph</td>
<td>ZANU PF</td>
<td>13,919</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Shurugwi South" data-content-type="roundMarkers" data-content-index="111" class="igm-map-content" id="shurugwisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong>Shurugwi South</strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mhlanga Michael</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mhuri Wilson</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvishavane-Ngezi" data-content-type="roundMarkers" data-content-index="112" class="igm-map-content" id="zvishavane-ngezi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvishavane-Ngezi</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jaravaza Mecky</td>
<td>ZANU PF</td>
<td>12,124</td>
</tr>
<tr>
<td>Mudisi Leopold</td>
<td>CCC</td>
<td>11,607</td>
</tr>
<tr>
<td>Nyoni Michael</td>
<td>INDEPENDENT</td>
<td>165</td>
</tr>
<tr>
<td>Sibanda Sheunopa</td>
<td>MDC-T</td>
<td>163</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvishavane Runde" data-content-type="roundMarkers" data-content-index="113" class="igm-map-content" id="zvishavanerunde_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvishavane Runde</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Fred</td>
<td>ZANU PF</td>
<td>0</td>
</tr>
<tr>
<td>Muchegwa Gift Ipai</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Beitbridge East" data-content-type="roundMarkers" data-content-index="114" class="igm-map-content" id="beitbridgeeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Beitbridge East</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ndou Renatho</td>
<td>CCC</td>
<td>5,626</td>
<td>0</td>
</tr>
<tr>
<td>Nguluvhe Albert</td>
<td>ZANU-PF</td>
<td>8,635</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Beitbridge West" data-content-type="roundMarkers" data-content-index="115" class="igm-map-content" id="beitbridgewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Beitbridge West</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ncube Morgan</td>
<td>CCC</td>
<td>7,428</td>
<td>0</td>
</tr>
<tr>
<td>Ndou Moffat Cephas</td>
<td>INDEPENDENT</td>
<td>1,114</td>
<td>0</td>
</tr>
<tr>
<td>Ndou Thusani</td>
<td>ZANU-PF</td>
<td>7,332</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bulilima" data-content-type="roundMarkers" data-content-index="116" class="igm-map-content" id="bulilima_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Bulilima</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maplanka Bekezela</td>
<td>CCC</td>
<td>6,660</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Aleck</td>
<td>MRP</td>
<td>50</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Artwell</td>
<td>ZAPU</td>
<td>933</td>
<td>0</td>
</tr>
<tr>
<td>Phuti Dingumuzi</td>
<td>ZANU-PF</td>
<td>7,185</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gwanda North" data-content-type="roundMarkers" data-content-index="117" class="igm-map-content" id="gwandanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Gwanda North</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ncube Lungisani Coster Twominutes</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Nkala Desire</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gwanda South" data-content-type="roundMarkers" data-content-index="118" class="igm-map-content" id="gwandasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Gwanda South</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Patrick</td>
<td>CCC</td>
<td>5,099</td>
<td>0</td>
</tr>
<tr>
<td>Gumbo Happy</td>
<td>UZA</td>
<td>269</td>
<td>0</td>
</tr>
<tr>
<td>Marupi Omphile</td>
<td>ZANU-PF</td>
<td>7,941</td>
<td>0</td>
</tr>
<tr>
<td>Nare Timothy</td>
<td>ZAPU</td>
<td>270</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gwanda Tshitaudze" data-content-type="roundMarkers" data-content-index="119" class="igm-map-content" id="gwandatshitaudze_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Gwanda Tshitaudze</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mazhale Jastone</td>
<td>CCC</td>
<td>5,839</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Fisani</td>
<td>ZANU-PF</td>
<td>8,671</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Luckson</td>
<td>ZAPU</td>
<td>271</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Insiza North" data-content-type="roundMarkers" data-content-index="120" class="igm-map-content" id="insizanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Insiza North</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Masuku David</td>
<td>CCC</td>
<td>4,837</td>
<td>0</td>
</tr>
<tr>
<td>Taruvinga Farai</td>
<td>ZANU-PF</td>
<td>9,716</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Insiza South" data-content-type="roundMarkers" data-content-index="121" class="igm-map-content" id="insizasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Insiza South</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Sifanjani Paul</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Sithole Spare</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mangwe" data-content-type="roundMarkers" data-content-index="122" class="igm-map-content" id="mangwe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Mangwe</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Gobosamang</td>
<td>MRP</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Nkomo Thembinkosi</td>
<td>ZAPU</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>Nleya Sandisiwe</td>
<td>ZANU-PF</td>
<td>6,506</td>
<td>0</td>
</tr>
<tr>
<td>Sihlabo Vincent</td>
<td>CCC</td>
<td>7,705</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Matobo" data-content-type="roundMarkers" data-content-index="123" class="igm-map-content" id="matobo_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Matobo</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Nicholas Abson</td>
<td>ZAPU</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Edgar</td>
<td>ZANU-PF</td>
<td>7,366</td>
<td>0</td>
</tr>
<tr>
<td>Ngwenya Collen</td>
<td>CCC</td>
<td>6,219</td>
<td>0</td>
</tr>
<tr>
<td>Nyathi Mlungisi</td>
<td>INDEPENDENT</td>
<td>278</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Matobo Mangwe" data-content-type="roundMarkers" data-content-index="124" class="igm-map-content" id="matobomangwe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Matobo Mangwe</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Khuphe Patriotic</td>
<td>ZAPU</td>
<td>1,554</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Soul</td>
<td>ZANU-PF</td>
<td>5,046</td>
<td>0</td>
</tr>
<tr>
<td>Ndebele Madalaboy</td>
<td>CCC</td>
<td>6,701</td>
<td>0</td>
</tr>
<tr>
<td>Ngwenya Jacob</td>
<td>INDEPENDENT</td>
<td>326</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Umzingwane" data-content-type="roundMarkers" data-content-index="125" class="igm-map-content" id="umzingwane_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong>Umzingwane</strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mayihlome Levi</td>
<td>ZANU-PF</td>
<td>7,416</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Mcebisi</td>
<td>CCC</td>
<td>7,232</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Binga North" data-content-type="roundMarkers" data-content-index="126" class="igm-map-content" id="binganorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong>Binga North</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Munsaka Kudakwashe Mavula</td>
<td>ZANU-PF</td>
<td>9,663</td>
<td>0</td>
</tr>
<tr>
<td>Munsaka Million</td>
<td>NCA</td>
<td>289</td>
<td>0</td>
</tr>
<tr>
<td>Nyoni Peter</td>
<td>INDEPENDENT</td>
<td>174</td>
<td>0</td>
</tr>
<tr>
<td>Siachami Wessele Siankumba</td>
<td>MDC-T</td>
<td>288</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Dubeko Prince</td>
<td>CCC</td>
<td>13,530</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Binga South" data-content-type="roundMarkers" data-content-index="127" class="igm-map-content" id="bingasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong>Binga South</strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cumazala Fanuel</td>
<td>CCC</td>
<td>10,967</td>
<td>0</td>
</tr>
<tr>
<td>Gava Anesu</td>
<td>ZCPD</td>
<td>349</td>
<td>0</td>
</tr>
<tr>
<td>Kujulu Munkombwe Themba Toonset</td>
<td>INDEPENDENT</td>
<td>1,044</td>
<td>0</td>
</tr>
<tr>
<td>Phiri Challenge</td>
<td>ZANU-PF</td>
<td>7,258</td>
<td>0</td>
</tr>
<tr>
<td>Sianaga John</td>
<td>INDEPENDENT</td>
<td>174</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bubi" data-content-type="roundMarkers" data-content-index="128" class="igm-map-content" id="bubi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong>Bubi</strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mabhena Bekhithemba</td>
<td>CCC</td>
<td>4,672</td>
<td>0</td>
</tr>
<tr>
<td>Mathe Nkululeko</td>
<td>INDEPENDENT</td>
<td>899</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Luke</td>
<td>ZAPU</td>
<td>753</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Enerst</td>
<td>Free Zim Congress</td>
<td>150</td>
<td>0</td>
</tr>
<tr>
<td>Nyathi Bekezela</td>
<td>UANC</td>
<td>250</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Fortune Jamela</td>
<td>MDC-T</td>
<td>583</td>
<td></td>
</tr>
<tr>
<td>Sibanda Simelisizwe</td>
<td>ZANU-PF</td>
<td>11,208</td>
<td></td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hwange Central" data-content-type="roundMarkers" data-content-index="129" class="igm-map-content" id="hwangecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hwange Central</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chinene Brian</td>
<td>INDEPENDENT</td>
<td>225</td>
<td>0</td>
</tr>
<tr>
<td>Dube Reed</td>
<td>ZANU-PF</td>
<td>5,157</td>
<td>0</td>
</tr>
<tr>
<td>Molokela-Tsiye Fortune Daniel</td>
<td>CCC</td>
<td>9,167</td>
<td>0</td>
</tr>
<tr>
<td>Ndhlovu Cosmas</td>
<td>INDEPENDENT</td>
<td>646</td>
<td>0</td>
</tr>
<tr>
<td>Nkomazana Salani</td>
<td>MDC-T</td>
<td>102</td>
<td>0</td>
</tr>
<tr>
<td>Nyathi Harriet</td>
<td>Free Zim Congress</td>
<td>74</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hwange East" data-content-type="roundMarkers" data-content-index="130" class="igm-map-content" id="hwangeeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hwange East</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bonda Joseph</td>
<td>CCC</td>
<td>8,931</td>
<td>0</td>
</tr>
<tr>
<td>Phiri Michael</td>
<td>MDC-T</td>
<td>684</td>
<td>0</td>
</tr>
<tr>
<td>Sikuka Alois Sundano</td>
<td>ZANU-PF</td>
<td>8,485</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hwange West" data-content-type="roundMarkers" data-content-index="131" class="igm-map-content" id="hwangewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Hwange West</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dhlamini Somveli</td>
<td>MDC-T</td>
<td>1,985</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Philani</td>
<td>ZANU-PF</td>
<td>7,504</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Vusumuzi</td>
<td>CCC</td>
<td>7,954</td>
<td>0</td>
</tr>
<tr>
<td>Nkomo Ditshoni</td>
<td>ZAPU</td>
<td>186</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Lupane East" data-content-type="roundMarkers" data-content-index="132" class="igm-map-content" id="lupaneeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Lupane East</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumbo Mtenjwa</td>
<td>ZAPU</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Machangu Ncube Phathisiwe</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Ezekiel</td>
<td>UZA</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Vanya Moyo Bright</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Lupane West" data-content-type="roundMarkers" data-content-index="133" class="igm-map-content" id="lupanewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Lupane West</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Keswa Engelinah</td>
<td>MDC-T</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Henry</td>
<td>UZA</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Mpumelelo</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Mxolisi Charles</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nkayi North" data-content-type="roundMarkers" data-content-index="134" class="igm-map-content" id="nkayinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Nkayi North</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mathema Sithabisiwe</td>
<td>INDEPENDENT</td>
<td>804</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Chief</td>
<td>MDC-T</td>
<td>4,065</td>
<td>0</td>
</tr>
<tr>
<td>Ndlovu Mandla</td>
<td>CCC</td>
<td>3,110</td>
<td>0</td>
</tr>
<tr>
<td>Nyoni Sithembiso Gile G</td>
<td>ZANU-PF</td>
<td>5,492</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Nkayi South" data-content-type="roundMarkers" data-content-index="135" class="igm-map-content" id="nkayisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong>Nkayi South</strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hadebe Jabulani</td>
<td>CCC</td>
<td>6,269</td>
</tr>
<tr>
<td>Mathe Stars</td>
<td>ZANU PF</td>
<td>5,066</td>
</tr>
<tr>
<td>Moyo Clilopasi</td>
<td>ZAPU</td>
<td>576</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Tsholotsho North" data-content-type="roundMarkers" data-content-index="136" class="igm-map-content" id="tsholotshonorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Tsholotsho North</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dube Francis Engelbert</td>
<td>UZA</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Gumbo Dokotela</td>
<td>ZAPU</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Khumalo Sibangumuzi Sixtone</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Vincent</td>
<td>INDEPENDENT</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Libion</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Tsholotsho South" data-content-type="roundMarkers" data-content-index="137" class="igm-map-content" id="tsholotshosouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Tsholotsho South</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Moyo Bongani</td>
<td>INDEPENDENT</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Mthombeni Leonard</td>
<td>ZAPU</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Musa</td>
<td>ZANU-PF</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Tapson Nganunu</td>
<td>CCC</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Umguza" data-content-type="roundMarkers" data-content-index="138" class="igm-map-content" id="umguza_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong>Umguza</strong></strong></strong></strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maligwa Queen</td>
<td>INDEPENDENT</td>
<td>8,070</td>
<td>0</td>
</tr>
<tr>
<td>Moyo Richard</td>
<td>ZANU-PF</td>
<td>11,718</td>
<td>0</td>
</tr>
<tr>
<td>Ncube Khumbulani Peter</td>
<td>DOP</td>
<td>151</td>
<td>0</td>
</tr>
<tr>
<td>Sibanda Young</td>
<td>INDEPENDENT</td>
<td>144</td>
<td>0</td>
</tr>
<tr>
<td>Wilson Andrew</td>
<td>UZA</td>
<td>194</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chikomba East" data-content-type="roundMarkers" data-content-index="139" class="igm-map-content" id="chikombaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chikomba East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mhona Felix Tapiwa</td>
<td>ZANU PF</td>
<td>12,089</td>
</tr>
<tr>
<td>Muvirimi Raymond Mutambudzi</td>
<td>INDEPENDENT</td>
<td>159</td>
</tr>
<tr>
<td>Chinembiri Muchengeti</td>
<td>CCC</td>
<td>6,202</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chikomba West" data-content-type="roundMarkers" data-content-index="140" class="igm-map-content" id="chikombawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chikomba West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mavetera Tatenda Annastacia</td>
<td>ZANU PF</td>
<td>19,620</td>
</tr>
<tr>
<td>Punungwe Emmanuel</td>
<td>CCC</td>
<td>7,860</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Goromonzi North" data-content-type="roundMarkers" data-content-index="141" class="igm-map-content" id="goromonzinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Goromonzi North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bvute Ozias</td>
<td>ZANU PF</td>
<td>14,546</td>
</tr>
<tr>
<td>Muchuwa Chenesai</td>
<td>CCC</td>
<td>10,881</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Goromonzi South" data-content-type="roundMarkers" data-content-index="142" class="igm-map-content" id="goromonzisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Goromonzi South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chagwiza Stephen</td>
<td>CCC</td>
<td>16,312</td>
</tr>
<tr>
<td>Chikonye Tinashe</td>
<td>ZANU-PF</td>
<td>15,216</td>
</tr>
<tr>
<td>Chikudo Rueben</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Chirenje Julieth</td>
<td>INDEPENDENT</td>
<td>421</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Goromonzi West" data-content-type="roundMarkers" data-content-index="143" class="igm-map-content" id="goromonziwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Goromonzi West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Karimatsenga Nyamupinga Biatah<br />Beatrice</td>
<td>ZANU-PF</td>
<td>12,072</td>
</tr>
<tr>
<td>Munetsi Tineyi</td>
<td>CCC</td>
<td>10,692</td>
</tr>
<tr>
<td>Nhamburo Taurai Clifford</td>
<td>INDEPENDENT</td>
<td>2,139</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Ruwa" data-content-type="roundMarkers" data-content-index="144" class="igm-map-content" id="ruwa_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Ruwa</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gwanzura Oswell Ndumo</td>
<td>ZANU-PF</td>
<td>9,373</td>
</tr>
<tr>
<td>Muwodzeri Thomas</td>
<td>CCC</td>
<td>16,986</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Marondera Central" data-content-type="roundMarkers" data-content-index="145" class="igm-map-content" id="maronderacentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Marondera Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kundiona Cleopas</td>
<td>ZANU-PF</td>
<td>9,714</td>
</tr>
<tr>
<td>Manyere Misheck</td>
<td>CCC</td>
<td>1,763</td>
</tr>
<tr>
<td>Matewu Caston</td>
<td>CCC</td>
<td>14,712</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Marondera East" data-content-type="roundMarkers" data-content-index="146" class="igm-map-content" id="maronderaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Marondera East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mutokonyi Vimbayi</td>
<td>ZANU-PF</td>
<td>15,221</td>
</tr>
<tr>
<td>Tasirenhamo Thomas</td>
<td>DUZ</td>
<td>262</td>
</tr>
<tr>
<td>Zhuwarara Kizito</td>
<td>CCC</td>
<td>3,566</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Marondera West" data-content-type="roundMarkers" data-content-index="147" class="igm-map-content" id="maronderawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Marondera West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Magwenzi Eddington</td>
<td>CCC</td>
<td>11,106</td>
</tr>
<tr>
<td>Maisvoreva Amon</td>
<td>ZNRP</td>
<td>487</td>
</tr>
<tr>
<td>Munhunepi Tichaona</td>
<td>INDEPENDENT</td>
<td>483</td>
</tr>
<tr>
<td>Tavaziva Godwin</td>
<td>ZANU PF</td>
<td>18,297</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mudzi North" data-content-type="roundMarkers" data-content-index="148" class="igm-map-content" id="mudzinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mudzi North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Musweweshiri Benjamin</td>
<td>ZANU-PF</td>
<td>15,099</td>
</tr>
<tr>
<td>Mututa Paradzai</td>
<td>CCC</td>
<td>2,858</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mudzi South" data-content-type="roundMarkers" data-content-index="149" class="igm-map-content" id="mudzisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mudzi South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Nyambo Tichafa</td>
<td>CCC</td>
<td>2,376</td>
</tr>
<tr>
<td>Samukange Jonathan Tawonana</td>
<td>ZANU-PF</td>
<td>20,653</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mudzi West" data-content-type="roundMarkers" data-content-index="150" class="igm-map-content" id="mudziwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mudzi West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kaitano Knowledge</td>
<td>ZANU-PF</td>
<td>18,513</td>
</tr>
<tr>
<td>Maja Tatenda</td>
<td>CCC</td>
<td>1,583</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Murewa North" data-content-type="roundMarkers" data-content-index="151" class="igm-map-content" id="murewanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Murewa North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Garwe Daniel</td>
<td>ZANU-PF</td>
<td>14,870</td>
</tr>
<tr>
<td>Magaso Peter</td>
<td>UANC</td>
<td>324</td>
</tr>
<tr>
<td>Mangwende Eunice Tambudzai</td>
<td>INDEPENDENT</td>
<td>1,323</td>
</tr>
<tr>
<td>Nyabinde Kennedy</td>
<td>CCC</td>
<td>7,215</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Murewa South" data-content-type="roundMarkers" data-content-index="152" class="igm-map-content" id="murewasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Murewa South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bume Timothy</td>
<td>CCC</td>
<td>2,902</td>
</tr>
<tr>
<td>Mangondo Noah Takawota Joni</td>
<td>ZANU-PF</td>
<td>19,657</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Murewa West" data-content-type="roundMarkers" data-content-index="153" class="igm-map-content" id="murewawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Murewa West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jere Farai</td>
<td>ZANU-PF</td>
<td>17,733</td>
</tr>
<tr>
<td>Mukurazhizha Lesley Manika</td>
<td>CCC</td>
<td>7,271</td>
</tr>
<tr>
<td>Nhamburo Silence</td>
<td>INDEPENDENT</td>
<td>114</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutoko East" data-content-type="roundMarkers" data-content-index="154" class="igm-map-content" id="mutokoeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mutoko East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kaseke Yeukai</td>
<td>CCC</td>
<td>3,613</td>
</tr>
<tr>
<td>Musiyiwa Richard</td>
<td>ZANU-PF</td>
<td>19,073</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutoko North" data-content-type="roundMarkers" data-content-index="155" class="igm-map-content" id="mutokonorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mutoko North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Makwiranzou Caleb</td>
<td>ZANU-PF</td>
<td>16,132</td>
</tr>
<tr>
<td>Mavhoko Taurai</td>
<td>CCC</td>
<td>4,031</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mutoko South" data-content-type="roundMarkers" data-content-index="156" class="igm-map-content" id="mutokosouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mutoko South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mapengo Mapango</td>
<td>CCC</td>
<td>4,296</td>
</tr>
<tr>
<td>Tasikani Isaac</td>
<td>ZANU-PF</td>
<td>17,459</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Seke" data-content-type="roundMarkers" data-content-index="157" class="igm-map-content" id="seke_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Seke</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kashambe Munyaradzi Tobias</td>
<td>ZANU PF</td>
<td>13,277</td>
</tr>
<tr>
<td>Madzimbamuto Willard Tapfumanei</td>
<td>CCC</td>
<td>14,032</td>
</tr>
<tr>
<td>Muzanenhamo Frederick</td>
<td>DUZ</td>
<td>235</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Maramba Pfungwe" data-content-type="roundMarkers" data-content-index="158" class="igm-map-content" id="marambapfungwe_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Maramba Pfungwe</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chimunhu Chiratidzo</td>
<td>CCC</td>
<td>1,448</td>
</tr>
<tr>
<td>Karumazondo Tichawona Makuwi</td>
<td>ZANU-PF</td>
<td>25,757</td>
</tr>
<tr>
<td>Mupukuta Ndinyarei</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Uzumba" data-content-type="roundMarkers" data-content-index="159" class="igm-map-content" id="uzumba_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Uzumba</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Konono Cosmas</td>
<td>CCC</td>
<td>1,977</td>
</tr>
<tr>
<td>Muchemwa Wiriranai</td>
<td>ZANU-PF</td>
<td>24,588</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Wedza North" data-content-type="roundMarkers" data-content-index="160" class="igm-map-content" id="wedzanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Wedza North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Fidelis Eunice</td>
<td>ZNRP</td>
<td>664</td>
</tr>
<tr>
<td>Katsaya Mapfumo</td>
<td>CCC</td>
<td>5,711</td>
</tr>
<tr>
<td>Ndudzo Itai</td>
<td>ZANU-PF</td>
<td>18,762</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Wedza South" data-content-type="roundMarkers" data-content-index="161" class="igm-map-content" id="wedzasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Wedza South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Machakarika Tinoda</td>
<td>ZANU-PF</td>
<td>12,563</td>
</tr>
<tr>
<td>Zinhumwe Valentine</td>
<td>CCC</td>
<td>5,822</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chegutu East" data-content-type="roundMarkers" data-content-index="162" class="igm-map-content" id="chegutueast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chegutu East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mandere Gabriel</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Shamu Webster Kotiwani</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chegutu West" data-content-type="roundMarkers" data-content-index="163" class="igm-map-content" id="chegutuwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chegutu West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chigavazira Last Farai</td>
<td>ZANU-PF</td>
<td>11,308</td>
</tr>
<tr>
<td>Chivero Admore</td>
<td>CCC</td>
<td>13,042</td>
</tr>
<tr>
<td>Konjana Gift Machoka</td>
<td>INDEPENDENT</td>
<td>875</td>
</tr>
<tr>
<td>Makiyi Elizabeth</td>
<td>INDEPENDENT</td>
<td>72</td>
</tr>
<tr>
<td>Matibe Takalani Prince</td>
<td>INDEPENDENT</td>
<td>320</td>
</tr>
<tr>
<td>Munatsi Owen</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mhondoro-Mubaira" data-content-type="roundMarkers" data-content-index="164" class="igm-map-content" id="mhondoro-mubaira_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mhondoro-Mubaira</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mubaira Jonathan</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Chivaura Vengai</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Chiwanza Rodrick Chamunorwa A</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Norton" data-content-type="roundMarkers" data-content-index="165" class="igm-map-content" id="norton_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Norton</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mliswa Temba Peter</td>
<td>INDEPENDENT</td>
<td>7,518</td>
</tr>
<tr>
<td>Shamu Constance</td>
<td>ZANU PF</td>
<td>5,017</td>
</tr>
<tr>
<td>Tsvangirayi Richard</td>
<td>CCC</td>
<td>13,089</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hurungwe Central" data-content-type="roundMarkers" data-content-index="166" class="igm-map-content" id="hurungwecentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Hurungwe Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mazhambe Joel</td>
<td>FREEZIM</td>
<td>0</td>
</tr>
<tr>
<td>Musochi Christopher</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ziki Richard</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hurungwe East" data-content-type="roundMarkers" data-content-index="167" class="igm-map-content" id="hurungweeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Hurungwe East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kangausaru Chenjerai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mandava Blessing</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hurungwe North" data-content-type="roundMarkers" data-content-index="168" class="igm-map-content" id="hurungwenorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Hurungwe North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mangwaira Stanford</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Muringazuva Pax</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Hurungwe West" data-content-type="roundMarkers" data-content-index="169" class="igm-map-content" id="hurungwewest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Hurungwe West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Kambuzuma Chinjai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Zvarevashe Innocent</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Magunje" data-content-type="roundMarkers" data-content-index="170" class="igm-map-content" id="magunje_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Magunje</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jasi Gabriel</td>
<td>INDEPENDENT</td>
<td>453</td>
</tr>
<tr>
<td>Kusemamuriwo Tonderayi Todd</td>
<td>CCC</td>
<td>8,422</td>
</tr>
<tr>
<td>Monga Super</td>
<td>ZANU-PF</td>
<td>10,121</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Kariba" data-content-type="roundMarkers" data-content-index="171" class="igm-map-content" id="kariba_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Kariba</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chiweshe Doras</td>
<td>FREEZIM</td>
<td>0</td>
</tr>
<tr>
<td>Gwangwaba Shine</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Mugadza Patrick Phillip</td>
<td>DOP</td>
<td>0</td>
</tr>
<tr>
<td>Mutsau Andrew</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Shamu Tichaona Nigeil</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chinhoyi" data-content-type="roundMarkers" data-content-index="172" class="igm-map-content" id="chinhoyi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chinhoyi</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidzomba Thomas</td>
<td>ZANU PF</td>
<td>10,051</td>
</tr>
<tr>
<td>Mhangwa Leslie Everman</td>
<td>CCC</td>
<td>15,761</td>
</tr>
<tr>
<td>Munyanduri Tendai Peter</td>
<td>DOP</td>
<td>60</td>
</tr>
<tr>
<td>Mutodi Nyasha Blessing Silence</td>
<td>Z/C/P/D</td>
<td>85</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Makonde" data-content-type="roundMarkers" data-content-index="173" class="igm-map-content" id="makonde_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Makonde</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Nyakata Christopher</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Tigere Noel</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Ziyambi Simbarashe</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mhangura" data-content-type="roundMarkers" data-content-index="174" class="igm-map-content" id="mhangura_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mhangura</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mombeshora Douglas Tendai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Zungura David</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mhondoro-Ngezi" data-content-type="roundMarkers" data-content-index="175" class="igm-map-content" id="mhondoro-ngezi_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mhondoro-Ngezi</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mukuhlani Tavengwa</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Netanyau Innocent</td>
<td>DOP</td>
<td>0</td>
</tr>
<tr>
<td>Tapera Simon</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Muzvezve" data-content-type="roundMarkers" data-content-index="176" class="igm-map-content" id="muzvezve_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Muzvezve</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Haritatos Vangelis Peter</td>
<td>ZANU-PF</td>
<td>16,754</td>
</tr>
<tr>
<td>Marufu Nicholas Anyway</td>
<td>CCC</td>
<td>6,425</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chakari" data-content-type="roundMarkers" data-content-index="177" class="igm-map-content" id="chakari_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chakari</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Nkani Andrew</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Tembo Solomon Isaac</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Kadoma Central" data-content-type="roundMarkers" data-content-index="178" class="igm-map-content" id="kadomacentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Kadoma Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Daka Cosmas</td>
<td>ZANU PF</td>
<td>7,956</td>
</tr>
<tr>
<td>Hamamuti Dzikamai</td>
<td>MDC-T</td>
<td>476</td>
</tr>
<tr>
<td>Mambipiri Gift</td>
<td>CCC</td>
<td>14,940</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Sanyati" data-content-type="roundMarkers" data-content-index="179" class="igm-map-content" id="sanyati_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Sanyati</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chabuka Simangaliso</td>
<td>INDEPENDENT</td>
<td>406</td>
</tr>
<tr>
<td>Kambamura Polite</td>
<td>ZANU PF</td>
<td>17,474</td>
</tr>
<tr>
<td>Mafa Lahliwe</td>
<td>CCC</td>
<td>4,843</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvimba East" data-content-type="roundMarkers" data-content-index="180" class="igm-map-content" id="zvimbaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvimba East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mukwangwariwa Francis Garikai</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Mutasa Oliver</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvimba West" data-content-type="roundMarkers" data-content-index="181" class="igm-map-content" id="zvimbawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvimba West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dinha Mercy Maruva</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Kurwa Brighton Chikaka</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Tanyanyiwa Mekia</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvimba South" data-content-type="roundMarkers" data-content-index="182" class="igm-map-content" id="zvimbasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvimba South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidakwa Walter Kufakunesu</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
<tr>
<td>Malinganiso Taurai Dexter</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Shayamano Nelson</td>
<td>CCC</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zvimba North" data-content-type="roundMarkers" data-content-index="183" class="igm-map-content" id="zvimbanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zvimba North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chombo Marian</td>
<td>ZANU-PF</td>
<td>20,616</td>
</tr>
<tr>
<td>Jenami Willard</td>
<td>CCC</td>
<td>5,382</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bikita East" data-content-type="roundMarkers" data-content-index="184" class="igm-map-content" id="bikitaeast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Bikita East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mudzingwa Bornface</td>
<td>CCC</td>
<td>7,544</td>
</tr>
<tr>
<td>Zevezayi Court</td>
<td>ZANU-PF</td>
<td>9,880</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bikita South" data-content-type="roundMarkers" data-content-index="185" class="igm-map-content" id="bikitasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Bikita South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mutodi Energy</td>
<td>ZANU-PF</td>
<td>11,396</td>
</tr>
<tr>
<td>Nyika Barney</td>
<td>CCC</td>
<td>6,622</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Bikita West" data-content-type="roundMarkers" data-content-index="186" class="igm-map-content" id="bikitawest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Bikita West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chivasa Madock Tatirai</td>
<td>NCA</td>
<td>774</td>
</tr>
<tr>
<td>Gutuza Pikirai</td>
<td>CCC</td>
<td>7,775</td>
</tr>
<tr>
<td>Nhatiso Daniel</td>
<td>ZANU PF</td>
<td>11,614</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiredzi Central" data-content-type="roundMarkers" data-content-index="187" class="igm-map-content" id="chiredzicentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chiredzi Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Hwende Gibson</td>
<td>INDEPENDENT</td>
<td>676</td>
</tr>
<tr>
<td>Makumire Ropafadzo</td>
<td>CCC</td>
<td>12,342</td>
</tr>
<tr>
<td>Moyo Francis</td>
<td>ZANU-PF</td>
<td>7,832</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiredzi East" data-content-type="roundMarkers" data-content-index="188" class="igm-map-content" id="chiredzieast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chiredzi East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maluleke Godfrey</td>
<td>CCC</td>
<td>3,922</td>
</tr>
<tr>
<td>Mundungehama Siyaki</td>
<td>ZANU-PF</td>
<td>14,265</td>
</tr>
<tr>
<td>Vhurande Mahlupeko</td>
<td>NCA</td>
<td>262</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiredzi North" data-content-type="roundMarkers" data-content-index="189" class="igm-map-content" id="chiredzinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chiredzi North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bhila Roy</td>
<td>ZANU-PF</td>
<td>18,696</td>
</tr>
<tr>
<td>Chamisa Fungai</td>
<td>CCC</td>
<td>2,584</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiredzi South" data-content-type="roundMarkers" data-content-index="190" class="igm-map-content" id="chiredzisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chiredzi South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gumbo Douglas</td>
<td>CCC</td>
<td>7,528</td>
</tr>
<tr>
<td>Sithole Joel</td>
<td>ZANU-PF</td>
<td>11,552</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chiredzi West" data-content-type="roundMarkers" data-content-index="191" class="igm-map-content" id="chiredziwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chiredzi West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chiwa Darlington</td>
<td>ZANU-PF</td>
<td>15,054</td>
</tr>
<tr>
<td>Machigere Nhamoinesu</td>
<td>CCC</td>
<td>6,554</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chivi Central" data-content-type="roundMarkers" data-content-index="192" class="igm-map-content" id="chivicentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chivi Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Makotose Peter Alexios</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Maoneke Exevia</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chivi North" data-content-type="roundMarkers" data-content-index="193" class="igm-map-content" id="chivinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chivi North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chidaushe Emmanuel</td>
<td>CCC</td>
<td>5,905</td>
</tr>
<tr>
<td>Mukungunugwa Huruva Godfrey</td>
<td>ZANU-PF</td>
<td>11,769</td>
</tr>
<tr>
<td>Mutswunguma Magret</td>
<td>UZA</td>
<td>78</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Chivi South" data-content-type="roundMarkers" data-content-index="194" class="igm-map-content" id="chivisouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Chivi South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chikondere Danisai</td>
<td>CCC</td>
<td>4,617</td>
</tr>
<tr>
<td>Maburutse Saul</td>
<td>ZANU-PF</td>
<td>12,874</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gutu Central" data-content-type="roundMarkers" data-content-index="195" class="igm-map-content" id="gutucentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Gutu Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chitando Wiston</td>
<td>ZANU-PF</td>
<td>13,683</td>
</tr>
<tr>
<td>Takaona Mathew</td>
<td>CCC</td>
<td>6,439</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gutu East" data-content-type="roundMarkers" data-content-index="196" class="igm-map-content" id="gutueast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Gutu East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ganyiwa Benjamin</td>
<td>ZANU-PF</td>
<td>7,569</td>
</tr>
<tr>
<td>Gonese Gift</td>
<td>CCC</td>
<td>4,759</td>
</tr>
<tr>
<td>Vhengere George</td>
<td>INDEPENDENT</td>
<td>4,641</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gutu South" data-content-type="roundMarkers" data-content-index="197" class="igm-map-content" id="gutusouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Gutu South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gobvu Hamandishe</td>
<td>CCC</td>
<td>7,116</td>
</tr>
<tr>
<td>Togarepi Pupurai</td>
<td>ZANU-PF</td>
<td>9,960</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Gutu West" data-content-type="roundMarkers" data-content-index="198" class="igm-map-content" id="gutuwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Gutu West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Morudu Ephraem</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Paradza John</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
<tr>
<td>Rwodzi Mutonhori Christopher</td>
<td>INDEPENDENT</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Masvingo Central" data-content-type="roundMarkers" data-content-index="199" class="igm-map-content" id="masvingocentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Masvingo Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mavhaire Moses Tinashe</td>
<td>CCC</td>
<td>7,350</td>
</tr>
<tr>
<td>Zvobgo Eddison Mudiwa N</td>
<td>ZANU-PF</td>
<td>9,967</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Masvingo North" data-content-type="roundMarkers" data-content-index="200" class="igm-map-content" id="masvingonorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Masvingo North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Madzivire Enock</td>
<td>CCC</td>
<td>9,147</td>
</tr>
<tr>
<td>Mudumi Brian</td>
<td>ZANU-PF</td>
<td>11,467</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Masvingo South" data-content-type="roundMarkers" data-content-index="201" class="igm-map-content" id="masvingosouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Masvingo South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mabvure Knowledge</td>
<td>CCC</td>
<td>5,088</td>
</tr>
<tr>
<td>Mukomberi Tanatsiwa</td>
<td>ZANU-PF</td>
<td>11,467</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Masvingo Urban" data-content-type="roundMarkers" data-content-index="202" class="igm-map-content" id="masvingourban_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Masvingo Urban</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Maboke Collen</td>
<td>INDEPENDENT</td>
<td>1,629</td>
</tr>
<tr>
<td>Mawende Wellington</td>
<td>ZANU-PF</td>
<td>6,513</td>
</tr>
<tr>
<td>Mazarire Bonface</td>
<td>MDC-T</td>
<td>294</td>
</tr>
<tr>
<td>Muneri Muneri Smar</td>
<td>UZA</td>
<td>86</td>
</tr>
<tr>
<td>Mureri Martin</td>
<td>CCC</td>
<td>13,042</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Masvingo West" data-content-type="roundMarkers" data-content-index="203" class="igm-map-content" id="masvingowest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Masvingo West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Gasva Pedzisai</td>
<td>CCC</td>
<td>9,458</td>
</tr>
<tr>
<td>Ruvai Ezira</td>
<td>ZANU-PF</td>
<td>10,472</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mwenezi East" data-content-type="roundMarkers" data-content-index="204" class="igm-map-content" id="mwenezieast_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mwenezi East</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chikomo Sheillah</td>
<td>ZANU-PF</td>
<td>17,234</td>
</tr>
<tr>
<td>Taruona Martin</td>
<td>CCC</td>
<td>1,910</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Mwenezi North" data-content-type="roundMarkers" data-content-index="205" class="igm-map-content" id="mwenezinorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mwenezi North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Makope Master</td>
<td>ZANU-PF</td>
<td>13,945</td>
</tr>
<tr>
<td>Mapfumo Patrick</td>
<td>CCC</td>
<td>3,373</td>
</tr>
</tbody>
</table>
</figure>
</div>
<div data-original-id="Mwenezi West" data-content-type="roundMarkers" data-content-index="206" class="igm-map-content" id="mweneziwest_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Mwenezi West</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chifumuro Brilliant</td>
<td>CCC</td>
<td>1,054</td>
</tr>
<tr>
<td>Moyo Priscilla</td>
<td>ZANU-PF</td>
<td>14,391</td>
</tr>
<tr>
<td>Shumba Tafadzwa Dhererai</td>
<td>INDEPENDENT</td>
<td>6,495</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zaka Central" data-content-type="roundMarkers" data-content-index="207" class="igm-map-content" id="zakacentral_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zaka Central</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Imbayarwo Pete</td>
<td>CCC</td>
<td>0</td>
</tr>
<tr>
<td>Marapira Davis</td>
<td>ZANU-PF</td>
<td>0</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zaka North" data-content-type="roundMarkers" data-content-index="208" class="igm-map-content" id="zakanorth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zaka North</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Murambiwa Ophias</td>
<td>ZANU-PF</td>
<td>12,620</td>
</tr>
<tr>
<td>Zanga Munyaradzi</td>
<td>CCC</td>
<td>7,079</td>
</tr>
</tbody>
</table>
</figure>
</div><div data-original-id="Zaka South" data-content-type="roundMarkers" data-content-index="209" class="igm-map-content" id="zakasouth_34"><figure class="wp-block-table is-style-stripes">
<table>
<tbody>
<tr>
<td><strong>Candidates</strong></td>
<td><strong>Party</strong></td>
<td><strong>Votes</strong></td>
</tr>
<tr>
<td><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>Zaka South</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chiduwa Clemence</td>
<td>ZANU-PF</td>
<td>14,163</td>
</tr>
<tr>
<td>Manjengwah Trust Salpisio</td>
<td>CCC</td>
<td>5,536</td>
</tr>
</tbody>
</table>
</figure>
</div>
</div>
'''


# Parse HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Find all div elements
divs = soup.find_all('div')

# Prepare JSON data
json_data = {}

# Process each div element
for div in divs:
    # Find constituency name
    constituency_name = div['data-original-id']

    # Find table rows containing candidate information
    rows = div.find_all('tr')

    # Initialize variables to store candidate information
    candidates = []

    # Extract candidate information from table rows
    for row in rows:
        # Skip header row
        if not row.find('strong'):

            # Extract candidate, party, and votes
            cells = row.find_all('td')
            candidate = cells[0].text.strip()
            party = cells[1].text.strip()
            vote = cells[2].text.strip().replace(',', '') if cells[2].text.strip() else "0"

            # Add candidate information to the list
            candidates.append({
                'Candidate': candidate,
                'Party': party,
                'Votes': vote
            })

    # Add constituency data to the JSON dictionary
    json_data[constituency_name] = candidates

# Write JSON data to a file
with open('candidate_votes.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
