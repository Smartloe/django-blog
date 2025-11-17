# Repository Guidelines

## Project Structure & Module Organization
- Core app lives in `blog/` (models, forms, URLs, admin_custom tweaks, management commands). Database migrations sit in `blog/migrations/`.
- Django project settings and root URLs are in `blog_project/`.
- Shared templates are under `templates/`; blog-specific templates live in `blog/templates/blog/`.
- Top-level helpers: `create_sample_data.py` and `demo_admin.py` seed or inspect data; `main.py`/`status_check.py` are quick entry points; SQLite dev DB is `db.sqlite3`.
- Tests are colocated (`blog/tests.py`, `test_login.py`, `test_auth.py`) and run against the standard Django test runner.

## Build, Test, and Development Commands
- Install deps: `uv sync`.
- Migrate database: `uv run python manage.py migrate`.
- Seed demo content: `uv run python manage.py create_sample_data` (custom management command).
- Run dev server: `uv run python manage.py runserver`.
- Run tests: `uv run python manage.py test` (picks up both app and root-level tests).
- Collect static for production: `uv run python manage.py collectstatic`.

## Coding Style & Naming Conventions
- Python 3.12+, follow PEP 8 (4-space indents, `snake_case` for functions/fields, `CapWords` for classes). Keep queries lazy and prefer queryset chaining over raw SQL.
- Django conventions: class-based views or function views live in `blog/views.py`; URL names are lowercase with hyphen-free slugs.
- Templates: use Bootstrap 5 components already present; keep blocks organized with `{% block %}` names matching page purpose (`content`, `extra_head`).
- Keep settings and secrets in env vars (`DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`); do not commit local overrides.

## Testing Guidelines
- Primary runner: `uv run python manage.py test`.
- Add new tests in `blog/tests.py` or module-specific files under `blog/` following `test_*` names. Use Django’s `TestCase` for DB-backed cases.
- Prefer fixtures/factories over hard-coded IDs; reuse the `create_sample_data` command for quick manual verification when appropriate.

## Commit & Pull Request Guidelines
- Recent history uses conventional-style prefixes (`feat:`, etc.); continue that pattern (e.g., `fix: guard empty context in view`).
- Commits should stay scoped: migrations + model changes together; template tweaks separated from data seeding when possible.
- PRs: include a clear summary, test command(s) executed, and screenshots/GIFs for visible UI/admin updates. Link issues when applicable.

## Security & Configuration Tips
- Never commit `SECRET_KEY` or production DB credentials; rely on environment configuration.
- For production, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and run `collectstatic` before deployment.
- Enforce strong admin credentials; the default `admin/admin123` is for demos only—change before exposing the instance.
