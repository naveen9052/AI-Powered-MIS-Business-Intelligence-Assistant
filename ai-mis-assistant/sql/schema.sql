CREATE TABLE IF NOT EXISTS departments (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS employees (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL CHECK (length(trim(name)) BETWEEN 1 AND 120),
    email TEXT NOT NULL CHECK (position('@' IN email) > 1),
    department_id BIGINT NOT NULL REFERENCES departments(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    role TEXT NOT NULL CHECK (length(trim(role)) BETWEEN 1 AND 100),
    status TEXT NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive')),
    hired_on DATE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_employees_email_ci ON employees (lower(email));

CREATE TABLE IF NOT EXISTS attendance (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id BIGINT NOT NULL REFERENCES employees(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    attendance_date DATE NOT NULL,
    check_in TIME,
    check_out TIME,
    status TEXT NOT NULL DEFAULT 'Present' CHECK (status IN ('Present', 'Absent', 'Leave', 'Remote')),
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (employee_id, attendance_date),
    CHECK (check_in IS NULL OR check_out IS NULL OR check_out >= check_in)
);

CREATE TABLE IF NOT EXISTS sales (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sale_date DATE NOT NULL,
    department_id BIGINT NOT NULL REFERENCES departments(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    employee_id BIGINT REFERENCES employees(id) ON UPDATE CASCADE ON DELETE SET NULL,
    amount_cents BIGINT NOT NULL CHECK (amount_cents >= 0),
    currency CHAR(3) NOT NULL DEFAULT 'USD',
    description TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_employees_department_status ON employees(department_id, status);
CREATE INDEX IF NOT EXISTS idx_attendance_date_status ON attendance(attendance_date, status);
CREATE INDEX IF NOT EXISTS idx_attendance_employee_date ON attendance(employee_id, attendance_date);
CREATE INDEX IF NOT EXISTS idx_sales_date_department ON sales(sale_date, department_id);
