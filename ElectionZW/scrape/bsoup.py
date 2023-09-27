import csv
from bs4 import BeautifulSoup
# HTML code with multiple divs
html_code = '''
<div data-original-id="Bulawayo North" data-content-type="roundMarkers" data-content-index="1" class="igm-map-content" id="bulawayonorth_34">
    <figure class="wp-block-table is-style-stripes">
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
                    <td>182</td>
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
                <tr>
                    <td>Moyo Nkosi</td>
                    <td>MDC</td>
                    <td>500</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Ncube Thandiwe</td>
                    <td>Independent</td>
                    <td>150</td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </figure>
</div>

<div data-original-id="Harare South" data-content-type="roundMarkers" data-content-index="2" class="igm-map-content" id="hararesouth_35">
    <figure class="wp-block-table is-style-stripes">
        <table>
            <tbody>
                <tr>
                    <td><strong>Candidates</strong></td>
                    <td><strong>Party</strong></td>
                    <td><strong>Votes</strong></td>
                    <td><strong>%</strong></td>
                </tr>
                <tr>
                    <td><strong>Harare South</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Mhlanga Tendai</td>
                    <td>ZANU PF</td>
                    <td>3,500</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Moyo Lovemore</td>
                    <td>MDC</td>
                    <td>2,800</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Ngwenya Sibusisiwe</td>
                    <td>CCC</td>
                    <td>4,200</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Nkomo Nkosana</td>
                    <td>DOP</td>
                    <td></td>
                    <td>300</td>
                </tr>
                <tr>
                    <td>Sibanda Thembani</td>
                    <td>Independent</td>
                    <td>250</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Tshuma Sipho</td>
                    <td>UZA</td>
                    <td>400</td>
                    g<td></td>
                </tr>
            </tbody>
        </table>
    </figure>
</div>
'''


# Parse HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Find all div elements
divs = soup.find_all('div')

# Prepare CSV data
header = ['Constituency', 'CCC', 'ZANU PF', 'DOP', 'UZA', 'MDC', 'Independent', 'Others', 'Total']
csv_data = [header]

# Process each div element
for div in divs:
    # Find constituency name
    constituency_name = div['data-original-id']

    # Find table rows containing candidate information
    rows = div.find_all('tr')

    # Initialize variables to store candidate information
    candidates = []
    parties = []
    votes = []

    # Extract candidate information from table rows
    for row in rows:
        # Skip header row
        if row.find('strong'):
            continue

        # Extract candidate, party, and votes
        cells = row.find_all('td')
        candidate = cells[0].text.strip()
        party = cells[1].text.strip()
        vote = cells[2].text.strip().replace(',', '') if cells[2].text.strip() else "0"

        # Add candidate information to respective lists
        candidates.append(candidate)
        parties.append(party)
        votes.append(vote)

    # Calculate total votes
    total_votes = sum(int(vote) for vote in votes)

    # Create a list with candidate votes in the same order as the header
    candidate_votes = []
    for party in header[1:-1]:
        if party in parties:
            index = parties.index(party)
            candidate_votes.append(votes[index])
        else:
            candidate_votes.append("0")

    # Append the total votes at the end of the list
    candidate_votes.append(str(total_votes))

    # Create a CSV row with constituency, candidate votes, and total votes
    csv_row = [constituency_name] + candidate_votes
    csv_data.append(csv_row)

# Write CSV data to a file
with open('candidate_votes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)