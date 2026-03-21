from .dbs import *

## Admin

def q_rich_select_zone_all_users () -> str:
  return f'''
  SELECT id, name, mail AS email, DATE(obj.created) AS dated, zadmin AS manager, active FROM users obj
  WHERE {check_obj_active(':active')} AND {check_obj_zoneidn(':id',':name')}
  ORDER BY obj.name'''

def q_select_all_users_by_name () -> str:
  return f'''
  {search_idname('users',':name')}
  AND zone IN {zone_case_system(':zoneidn', 'zone')}'''

def q_select_all_zones_by_name () -> str:
  return f'''
  {search_idname('zones',':name')}
  AND id IN {zone_case_system(':zoneidn', 'id')}'''

def q_select_working_login_user () -> str:
  return f'''
  SELECT *, {get_zoneidn_by_useridn(':zoneidn',':conuser')} AS zoneidn, :useridn AS useridn, :conuser AS conuser
  FROM users WHERE {check_strict_user_id_or_name(':id',':name')}
  AND (users.id=1 OR {check_strict_user_working(':worktime')})'''

def q_select_zone_all_users () -> str:
  return f'''
  SELECT * FROM users
  WHERE zone IN (SELECT id FROM zones WHERE {check_zone_id_or_name(':id',':name')})
  ORDER BY name'''

## Accounting

def q_select_pure_specroles () -> str:
  return f'''
  SELECT spec, specs.name as spec_name, role, roles.name as role_name
  FROM specroles, specs, roles
  WHERE spec=specs.id AND role=roles.id'''

def q_select_uni_items () -> str:
  return f'''
  SELECT items.*,
  subs.code AS subcode,
  subs.name AS subname,
  subs.note AS subnote,
  accounts.code AS accountcode,
  accounts.name AS accountname,
  accounts.note AS accountnote,
  roots.code AS rootcode,
  roots.name AS rootname,
  groups.code AS groupcode,
  groups.name AS groupname
  FROM items
  INNER JOIN subs ON items.sub=subs.id
  INNER JOIN accounts ON subs.account=accounts.id
  INNER JOIN roots ON accounts.root=roots.id
  INNER JOIN groups ON roots.grup=groups.id'''

def q_select_uni_subs () -> str:
  return f'''
  SELECT subs.*,
  accounts.code AS accountcode,
  accounts.name AS accountname,
  accounts.note AS accountnote,
  roots.code AS rootcode,
  roots.name AS rootname,
  groups.code AS groupcode,
  groups.name AS groupname
  FROM subs
  INNER JOIN accounts ON subs.account=accounts.id
  INNER JOIN roots ON accounts.root=roots.id
  INNER JOIN groups ON roots.grup=groups.id'''
