import re

data = [{"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bajila Collins Discent", "candidate": "CCC", "party": "0"}, {"constituency": "Ndlovu Khulumani", "candidate": "ZANC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bizaliel Kennedy", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Mupundu Simbarashe", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chigumbu Darlington Dzikamai", "candidate": "CCC", "party": "17,348"}, {"constituency": "Mukweya Tatenda", "candidate": "ZANU-PF", "party": "3,703"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chitoro Nyashadzashe Enock", "candidate": "CCC", "party": "0"}, {"constituency": "Sithole Godfrey Karakadzayi", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dzvene Elvis", "candidate": "UZA", "party": "0"}, {"constituency": "Mafuratidze Goodwell", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chikomo Traswell", "candidate": "CCC", "party": "16,004"}, {"constituency": "Nyikadzino Tichaona", "candidate": "CCC", "party": "2,459"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chamatowa Lovemore", "candidate": "ZANU-PF", "party": "9,227"}, {"constituency": "Mushoriwa Edwin", "candidate": "CCC", "party": "16,453"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidewu Njodzi", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Mhetu Togarepi Zivai", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bande Didymus", "candidate": "CCC", "party": "1,867"}, {"constituency": "Chatambudza Kudakwashe Blessed", "candidate": "CCC", "party": "6,745"}, {"constituency": "Taedzwa Honour Mbofana", "candidate": "ZANU-PF", "party": "8,112"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chikombo Wellington", "candidate": "CCC", "party": "17,009"}, {"constituency": "Mupindu Muchineripi", "candidate": "ZANU-PF", "party": "4,261"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidziva Happymore", "candidate": "CCC", "party": "0"}, {"constituency": "Mangachena Musekiwa", "candidate": "FREE ZIM CONGRESS", "party": "0"}, {"constituency": "Zamanga Witness Tumelo", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chinyadza Justice", "candidate": "UZA", "party": "0"}, {"constituency": "Muchuwe Offard", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jimu Lovemore", "candidate": "CCC", "party": "0"}, {"constituency": "Zenda Nyasha Gift", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gumbo Mavis", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Mlambo Garikai", "candidate": "UZA", "party": "0"}, {"constituency": "Razaru Malvin", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hasha Trouble", 
"candidate": "CCC", "party": "4,009"}, {"constituency": "Magweta George", "candidate": "CCC", "party": "1,573"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mamombe Joanah", "candidate": "CCC", "party": "18,141"}, {"constituency": "Zindoga Patrick Tendayi", "candidate": "ZANU-PF", "party": "3,453"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gumbo Agency", "candidate": "CCC", "party": "0"}, {"constituency": "Mashongandoro Modock", "candidate": "DUZ", "party": "0"}, {"constituency": "Sande Lloyd", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chapinduka Clara", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Nyamakanga Paidamoyo", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mashonganyika Mike", "candidate": "ZANU-PF", "party": "3,789"}, {"constituency": "Mukunguma Luckson", "candidate": "MDC-T", "party": "248"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Baudi Pattence", "candidate": "UZA", "party": "0"}, {"constituency": "Khumbula Terrence", "candidate": "CCC", "party": "0"}, {"constituency": 
"Mnangagwa Tongai Mafidi", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": 
"Votes</strong>"}, {"constituency": "Hwende Chalton", "candidate": "CCC", "party": "0"}, {"constituency": "Majavhura Tellme", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Takawira Collen Munyaradzi", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chimbalanga Jossam", "candidate": "INDEPENDENT", "party": "272"}, 
{"constituency": "Mauka Tauya", "candidate": "ZANU-PF", "party": "5,251"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", 
"party": "Votes</strong>"}, {"constituency": "Kufahakutizwi Munyaradzi Febion", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chamisa Starman", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gwasira Beadle Musatye", "candidate": "ZANU-PF", "party": "7,787"}, {"constituency": "Mahere Fadzayi", "candidate": "CCC", "party": "12,865"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kunaka Jim", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Nyemba Maureen", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jinjika Norbet", "candidate": "ZANU-PF", "party": "77,28"}, {"constituency": "Mazhindu Brighton", "candidate": "CCC", "party": "11,094"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Goremusandu Christmas", "candidate": "CCC", "party": "2,762"}, {"constituency": "Magweba Loice", "candidate": "ZANU-PF", "party": "6,236"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidawa Tafadzwa", "candidate": "ZANU PF", "party": "0"}, {"constituency": "July Antony", "candidate": "UZA", "party": "0"}, {"constituency": "Matika Energy Tanaka", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chimbaira Goodrich", "candidate": "CCC", "party": "0"}, {"constituency": "Mutimbanyoka Kiven", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidakwa Simon", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kandenga Timothy", "candidate": "CCC", "party": "5,276"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Guyo Phillip", "candidate": "ZANU PF", "party": "12,258"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hodhera Solomon", "candidate": "CCC", "party": "7,912"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mangwanya Herbert", "candidate": "CCC", "party": "6,967"}, {"constituency": "Tsvangirai Komborero", "candidate": "MDC-T", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Charamba Garikayi", "candidate": "NCA", "party": "59"}, {"constituency": "Karenyi Lynette", "candidate": "CCC", "party": "14,237"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dube Innocent", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": 
"Maposa Wilson", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Mushango Isaiah", "candidate": "NCA", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dhlumo Livingstone", "candidate": "CCC", "party": "11,148"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dhliwayo Lincoln", "candidate": "ZANU-PF", "party": "12,186"}, {"constituency": "Mupaji Samuel", "candidate": "NCA", "party": "213"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hlatywayo Clifford", "candidate": "CCC", "party": "11,039"}, {"constituency": "Mlambo Ronald", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Porusungazi Enock", "candidate": "ZANU-PF", "party": "8,090"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jani Clide", 
"candidate": "ZANU PF", "party": "6,343"}, {"constituency": "Mwandunguza Lameck Mark", "candidate": "NCA", "party": "221"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mapfumo Farai Walter", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Lastone Julius", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Nyika Shepherd", "candidate": "ZANU-PF", "party": "8,503"}, {"constituency": "Tekeshe \r\nDavid", "candidate": "MDC-T", "party": "1,760"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chitena Shepherd", "candidate": "CCC", "party": "6,257"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chenai Danmore Tinashe", "candidate": "CCC", "party": "0"}, {"constituency": "Nyakuedzwa Albert", "candidate": "ZANU-PF", "party": ""}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gonye Prince", "candidate": "INDEPENDENT", "party": "549"}, {"constituency": "Muswere Jenfan", "candidate": "ZANU-PF", "party": "10,863"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "James Leslie Brian", "candidate": "CCC", "party": "15,628"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mahachi Admire", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dumbarimwe Tawanda", "candidate": "ZANU-PF", "party": "12,886"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Marange Nyasha", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Nemasasi Prayer", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Benza Innocent Dambudzo", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bvute Obey", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mugadza Misheck", "candidate": "ZANU-PF", "party": "11,608"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chauke Alexander", "candidate": "DUZ", "party": "354"}, {"constituency": "Mudzamiri Thomas", "candidate": "NCA", "party": "269"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chifodya Nyahando", "candidate": "CCC", "party": "8,540"}, {"constituency": "Mwonzora Munyaradzi", "candidate": "MDC-T", "party": "735"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Madziwa Tonderai Joseph", "candidate": "MDC-T", "party": "619"}, {"constituency": "Mccormick Ruxandra Grigoreta", "candidate": "CCC", "party": "9,574"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kajokoto Zvidzai Ruzvidzo", "candidate": "CCC", "party": "0"}, {"constituency": "Musanhi Kenneth Shupikai", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gwarada George", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Pinduka Tendai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Basa Shupiko", "candidate": "CCC", "party": "0"}, {"constituency": "Svembere Dominic", "candidate": "NPC-UBUNTU", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mushonga Shepherd Lenard", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, 
{"constituency": "Makumbe Tsungai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", 
"party": "Votes</strong>"}, {"constituency": "Chari Rangarirai", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kazembe Kazembe", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Butau David", "candidate": "ZANU-PF", "party": 
"0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Butau Dzidzai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mapundu Vengai", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gura Reason", "candidate": "CCC", "party": "0"}, {"constituency": "Tsenengamu Godfrey", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jonga Witness", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Utete Mativenga", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kagura Agreement Takawira", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gweru Wellington", "candidate": "CCC", "party": "1,984"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mutero Cuthbert", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chinodakufa Isac", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mapiki Joseph", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Cheza Patrick", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chokururama Jacob", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gumbo Joseph", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Ndhlukulani Jeremiah", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chabata Misheck", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Tshuma Givemore", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bangure \r\nDonwell", "candidate": "CCC", "party": "0"}, {"constituency": "Muswere Ndemera", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chitiyo Richard", "candidate": "ZAPU", "party": "408"}, {"constituency": "Mears Spencer Valentine", "candidate": "INDEPENDENT", "party": "185"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Ncube Owen", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Karikoga Tawanda", "candidate": "ZANU PF", "party": "0"}, 
{"constituency": "Zhiva Rueben", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mavima Paul", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Matiza Madron", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kwidini Sleiman Timios", "candidate": "ZANU PF", 
"party": "10,890"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chadoka Albert", "candidate": "MDC-T", "party": "0"}, {"constituency": "Magura Wellington", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Antonio Learmore", "candidate": "FREEZIM CONGRESS", "party": "68"}, {"constituency": "Gondo William", "candidate": "ZANU PF", "party": "4,906"}, {"constituency": "Mkandhla Tadios", "candidate": "UZA", "party": "56"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mgiyelwa Innocent", "candidate": "DOP", "party": "0"}, {"constituency": "Ndlovu Brown", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Manwere Dereck", "candidate": "UZA", "party": "113"}, {"constituency": "Ndlovu Mbekezeli", "candidate": "MDC-T", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Madzivanyika Corban", "candidate": "CCC", "party": "0"}, {"constituency": "Mupereri Vongaishe", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kasiriwori Unique", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Moyo July", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jona Nyevera", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Ndebele Ephraim Makhele", "candidate": "ZAPU", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Ntini Benison Judah", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Shumba Tinashe", "candidate": "ZANU PF", "party": "17,689"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hungwe Tasara", "candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Msipa Dambudzo", "candidate": "FREEZIM CONGRESS", "party": "559"}, {"constituency": "Zhou Tafanana", "candidate": "ZANU PF", "party": "13,795"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mhindu Phillip", "candidate": "CCC", "party": "9,094"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mhlanga Michael", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jaravaza Mecky", "candidate": "ZANU PF", "party": "12,124"}, {"constituency": "Nyoni Michael", "candidate": "INDEPENDENT", 
"party": "165"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Moyo Fred", 
"candidate": "ZANU PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hadebe Jabulani", "candidate": "CCC", "party": "6,269"}, {"constituency": "Moyo Clilopasi", "candidate": "ZAPU", "party": "576"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mhona Felix Tapiwa", "candidate": "ZANU PF", "party": "12,089"}, {"constituency": "Chinembiri Muchengeti", "candidate": "CCC", "party": "6,202"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mavetera Tatenda Annastacia", "candidate": "ZANU PF", "party": "19,620"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bvute Ozias", "candidate": "ZANU PF", "party": "14,546"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chagwiza Stephen", "candidate": "CCC", "party": "16,312"}, {"constituency": "Chikudo Rueben", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Karimatsenga Nyamupinga Biatah<br />Beatrice", "candidate": "ZANU-PF", "party": "12,072"}, {"constituency": "Nhamburo Taurai Clifford", "candidate": "INDEPENDENT", "party": "2,139"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gwanzura Oswell Ndumo", "candidate": "ZANU-PF", "party": "9,373"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, 
{"constituency": "Kundiona Cleopas", "candidate": "ZANU-PF", "party": "9,714"}, {"constituency": "Matewu Caston", "candidate": "CCC", "party": "14,712"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mutokonyi Vimbayi", "candidate": "ZANU-PF", "party": "15,221"}, {"constituency": "Zhuwarara Kizito", "candidate": "CCC", "party": "3,566"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Magwenzi Eddington", "candidate": "CCC", "party": "11,106"}, {"constituency": "Munhunepi Tichaona", "candidate": "INDEPENDENT", "party": "483"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Musweweshiri Benjamin", "candidate": "ZANU-PF", "party": "15,099"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Nyambo Tichafa", "candidate": "CCC", "party": "2,376"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kaitano Knowledge", 
"candidate": "ZANU-PF", "party": "18,513"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Garwe Daniel", "candidate": "ZANU-PF", "party": "14,870"}, {"constituency": "Mangwende Eunice Tambudzai", "candidate": "INDEPENDENT", "party": "1,323"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bume Timothy", "candidate": "CCC", "party": "2,902"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, 
{"constituency": "Jere Farai", "candidate": "ZANU-PF", "party": "17,733"}, {"constituency": "Nhamburo Silence", "candidate": "INDEPENDENT", "party": "114"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kaseke Yeukai", "candidate": "CCC", "party": "3,613"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Makwiranzou Caleb", "candidate": "ZANU-PF", "party": "16,132"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mapengo Mapango", "candidate": "CCC", "party": "4,296"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kashambe Munyaradzi Tobias", "candidate": "ZANU PF", "party": "13,277"}, {"constituency": "Muzanenhamo Frederick", "candidate": "DUZ", "party": "235"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chimunhu Chiratidzo", "candidate": "CCC", "party": "1,448"}, {"constituency": "Mupukuta Ndinyarei", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Konono Cosmas", "candidate": "CCC", "party": "1,977"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Fidelis Eunice", "candidate": "ZNRP", "party": "664"}, {"constituency": "Ndudzo Itai", "candidate": "ZANU-PF", "party": "18,762"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Machakarika Tinoda", "candidate": "ZANU-PF", "party": "12,563"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mandere Gabriel", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chigavazira Last Farai", "candidate": "ZANU-PF", "party": "11,308"}, {"constituency": "Konjana Gift Machoka", "candidate": "INDEPENDENT", "party": "875"}, {"constituency": "Matibe Takalani Prince", "candidate": "INDEPENDENT", "party": "320"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mubaira Jonathan", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Chiwanza Rodrick Chamunorwa A", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mliswa Temba Peter", "candidate": "INDEPENDENT", "party": "7,518"}, {"constituency": "Tsvangirayi Richard", "candidate": "CCC", "party": "13,089"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mazhambe Joel", "candidate": "FREEZIM", "party": "0"}, {"constituency": "Ziki Richard", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kangausaru Chenjerai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mangwaira Stanford", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Kambuzuma Chinjai", "candidate": "ZANU-PF", "party": "0"}, 
{"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Jasi Gabriel", "candidate": "INDEPENDENT", "party": "453"}, {"constituency": "Monga Super", "candidate": "ZANU-PF", "party": "10,121"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chiweshe Doras", "candidate": "FREEZIM", "party": "0"}, {"constituency": "Mugadza Patrick Phillip", "candidate": "DOP", "party": "0"}, {"constituency": "Shamu Tichaona Nigeil", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidzomba Thomas", "candidate": "ZANU PF", "party": "10,051"}, {"constituency": "Munyanduri Tendai Peter", "candidate": "DOP", "party": "60"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Nyakata Christopher", "candidate": "INDEPENDENT", "party": 
"0"}, {"constituency": "Ziyambi Simbarashe", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mombeshora Douglas Tendai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mukuhlani Tavengwa", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Tapera Simon", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", 
"party": "Votes</strong>"}, {"constituency": "Haritatos Vangelis Peter", "candidate": "ZANU-PF", "party": "16,754"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Nkani Andrew", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Daka Cosmas", "candidate": "ZANU \r\nPF", "party": "7,956"}, {"constituency": "Mambipiri Gift", "candidate": "CCC", "party": "14,940"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chabuka Simangaliso", "candidate": "INDEPENDENT", "party": "406"}, {"constituency": "Mafa Lahliwe", "candidate": "CCC", "party": "4,843"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mukwangwariwa Francis Garikai", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Dinha Mercy Maruva", "candidate": "ZANU-PF", "party": "0"}, {"constituency": "Tanyanyiwa Mekia", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidakwa Walter Kufakunesu", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Shayamano Nelson", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chombo Marian", "candidate": "ZANU-PF", "party": "20,616"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mudzingwa Bornface", "candidate": "CCC", "party": "7,544"}, {"constituency": "Candidates</strong>", "candidate": 
"Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mutodi Energy", "candidate": "ZANU-PF", "party": "11,396"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chivasa Madock Tatirai", "candidate": "NCA", "party": "774"}, {"constituency": "Nhatiso Daniel", "candidate": "ZANU PF", "party": "11,614"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Hwende Gibson", "candidate": "INDEPENDENT", "party": "676"}, {"constituency": "Moyo Francis", "candidate": "ZANU-PF", "party": "7,832"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Maluleke Godfrey", "candidate": "CCC", "party": "3,922"}, {"constituency": "Vhurande Mahlupeko", "candidate": "NCA", "party": "262"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Bhila Roy", "candidate": "ZANU-PF", "party": "18,696"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gumbo Douglas", "candidate": "CCC", "party": "7,528"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chiwa Darlington", "candidate": "ZANU-PF", "party": "15,054"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Makotose Peter Alexios", "candidate": "CCC", "party": "0"}, {"constituency": 
"Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chidaushe Emmanuel", "candidate": "CCC", "party": "5,905"}, {"constituency": "Mutswunguma Magret", "candidate": "UZA", "party": "78"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chikondere Danisai", "candidate": "CCC", "party": "4,617"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chitando Wiston", "candidate": "ZANU-PF", "party": "13,683"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Ganyiwa Benjamin", "candidate": "ZANU-PF", "party": "7,569"}, {"constituency": "Vhengere George", "candidate": "INDEPENDENT", "party": "4,641"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gobvu Hamandishe", "candidate": "CCC", "party": "7,116"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Morudu Ephraem", "candidate": "CCC", "party": "0"}, {"constituency": "Rwodzi Mutonhori Christopher", "candidate": "INDEPENDENT", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mavhaire Moses Tinashe", "candidate": "CCC", "party": 
"7,350"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Madzivire Enock", "candidate": "CCC", "party": "9,147"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Mabvure Knowledge", "candidate": "CCC", "party": "5,088"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Maboke Collen", "candidate": "INDEPENDENT", "party": "1,629"}, {"constituency": "Mazarire Bonface", "candidate": "MDC-T", "party": "294"}, {"constituency": "Mureri Martin", "candidate": "CCC", "party": "13,042"}, {"constituency": "Candidates</strong>", 
"candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Gasva Pedzisai", "candidate": "CCC", "party": "9,458"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chikomo Sheillah", "candidate": "ZANU-PF", "party": "17,234"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Makope Master", "candidate": "ZANU-PF", "party": "13,945"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chifumuro Brilliant", "candidate": "CCC", "party": "1,054"}, {"constituency": "Shumba Tafadzwa Dhererai", "candidate": "INDEPENDENT", "party": "6,495"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": 
"Imbayarwo Pete", "candidate": "CCC", "party": "0"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Murambiwa Ophias", "candidate": "ZANU-PF", "party": "12,620"}, {"constituency": "Candidates</strong>", "candidate": "Party</strong>", "party": "Votes</strong>"}, {"constituency": "Chiduwa Clemence", "candidate": "ZANU-PF", "party": "14,163"}]
  
def clean_data(data):
   for row in data:
    row["candidate"] = re.sub(r"<strong>Candidates</strong>", "", row["candidate"])
    row["party"] = re.sub(r"<strong>Party</strong>", "", row["party"])

    return data
