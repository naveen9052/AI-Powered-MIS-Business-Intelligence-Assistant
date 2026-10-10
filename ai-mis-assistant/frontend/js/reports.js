async function loadReport() {
  try {
    const [summary, departments] = await Promise.all([api('/reports/summary'), api('/reports/sales-by-department')]);
    document.getElementById('report-employees').textContent = summary.employees;
    document.getElementById('report-present').textContent = summary.present_today;
    document.getElementById('report-rate').textContent = `${summary.attendance_rate}% attendance rate`;
    document.getElementById('report-sales').textContent = money(summary.sales_month);
    document.getElementById('report-month').textContent = new Date().toLocaleString(undefined, { month: 'long', year: 'numeric' });
    const max = Math.max(...departments.map(d => d.amount), 1);
    document.getElementById('sales-breakdown').innerHTML = departments.map(d => `<div class="bar-row"><span style="width:95px">${d.department}</span><div class="bar-track"><div class="bar-fill" style="width:${Math.max(2, d.amount / max * 100)}%"></div></div><b>${money(d.amount)}</b></div>`).join('') || '<p style="margin-top:18px">No sales recorded.</p>';
  } catch (error) { document.getElementById('sales-breakdown').innerHTML = `<div class="error">${error.message}. Start the backend to load live data.</div>`; }
}
loadReport();
