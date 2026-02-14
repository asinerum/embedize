from .dcore import check_valid_naming, check_valid_naming2, sql_uni_replace, duck_replaces

create_admin_zones = f'''
CREATE TABLE IF NOT EXISTS zones (
id INTEGER PRIMARY KEY DEFAULT 0,
name VARCHAR UNIQUE NOT NULL,
info TEXT DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
modified DATETIME DEFAULT (DATETIME('now')),
creator INTEGER NULL,
modifier INTEGER NULL,
active BOOLEAN DEFAULT TRUE,
CHECK (name=UPPER(TRIM(name))
 AND id>=0 AND id<=65535
 AND {check_valid_naming()})
)'''

create_admin_users = f'''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
zone INTEGER NOT NULL DEFAULT 0,
name VARCHAR UNIQUE NOT NULL,
hpwd TEXT DEFAULT '',
mail VARCHAR DEFAULT '',
info TEXT DEFAULT '',
note TEXT DEFAULT '',
created DATETIME DEFAULT (DATETIME('now')),
modified DATETIME DEFAULT (DATETIME('now')),
creator INTEGER NULL,
modifier INTEGER NULL,
workbegin DATETIME NULL,
workend DATETIME NULL,
zadmin BOOLEAN DEFAULT FALSE,
active BOOLEAN DEFAULT FALSE,
FOREIGN KEY (zone) REFERENCES zones(id),
CHECK (name=LOWER(TRIM(name))
 AND id>=0
 AND {check_valid_naming()})
)'''

duck_create_admin_zones = sql_uni_replace(create_admin_zones, duck_replaces())
duck_create_admin_users = sql_uni_replace(create_admin_users, duck_replaces())
