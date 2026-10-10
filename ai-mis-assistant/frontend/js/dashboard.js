const todayEl = document.getElementById('today');
todayEl.textContent = new Intl.DateTimeFormat(undefined, {
  month: 'short',
  day: 'numeric',
  year: 'numeric'
}).format(new Date());

async function loadDashboard() {
  try {
    const [summary, employees] = await Promise.all([
      api('/reports/summary'),
      api('/employees')
    ]);

    document.getElementById('employees-total').textContent =
      summary.employees;

    document.getElementById('present-total').textContent =
      summary.present_today;

    document.getElementById('attendance-rate').textContent =
      `${summary.attendance_rate}% attendance`;

    document.getElementById('sales-total').textContent =
      money(summary.sales_month);

    document.getElementById('activity-list').innerHTML =
      employees.slice(0, 4).map((person, i) => `
        <div class="activity-item">
          <div class="avatar"
               style="background:${['#e7e2fb','#e1f2ec','#e2eefb','#f8eadb'][i]}">
            ${person.name
              .split(' ')
              .map(n => n[0])
              .slice(0, 2)
              .join('')}
          </div>

          <div class="activity-copy">
            <b>${person.name}</b> is part of ${person.department}
            <small>${person.designation} · ${person.status}</small>
          </div>
        </div>
      `).join('') || '<p>No employees added yet.</p>';

  } catch (error) {
    document.getElementById('activity-list').innerHTML =
      `<div class="error">
        ${error.message}. Start the backend to load live data.
      </div>`;
  }
}

loadDashboard();