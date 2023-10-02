// Main function to fetch and display resident information based on API links
function getResidentsLink(apilinks) {
    const modalContent = document.getElementById('modalcontent');
    if (!modalContent) {
        console.error("modal is missing");
        return;
    }
    modalContent.innerHTML = ""; //reset popup window content
    displayHeaders();
    const links = parseJson(apilinks);
    links.forEach(link => displayResident(link));
}

// JSON parser with regex to handle the non-standard quotation marks due to "limitations" in jinja2
function parseJson(json) {
    try {
        return JSON.parse(json.replace(/'/g, '"'));
    } catch (error) {
        console.error('Failed to parse JSON:', error);
        return [];
    }
}

async function displayResident(link) {
    try {
        const response = await fetch(link);
        const resident = await response.json();
        const residentRow = createResidentRow(resident);
        document.getElementById('modalcontent').appendChild(residentRow);
    } catch (error) {
        console.error('Failed to fetch resident:', error);
    }
}

function displayHeaders() {
    const headers = [
        'Name', 'Height', 'Mass', 'Hair color', 'Skin color', 'Eye color', 'Birth year', 'Gender'
    ];
    const headerHTML = headers.map(header =>
        `<div class="col p-3 mb-2 bg-light text-dark border text-center">
            <b>${header}</b>
        </div>`
    ).join('');
    document.getElementById('modalcontent').innerHTML = `<div class="row height">${headerHTML}</div>`;
}

function createResidentRow(resident) {
    const row = document.createElement('div');
    row.classList.add('row');

    const attributes = [
        resident.name, resident.height, resident.mass, resident.hair_color,
        resident.skin_color, resident.eye_color, resident.birth_year, resident.gender
    ];

    attributes.forEach(attribute => {
        const column = createColumnWithSpan(attribute);
        row.appendChild(column);
    });

    return row;
}

function createColumnWithSpan(content) {
    const col = document.createElement('div');
    col.classList.add('col', 'bg-light', 'text-dark', 'border');

    const span = document.createElement('span');
    span.style.display = 'inline-block';
    span.style.textAlign = 'center';
    span.textContent = content;

    col.appendChild(span);
    return col;
}
