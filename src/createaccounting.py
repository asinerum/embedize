from .dcore import uuid_value, sql_uni_replace, duck_replaces

function_select_uuid = f'''
SELECT {uuid_value()} AS uuid
'''

create_zone_roles = f'''
CREATE TABLE IF NOT EXISTS roles (
id INTEGER PRIMARY KEY NOT NULL,
name VARCHAR DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
active BOOLEAN DEFAULT TRUE
)'''

create_zone_specs = f'''
CREATE TABLE IF NOT EXISTS specs (
id INTEGER PRIMARY KEY NOT NULL,
name VARCHAR DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
active BOOLEAN DEFAULT TRUE
)'''

##CanDelete
create_zone_specroles = f'''
CREATE TABLE IF NOT EXISTS specroles (
spec INTEGER NOT NULL REFERENCES specs (id),
role INTEGER NOT NULL REFERENCES roles (id),
CONSTRAINT pk_specrole PRIMARY KEY (spec, role)
)'''

##CanDelete
create_zone_userspecs = f'''
CREATE TABLE IF NOT EXISTS userspecs (
user INTEGER NOT NULL,
spec INTEGER NOT NULL REFERENCES specs (id),
CONSTRAINT pk_userspec PRIMARY KEY (user, spec)
)'''

##CanDelete
create_zone_userroles = f'''
CREATE TABLE IF NOT EXISTS userroles (
user INTEGER NOT NULL,
role INTEGER NOT NULL REFERENCES roles (id),
CONSTRAINT pk_userrole PRIMARY KEY (user, role)
)'''

create_zone_groups = f'''
CREATE TABLE IF NOT EXISTS groups (
id INTEGER PRIMARY KEY NOT NULL,
code VARCHAR UNIQUE NOT NULL,
name VARCHAR DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
active BOOLEAN DEFAULT TRUE,
CHECK (code=UPPER(TRIM(code)))
)'''

create_zone_roots = f'''
CREATE TABLE IF NOT EXISTS roots (
id INTEGER PRIMARY KEY NOT NULL,
grup INTEGER NOT NULL REFERENCES groups (id),
code VARCHAR UNIQUE NOT NULL,
name VARCHAR DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
active BOOLEAN DEFAULT TRUE,
CHECK (code=UPPER(TRIM(code)))
)'''

create_zone_accounts = f'''
CREATE TABLE IF NOT EXISTS accounts (
id INTEGER PRIMARY KEY NOT NULL,
root INTEGER NOT NULL REFERENCES roots (id),
code VARCHAR UNIQUE NOT NULL,
name VARCHAR DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
active BOOLEAN DEFAULT TRUE,
CHECK (code=UPPER(TRIM(code)))
)'''

create_zone_subs = f'''
CREATE TABLE IF NOT EXISTS subs (
id INTEGER NOT NULL UNIQUE,
account INTEGER NOT NULL REFERENCES accounts (id),
code VARCHAR NOT NULL,
name VARCHAR DEFAULT '',
info TEXT DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
modified DATETIME DEFAULT (DATETIME('now')),
creator INTEGER NOT NULL,
modifier INTEGER NULL,
active BOOLEAN DEFAULT TRUE,
CONSTRAINT pk_subcodeaccount PRIMARY KEY (code, account),
CHECK (code=UPPER(TRIM(code)))
)'''

create_zone_items = f'''
CREATE TABLE IF NOT EXISTS items (
id INTEGER PRIMARY KEY,
sub INTEGER NULL REFERENCES subs (id), --AR!
ref INTEGER NULL REFERENCES accounts (id), --VAT!
uuid CHAR(36) UNIQUE NOT NULL,
head VARCHAR DEFAULT '', --INVOICE!
info TEXT DEFAULT '',
note TEXT DEFAULT '',
dated DATETIME NULL,
created DATETIME DEFAULT (DATETIME('now')),
modified DATETIME DEFAULT (DATETIME('now')),
creator INTEGER NOT NULL,
modifier INTEGER NULL,
active BOOLEAN DEFAULT TRUE,
cancel BOOLEAN DEFAULT FALSE,
CHECK (uuid=LOWER(TRIM(uuid)))
)'''

create_zone_txs = f'''
CREATE TABLE IF NOT EXISTS txs (
id INTEGER PRIMARY KEY,
uuid CHAR(36) UNIQUE NOT NULL,
tx CHAR(36) NOT NULL,
info TEXT DEFAULT '',
note TEXT DEFAULT '',
dated DATETIME NOT NULL,
ref INTEGER NULL REFERENCES accounts (id), --COR
account INTEGER NOT NULL REFERENCES accounts (id),
sub INTEGER NULL REFERENCES subs (id),
item INTEGER NULL REFERENCES items (id),
debit REAL NOT NULL DEFAULT 0,
credit REAL NOT NULL DEFAULT 0,
created DATETIME DEFAULT (DATETIME('now')),
modified DATETIME DEFAULT (DATETIME('now')),
creator INTEGER NOT NULL,
modifier INTEGER NULL,
CHECK (((debit=0 AND credit>0) OR (credit=0 AND debit>0))
AND (uuid=LOWER(TRIM(uuid))))
)'''

duck_create_zone_roles = sql_uni_replace(create_zone_roles, duck_replaces())
duck_create_zone_specs = sql_uni_replace(create_zone_specs, duck_replaces())
duck_create_zone_specroles = sql_uni_replace(create_zone_specroles, duck_replaces())
duck_create_zone_userspecs = sql_uni_replace(create_zone_userspecs, duck_replaces())
duck_create_zone_userroles = sql_uni_replace(create_zone_userroles, duck_replaces())
duck_create_zone_groups = sql_uni_replace(create_zone_groups, duck_replaces())
duck_create_zone_roots = sql_uni_replace(create_zone_roots, duck_replaces())
duck_create_zone_accounts = sql_uni_replace(create_zone_accounts, duck_replaces())
duck_create_zone_subs = sql_uni_replace(create_zone_subs, duck_replaces())
duck_create_zone_items = sql_uni_replace(create_zone_items, duck_replaces())
duck_create_zone_txs = sql_uni_replace(create_zone_txs, duck_replaces())
