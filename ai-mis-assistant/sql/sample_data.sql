INSERT INTO departments(name, slug) VALUES
    ('Sales', 'sales'), ('People', 'people'), ('Operations', 'operations'), ('Partnerships', 'partnerships')
ON CONFLICT(name) DO NOTHING;

INSERT INTO employees(name, email, department_id, role) VALUES
    ('Aarav Mehta', 'aarav.mehta@example.com', (SELECT id FROM departments WHERE slug='sales'), 'Account Executive'),
    ('Maya Iyer', 'maya.iyer@example.com', (SELECT id FROM departments WHERE slug='people'), 'HR Manager'),
    ('Kabir Shah', 'kabir.shah@example.com', (SELECT id FROM departments WHERE slug='operations'), 'Operations Analyst')
ON CONFLICT DO NOTHING;

INSERT INTO attendance(employee_id, attendance_date, check_in, check_out, status) VALUES
    ((SELECT id FROM employees WHERE email='aarav.mehta@example.com'), CURRENT_DATE, '09:02', '17:31', 'Present'),
    ((SELECT id FROM employees WHERE email='maya.iyer@example.com'), CURRENT_DATE, '09:12', '17:04', 'Remote'),
    ((SELECT id FROM employees WHERE email='kabir.shah@example.com'), CURRENT_DATE, NULL, NULL, 'Leave')
ON CONFLICT(employee_id, attendance_date) DO NOTHING;

INSERT INTO sales(sale_date, department_id, amount_cents, description) VALUES
    (CURRENT_DATE, (SELECT id FROM departments WHERE slug='sales'), 1840000, 'Enterprise renewals'),
    (CURRENT_DATE, (SELECT id FROM departments WHERE slug='sales'), 1275000, 'New business'),
    (CURRENT_DATE, (SELECT id FROM departments WHERE slug='partnerships'), 960000, 'Partner referral');
