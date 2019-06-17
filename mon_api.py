
from typing import List


def auth_add(entity: str, caps: List[str]=None):
    """
    add auth info for <entity> from input file, or random key if no input is given, and/or any caps specified in the command
    :param entity: CephString who=None req=True {}
    :param caps: CephString who=None req=false {}
    module=auth perm=rwx flags=
    """
    prefix = 'auth add'
    _args = {'prefix': prefix, 'entity': entity, 'caps': caps} 

def auth_caps(entity: str, caps: List[str]):
    """
    update caps for <name> from caps specified in the command
    :param entity: CephString who=None req=True {}
    :param caps: CephString who=None req=True {}
    module=auth perm=rwx flags=
    """
    prefix = 'auth caps'
    _args = {'prefix': prefix, 'entity': entity, 'caps': caps} 

def auth_del(entity: str):
    """
    delete all caps for <name>
    :param entity: CephString who=None req=True {}
    module=auth perm=rwx flags=deprecated
    """
    prefix = 'auth del'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_export(entity: str=None):
    """
    write keyring for requested entity, or master keyring if none given
    :param entity: CephString who=None req=false {}
    module=auth perm=rx flags=
    """
    prefix = 'auth export'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_get(entity: str):
    """
    write keyring file with requested key
    :param entity: CephString who=None req=True {}
    module=auth perm=rx flags=
    """
    prefix = 'auth get'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_get_key(entity: str):
    """
    display requested key
    :param entity: CephString who=None req=True {}
    module=auth perm=rx flags=
    """
    prefix = 'auth get-key'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_get_or_create(entity: str, caps: List[str]=None):
    """
    add auth info for <entity> from input file, or random key if no input given, and/or any caps specified in the command
    :param entity: CephString who=None req=True {}
    :param caps: CephString who=None req=false {}
    module=auth perm=rwx flags=
    """
    prefix = 'auth get-or-create'
    _args = {'prefix': prefix, 'entity': entity, 'caps': caps} 

def auth_get_or_create_key(entity: str, caps: List[str]=None):
    """
    get, or add, key for <name> from system/caps pairs specified in the command.  If key already exists, any given caps must match the existing caps for that key.
    :param entity: CephString who=None req=True {}
    :param caps: CephString who=None req=false {}
    module=auth perm=rwx flags=
    """
    prefix = 'auth get-or-create-key'
    _args = {'prefix': prefix, 'entity': entity, 'caps': caps} 

def auth_import():
    """
    auth import: read keyring file from -i <file>

    module=auth perm=rwx flags=
    """
    prefix = 'auth import'
    _args = {'prefix': prefix, } 

def auth_list():
    """
    list authentication state

    module=auth perm=rx flags=deprecated
    """
    prefix = 'auth list'
    _args = {'prefix': prefix, } 

def auth_ls():
    """
    list authentication state

    module=auth perm=rx flags=
    """
    prefix = 'auth ls'
    _args = {'prefix': prefix, } 

def auth_print_key(entity: str):
    """
    display requested key
    :param entity: CephString who=None req=True {}
    module=auth perm=rx flags=
    """
    prefix = 'auth print-key'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_print_key(entity: str):
    """
    display requested key
    :param entity: CephString who=None req=True {}
    module=auth perm=rx flags=
    """
    prefix = 'auth print_key'
    _args = {'prefix': prefix, 'entity': entity} 

def auth_rm(entity: str):
    """
    remove all caps for <name>
    :param entity: CephString who=None req=True {}
    module=auth perm=rwx flags=
    """
    prefix = 'auth rm'
    _args = {'prefix': prefix, 'entity': entity} 

def balancer_dump(plan: str):
    """
    Show an optimization plan
    :param plan: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer dump'
    _args = {'prefix': prefix, 'plan': plan} 

def balancer_eval(option: str=None):
    """
    Evaluate data distribution for the current cluster or specific pool or specific plan
    :param option: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer eval'
    _args = {'prefix': prefix, 'option': option} 

def balancer_eval_verbose(option: str=None):
    """
    Evaluate data distribution for the current cluster or specific pool or specific plan (verbosely)
    :param option: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer eval-verbose'
    _args = {'prefix': prefix, 'option': option} 

def balancer_execute(plan: str):
    """
    Execute an optimization plan
    :param plan: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer execute'
    _args = {'prefix': prefix, 'plan': plan} 

def balancer_ls():
    """
    List all plans

    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer ls'
    _args = {'prefix': prefix, } 

def balancer_mode(mode: str):
    """
    Set balancer mode
    :param mode: CephChoices who=None req=True {u'strings': u'none|crush-compat|upmap'}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer mode'
    _args = {'prefix': prefix, 'mode': mode} 

def balancer_off():
    """
    Disable automatic balancing

    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer off'
    _args = {'prefix': prefix, } 

def balancer_on():
    """
    Enable automatic balancing

    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer on'
    _args = {'prefix': prefix, } 

def balancer_optimize(plan: str, pools: List[str]=None):
    """
    Run optimizer to create a new plan
    :param plan: CephString who=None req=True {}
    :param pools: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer optimize'
    _args = {'prefix': prefix, 'plan': plan, 'pools': pools} 

def balancer_pool_add(pools: List[str]):
    """
    Enable automatic balancing for specific pools
    :param pools: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer pool add'
    _args = {'prefix': prefix, 'pools': pools} 

def balancer_pool_ls():
    """
    List automatic balancing pools. Note that empty list means all existing pools will be automatic balancing targets, which is the default behaviour of balancer.

    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer pool ls'
    _args = {'prefix': prefix, } 

def balancer_pool_rm(pools: List[str]):
    """
    Disable automatic balancing for specific pools
    :param pools: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer pool rm'
    _args = {'prefix': prefix, 'pools': pools} 

def balancer_reset():
    """
    Discard all optimization plans

    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer reset'
    _args = {'prefix': prefix, } 

def balancer_rm(plan: str):
    """
    Discard an optimization plan
    :param plan: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'balancer rm'
    _args = {'prefix': prefix, 'plan': plan} 

def balancer_show(plan: str):
    """
    Show details of an optimization plan
    :param plan: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer show'
    _args = {'prefix': prefix, 'plan': plan} 

def balancer_status():
    """
    Show balancer status

    module=mgr perm=r flags=mgr
    """
    prefix = 'balancer status'
    _args = {'prefix': prefix, } 

def compact():
    """
    cause compaction of monitor's leveldb/rocksdb storage

    module=mon perm=rw flags=deprecated, no_forward
    """
    prefix = 'compact'
    _args = {'prefix': prefix, } 

def config_assimilate_conf():
    """
    Assimilate options from a conf, and return a new, minimal conf file

    module=config perm=rw flags=
    """
    prefix = 'config assimilate-conf'
    _args = {'prefix': prefix, } 

def config_dump():
    """
    Show all configuration option(s)

    module=mon perm=r flags=
    """
    prefix = 'config dump'
    _args = {'prefix': prefix, } 

def config_generate_minimal_conf():
    """
    Generate a minimal ceph.conf file

    module=config perm=r flags=
    """
    prefix = 'config generate-minimal-conf'
    _args = {'prefix': prefix, } 

def config_get(who: str, key: str):
    """
    Show configuration option(s) for an entity
    :param who: CephString who=None req=True {}
    :param key: CephString who=None req=False {}
    module=config perm=r flags=
    """
    prefix = 'config get'
    _args = {'prefix': prefix, 'who': who, 'key': key} 

def config_help(key: str):
    """
    Describe a configuration option
    :param key: CephString who=None req=True {}
    module=config perm=r flags=
    """
    prefix = 'config help'
    _args = {'prefix': prefix, 'key': key} 

def config_log(num: int):
    """
    Show recent history of config changes
    :param num: CephInt who=None req=False {}
    module=config perm=r flags=
    """
    prefix = 'config log'
    _args = {'prefix': prefix, 'num': num} 

def config_ls():
    """
    List available configuration options

    module=config perm=r flags=
    """
    prefix = 'config ls'
    _args = {'prefix': prefix, } 

def config_reset(num: int):
    """
    Revert configuration to a historical version specified by <num>
    :param num: CephInt who=None req=True {u'range': u'0'}
    module=config perm=rw flags=
    """
    prefix = 'config reset'
    _args = {'prefix': prefix, 'num': num} 

def config_rm(who: str, name: str):
    """
    Clear a configuration option for one or more entities
    :param who: CephString who=None req=True {}
    :param name: CephString who=None req=True {}
    module=config perm=rw flags=
    """
    prefix = 'config rm'
    _args = {'prefix': prefix, 'who': who, 'name': name} 

def config_set(who: str, name: str, value: str, force: bool=None):
    """
    Set a configuration option for one or more entities
    :param who: CephString who=None req=True {}
    :param name: CephString who=None req=True {}
    :param value: CephString who=None req=True {}
    :param force: CephBool who=None req=false {}
    module=config perm=rw flags=
    """
    prefix = 'config set'
    _args = {'prefix': prefix, 'who': who, 'name': name, 'value': value, 'force': force} 

def config_show(who: str, key: str):
    """
    Show running configuration
    :param who: CephString who=None req=True {}
    :param key: CephString who=None req=False {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'config show'
    _args = {'prefix': prefix, 'who': who, 'key': key} 

def config_show_with_defaults(who: str):
    """
    Show running configuration (including compiled-in defaults)
    :param who: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'config show-with-defaults'
    _args = {'prefix': prefix, 'who': who} 

def config_key_del(key: str):
    """
    delete <key>
    :param key: CephString who=None req=True {}
    module=config-key perm=rw flags=deprecated
    """
    prefix = 'config-key del'
    _args = {'prefix': prefix, 'key': key} 

def config_key_dump(key: str=None):
    """
    dump keys and values (with optional prefix)
    :param key: CephString who=None req=false {}
    module=config-key perm=r flags=
    """
    prefix = 'config-key dump'
    _args = {'prefix': prefix, 'key': key} 

def config_key_exists(key: str):
    """
    check for <key>'s existence
    :param key: CephString who=None req=True {}
    module=config-key perm=r flags=
    """
    prefix = 'config-key exists'
    _args = {'prefix': prefix, 'key': key} 

def config_key_get(key: str):
    """
    get <key>
    :param key: CephString who=None req=True {}
    module=config-key perm=r flags=
    """
    prefix = 'config-key get'
    _args = {'prefix': prefix, 'key': key} 

def config_key_list():
    """
    list keys

    module=config-key perm=r flags=deprecated
    """
    prefix = 'config-key list'
    _args = {'prefix': prefix, } 

def config_key_ls():
    """
    list keys

    module=config-key perm=r flags=
    """
    prefix = 'config-key ls'
    _args = {'prefix': prefix, } 

def config_key_put(key: str, val: str=None):
    """
    put <key>, value <val>
    :param key: CephString who=None req=True {}
    :param val: CephString who=None req=false {}
    module=config-key perm=rw flags=deprecated
    """
    prefix = 'config-key put'
    _args = {'prefix': prefix, 'key': key, 'val': val} 

def config_key_rm(key: str):
    """
    rm <key>
    :param key: CephString who=None req=True {}
    module=config-key perm=rw flags=
    """
    prefix = 'config-key rm'
    _args = {'prefix': prefix, 'key': key} 

def config_key_set(key: str, val: str=None):
    """
    set <key> to value <val>
    :param key: CephString who=None req=True {}
    :param val: CephString who=None req=false {}
    module=config-key perm=rw flags=
    """
    prefix = 'config-key set'
    _args = {'prefix': prefix, 'key': key, 'val': val} 

def crash_info(id_: str):
    """
    show crash dump metadata
    :param id: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'crash info'
    _args = {'prefix': prefix, 'id': id_} 

def crash_json_report(hours: str):
    """
    Crashes in the last <hours> hours
    :param hours: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'crash json_report'
    _args = {'prefix': prefix, 'hours': hours} 

def crash_ls():
    """
    Show saved crash dumps

    module=mgr perm=r flags=mgr
    """
    prefix = 'crash ls'
    _args = {'prefix': prefix, } 

def crash_post():
    """
    Add a crash dump (use -i <jsonfile>)

    module=mgr perm=rw flags=mgr
    """
    prefix = 'crash post'
    _args = {'prefix': prefix, } 

def crash_prune(keep: str):
    """
    Remove crashes older than <keep> days
    :param keep: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'crash prune'
    _args = {'prefix': prefix, 'keep': keep} 

def crash_rm(id_: str):
    """
    Remove a saved crash <id>
    :param id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'crash rm'
    _args = {'prefix': prefix, 'id': id_} 

def crash_stat():
    """
    Summarize recorded crashes

    module=mgr perm=r flags=mgr
    """
    prefix = 'crash stat'
    _args = {'prefix': prefix, } 

def dashboard_ac_role_add_scope_perms(rolename: str, scopename: str, permissions: List[str]):
    """
    Add the scope permissions for a role
    :param rolename: CephString who=None req=True {}
    :param scopename: CephString who=None req=True {}
    :param permissions: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-role-add-scope-perms'
    _args = {'prefix': prefix, 'rolename': rolename, 'scopename': scopename, 'permissions': permissions} 

def dashboard_ac_role_create(rolename: str, description: str=None):
    """
    Create a new access control role
    :param rolename: CephString who=None req=True {}
    :param description: CephString who=None req=false {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-role-create'
    _args = {'prefix': prefix, 'rolename': rolename, 'description': description} 

def dashboard_ac_role_del_scope_perms(rolename: str, scopename: str):
    """
    Delete the scope permissions for a role
    :param rolename: CephString who=None req=True {}
    :param scopename: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-role-del-scope-perms'
    _args = {'prefix': prefix, 'rolename': rolename, 'scopename': scopename} 

def dashboard_ac_role_delete(rolename: str):
    """
    Delete an access control role
    :param rolename: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-role-delete'
    _args = {'prefix': prefix, 'rolename': rolename} 

def dashboard_ac_role_show(rolename: str=None):
    """
    Show role info
    :param rolename: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard ac-role-show'
    _args = {'prefix': prefix, 'rolename': rolename} 

def dashboard_ac_user_add_roles(username: str, roles: List[str]):
    """
    Add roles to user
    :param username: CephString who=None req=True {}
    :param roles: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-add-roles'
    _args = {'prefix': prefix, 'username': username, 'roles': roles} 

def dashboard_ac_user_create(username: str, password: str=None, rolename: str=None, name: str=None, email: str=None):
    """
    Create a user
    :param username: CephString who=None req=True {}
    :param password: CephString who=None req=false {}
    :param rolename: CephString who=None req=false {}
    :param name: CephString who=None req=false {}
    :param email: CephString who=None req=false {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-create'
    _args = {'prefix': prefix, 'username': username, 'password': password, 'rolename': rolename, 'name': name, 'email': email} 

def dashboard_ac_user_del_roles(username: str, roles: List[str]):
    """
    Delete roles from user
    :param username: CephString who=None req=True {}
    :param roles: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-del-roles'
    _args = {'prefix': prefix, 'username': username, 'roles': roles} 

def dashboard_ac_user_delete(username: str):
    """
    Delete user
    :param username: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-delete'
    _args = {'prefix': prefix, 'username': username} 

def dashboard_ac_user_set_info(username: str, name: str, email: str):
    """
    Set user info
    :param username: CephString who=None req=True {}
    :param name: CephString who=None req=True {}
    :param email: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-set-info'
    _args = {'prefix': prefix, 'username': username, 'name': name, 'email': email} 

def dashboard_ac_user_set_password(username: str, password: str):
    """
    Set user password
    :param username: CephString who=None req=True {}
    :param password: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-set-password'
    _args = {'prefix': prefix, 'username': username, 'password': password} 

def dashboard_ac_user_set_roles(username: str, roles: List[str]):
    """
    Set user roles
    :param username: CephString who=None req=True {}
    :param roles: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard ac-user-set-roles'
    _args = {'prefix': prefix, 'username': username, 'roles': roles} 

def dashboard_ac_user_show(username: str=None):
    """
    Show user info
    :param username: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard ac-user-show'
    _args = {'prefix': prefix, 'username': username} 

def dashboard_create_self_signed_cert():
    """
    Create self signed certificate

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard create-self-signed-cert'
    _args = {'prefix': prefix, } 

def dashboard_feature(action: str, features: List[str]=None):
    """
    Enable or disable features in Ceph-Mgr Dashboard
    :param action: CephChoices who=None req=True {u'strings': u'disable|enable|status'}
    :param features: CephChoices who=None req=false {u'strings': u'cephfs|iscsi|mirroring|rbd|rgw'}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'dashboard feature'
    _args = {'prefix': prefix, 'action': action, 'features': features} 

def dashboard_get_alertmanager_api_host():
    """
    Get the ALERTMANAGER_API_HOST option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-alertmanager-api-host'
    _args = {'prefix': prefix, } 

def dashboard_get_audit_api_enabled():
    """
    Get the AUDIT_API_ENABLED option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-audit-api-enabled'
    _args = {'prefix': prefix, } 

def dashboard_get_audit_api_log_payload():
    """
    Get the AUDIT_API_LOG_PAYLOAD option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-audit-api-log-payload'
    _args = {'prefix': prefix, } 

def dashboard_get_enable_browsable_api():
    """
    Get the ENABLE_BROWSABLE_API option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-enable-browsable-api'
    _args = {'prefix': prefix, } 

def dashboard_get_ganesha_clusters_rados_pool_namespace():
    """
    Get the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-ganesha-clusters-rados-pool-namespace'
    _args = {'prefix': prefix, } 

def dashboard_get_grafana_api_password():
    """
    Get the GRAFANA_API_PASSWORD option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-grafana-api-password'
    _args = {'prefix': prefix, } 

def dashboard_get_grafana_api_url():
    """
    Get the GRAFANA_API_URL option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-grafana-api-url'
    _args = {'prefix': prefix, } 

def dashboard_get_grafana_api_username():
    """
    Get the GRAFANA_API_USERNAME option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-grafana-api-username'
    _args = {'prefix': prefix, } 

def dashboard_get_iscsi_api_ssl_verification():
    """
    Get the ISCSI_API_SSL_VERIFICATION option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-iscsi-api-ssl-verification'
    _args = {'prefix': prefix, } 

def dashboard_get_jwt_token_ttl():
    """
    Get the JWT token TTL in seconds

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-jwt-token-ttl'
    _args = {'prefix': prefix, } 

def dashboard_get_prometheus_api_host():
    """
    Get the PROMETHEUS_API_HOST option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-prometheus-api-host'
    _args = {'prefix': prefix, } 

def dashboard_get_rest_requests_timeout():
    """
    Get the REST_REQUESTS_TIMEOUT option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rest-requests-timeout'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_access_key():
    """
    Get the RGW_API_ACCESS_KEY option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-access-key'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_admin_resource():
    """
    Get the RGW_API_ADMIN_RESOURCE option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-admin-resource'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_host():
    """
    Get the RGW_API_HOST option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-host'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_port():
    """
    Get the RGW_API_PORT option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-port'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_scheme():
    """
    Get the RGW_API_SCHEME option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-scheme'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_secret_key():
    """
    Get the RGW_API_SECRET_KEY option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-secret-key'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_ssl_verify():
    """
    Get the RGW_API_SSL_VERIFY option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-ssl-verify'
    _args = {'prefix': prefix, } 

def dashboard_get_rgw_api_user_id():
    """
    Get the RGW_API_USER_ID option value

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard get-rgw-api-user-id'
    _args = {'prefix': prefix, } 

def dashboard_iscsi_gateway_add(service_url: str):
    """
    Add iSCSI gateway configuration
    :param service_url: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard iscsi-gateway-add'
    _args = {'prefix': prefix, 'service_url': service_url} 

def dashboard_iscsi_gateway_list():
    """
    List iSCSI gateways

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard iscsi-gateway-list'
    _args = {'prefix': prefix, } 

def dashboard_iscsi_gateway_rm(name: str):
    """
    Remove iSCSI gateway configuration
    :param name: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard iscsi-gateway-rm'
    _args = {'prefix': prefix, 'name': name} 

def dashboard_reset_alertmanager_api_host():
    """
    Reset the ALERTMANAGER_API_HOST option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-alertmanager-api-host'
    _args = {'prefix': prefix, } 

def dashboard_reset_audit_api_enabled():
    """
    Reset the AUDIT_API_ENABLED option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-audit-api-enabled'
    _args = {'prefix': prefix, } 

def dashboard_reset_audit_api_log_payload():
    """
    Reset the AUDIT_API_LOG_PAYLOAD option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-audit-api-log-payload'
    _args = {'prefix': prefix, } 

def dashboard_reset_enable_browsable_api():
    """
    Reset the ENABLE_BROWSABLE_API option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-enable-browsable-api'
    _args = {'prefix': prefix, } 

def dashboard_reset_ganesha_clusters_rados_pool_namespace():
    """
    Reset the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-ganesha-clusters-rados-pool-namespace'
    _args = {'prefix': prefix, } 

def dashboard_reset_grafana_api_password():
    """
    Reset the GRAFANA_API_PASSWORD option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-grafana-api-password'
    _args = {'prefix': prefix, } 

def dashboard_reset_grafana_api_url():
    """
    Reset the GRAFANA_API_URL option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-grafana-api-url'
    _args = {'prefix': prefix, } 

def dashboard_reset_grafana_api_username():
    """
    Reset the GRAFANA_API_USERNAME option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-grafana-api-username'
    _args = {'prefix': prefix, } 

def dashboard_reset_iscsi_api_ssl_verification():
    """
    Reset the ISCSI_API_SSL_VERIFICATION option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-iscsi-api-ssl-verification'
    _args = {'prefix': prefix, } 

def dashboard_reset_prometheus_api_host():
    """
    Reset the PROMETHEUS_API_HOST option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-prometheus-api-host'
    _args = {'prefix': prefix, } 

def dashboard_reset_rest_requests_timeout():
    """
    Reset the REST_REQUESTS_TIMEOUT option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rest-requests-timeout'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_access_key():
    """
    Reset the RGW_API_ACCESS_KEY option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-access-key'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_admin_resource():
    """
    Reset the RGW_API_ADMIN_RESOURCE option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-admin-resource'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_host():
    """
    Reset the RGW_API_HOST option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-host'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_port():
    """
    Reset the RGW_API_PORT option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-port'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_scheme():
    """
    Reset the RGW_API_SCHEME option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-scheme'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_secret_key():
    """
    Reset the RGW_API_SECRET_KEY option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-secret-key'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_ssl_verify():
    """
    Reset the RGW_API_SSL_VERIFY option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-ssl-verify'
    _args = {'prefix': prefix, } 

def dashboard_reset_rgw_api_user_id():
    """
    Reset the RGW_API_USER_ID option to its default value

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard reset-rgw-api-user-id'
    _args = {'prefix': prefix, } 

def dashboard_set_alertmanager_api_host(value: str):
    """
    Set the ALERTMANAGER_API_HOST option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-alertmanager-api-host'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_audit_api_enabled(value: str):
    """
    Set the AUDIT_API_ENABLED option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-audit-api-enabled'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_audit_api_log_payload(value: str):
    """
    Set the AUDIT_API_LOG_PAYLOAD option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-audit-api-log-payload'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_enable_browsable_api(value: str):
    """
    Set the ENABLE_BROWSABLE_API option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-enable-browsable-api'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_ganesha_clusters_rados_pool_namespace(value: str):
    """
    Set the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-ganesha-clusters-rados-pool-namespace'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_grafana_api_password(value: str):
    """
    Set the GRAFANA_API_PASSWORD option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-grafana-api-password'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_grafana_api_url(value: str):
    """
    Set the GRAFANA_API_URL option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-grafana-api-url'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_grafana_api_username(value: str):
    """
    Set the GRAFANA_API_USERNAME option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-grafana-api-username'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_iscsi_api_ssl_verification(value: str):
    """
    Set the ISCSI_API_SSL_VERIFICATION option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-iscsi-api-ssl-verification'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_jwt_token_ttl(seconds: int):
    """
    Set the JWT token TTL in seconds
    :param seconds: CephInt who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-jwt-token-ttl'
    _args = {'prefix': prefix, 'seconds': seconds} 

def dashboard_set_login_credentials(username: str, password: str):
    """
    Set the login credentials
    :param username: CephString who=None req=True {}
    :param password: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-login-credentials'
    _args = {'prefix': prefix, 'username': username, 'password': password} 

def dashboard_set_prometheus_api_host(value: str):
    """
    Set the PROMETHEUS_API_HOST option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-prometheus-api-host'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rest_requests_timeout(value: int):
    """
    Set the REST_REQUESTS_TIMEOUT option value
    :param value: CephInt who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rest-requests-timeout'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_access_key(value: str):
    """
    Set the RGW_API_ACCESS_KEY option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-access-key'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_admin_resource(value: str):
    """
    Set the RGW_API_ADMIN_RESOURCE option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-admin-resource'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_host(value: str):
    """
    Set the RGW_API_HOST option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-host'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_port(value: int):
    """
    Set the RGW_API_PORT option value
    :param value: CephInt who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-port'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_scheme(value: str):
    """
    Set the RGW_API_SCHEME option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-scheme'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_secret_key(value: str):
    """
    Set the RGW_API_SECRET_KEY option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-secret-key'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_ssl_verify(value: str):
    """
    Set the RGW_API_SSL_VERIFY option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-ssl-verify'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_set_rgw_api_user_id(value: str):
    """
    Set the RGW_API_USER_ID option value
    :param value: CephString who=None req=True {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard set-rgw-api-user-id'
    _args = {'prefix': prefix, 'value': value} 

def dashboard_sso_disable():
    """
    Disable Single Sign-On

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard sso disable'
    _args = {'prefix': prefix, } 

def dashboard_sso_enable_saml2():
    """
    Enable SAML2 Single Sign-On

    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard sso enable saml2'
    _args = {'prefix': prefix, } 

def dashboard_sso_setup_saml2(ceph_dashboard_base_url: str, idp_metadata: str, idp_username_attribute: str=None, idp_entity_id: str=None, sp_x_509_cert: str=None, sp_private_key: str=None):
    """
    Setup SAML2 Single Sign-On
    :param ceph_dashboard_base_url: CephString who=None req=True {}
    :param idp_metadata: CephString who=None req=True {}
    :param idp_username_attribute: CephString who=None req=false {}
    :param idp_entity_id: CephString who=None req=false {}
    :param sp_x_509_cert: CephString who=None req=false {}
    :param sp_private_key: CephString who=None req=false {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'dashboard sso setup saml2'
    _args = {'prefix': prefix, 'ceph_dashboard_base_url': ceph_dashboard_base_url, 'idp_metadata': idp_metadata, 'idp_username_attribute': idp_username_attribute, 'idp_entity_id': idp_entity_id, 'sp_x_509_cert': sp_x_509_cert, 'sp_private_key': sp_private_key} 

def dashboard_sso_show_saml2():
    """
    Show SAML2 configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard sso show saml2'
    _args = {'prefix': prefix, } 

def dashboard_sso_status():
    """
    Get Single Sign-On status

    module=mgr perm=r flags=mgr
    """
    prefix = 'dashboard sso status'
    _args = {'prefix': prefix, } 

def deepsea_config_set(key: str, value: str):
    """
    Set a configuration value
    :param key: CephString who=None req=True {}
    :param value: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'deepsea config-set'
    _args = {'prefix': prefix, 'key': key, 'value': value} 

def deepsea_config_show():
    """
    Show current configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'deepsea config-show'
    _args = {'prefix': prefix, } 

def device_check_health():
    """
    Check life expectancy of devices

    module=mgr perm=rw flags=mgr
    """
    prefix = 'device check-health'
    _args = {'prefix': prefix, } 

def device_debug_metrics_forced():
    """
    Run metrics agent forced

    module=mgr perm=r flags=mgr
    """
    prefix = 'device debug metrics-forced'
    _args = {'prefix': prefix, } 

def device_debug_smart_forced():
    """
    Run smart agent forced

    module=mgr perm=r flags=mgr
    """
    prefix = 'device debug smart-forced'
    _args = {'prefix': prefix, } 

def device_get_health_metrics(devid: str, sample: str):
    """
    Show stored device metrics for the device
    :param devid: CephString who=None req=True {}
    :param sample: CephString who=None req=False {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device get-health-metrics'
    _args = {'prefix': prefix, 'devid': devid, 'sample': sample} 

def device_info(devid: str):
    """
    Show information about a device
    :param devid: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device info'
    _args = {'prefix': prefix, 'devid': devid} 

def device_ls():
    """
    Show devices

    module=mgr perm=r flags=mgr
    """
    prefix = 'device ls'
    _args = {'prefix': prefix, } 

def device_ls_by_daemon(who: str):
    """
    Show devices associated with a daemon
    :param who: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device ls-by-daemon'
    _args = {'prefix': prefix, 'who': who} 

def device_ls_by_host(host: str):
    """
    Show devices on a host
    :param host: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device ls-by-host'
    _args = {'prefix': prefix, 'host': host} 

def device_monitoring_off():
    """
    Disable device health monitoring

    module=mgr perm=rw flags=mgr
    """
    prefix = 'device monitoring off'
    _args = {'prefix': prefix, } 

def device_monitoring_on():
    """
    Enable device health monitoring

    module=mgr perm=rw flags=mgr
    """
    prefix = 'device monitoring on'
    _args = {'prefix': prefix, } 

def device_predict_life_expectancy(devid: str):
    """
    Predict life expectancy with local predictor
    :param devid: CephString who=None req=true {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device predict-life-expectancy'
    _args = {'prefix': prefix, 'devid': devid} 

def device_query_daemon_health_metrics(who: str):
    """
    Get device health metrics for a given daemon
    :param who: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device query-daemon-health-metrics'
    _args = {'prefix': prefix, 'who': who} 

def device_rm_life_expectancy(devid: str):
    """
    Clear predicted device life expectancy
    :param devid: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'device rm-life-expectancy'
    _args = {'prefix': prefix, 'devid': devid} 

def device_scrape_daemon_health_metrics(who: str):
    """
    Scrape and store device health metrics for a given daemon
    :param who: CephString who=None req=True {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device scrape-daemon-health-metrics'
    _args = {'prefix': prefix, 'who': who} 

def device_scrape_health_metrics(devid: str):
    """
    Scrape and store health metrics
    :param devid: CephString who=None req=False {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'device scrape-health-metrics'
    _args = {'prefix': prefix, 'devid': devid} 

def device_set_cloud_prediction_config(server: str, user: str, password: str, certfile: str, port: str=None):
    """
    Configure Disk Prediction service
    :param server: CephString who=None req=true {}
    :param user: CephString who=None req=true {}
    :param password: CephString who=None req=true {}
    :param certfile: CephString who=None req=true {}
    :param port: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'device set-cloud-prediction-config'
    _args = {'prefix': prefix, 'server': server, 'user': user, 'password': password, 'certfile': certfile, 'port': port} 

def device_set_life_expectancy(devid: str, from_: str, to: str):
    """
    Set predicted device life expectancy
    :param devid: CephString who=None req=True {}
    :param from: CephString who=None req=True {}
    :param to: CephString who=None req=False {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'device set-life-expectancy'
    _args = {'prefix': prefix, 'devid': devid, 'from': from_, 'to': to} 

def device_show_prediction_config():
    """
    Prints diskprediction configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'device show-prediction-config'
    _args = {'prefix': prefix, } 

def df(detail: str=None):
    """
    show cluster free space stats
    :param detail: CephChoices who=None req=false {u'strings': u'detail'}
    module=mon perm=r flags=
    """
    prefix = 'df'
    _args = {'prefix': prefix, 'detail': detail} 

def diskprediction_cloud_status():
    """
    Check diskprediction_cloud status

    module=mgr perm=r flags=mgr
    """
    prefix = 'diskprediction_cloud status'
    _args = {'prefix': prefix, } 

def features():
    """
    report of connected features

    module=mon perm=r flags=
    """
    prefix = 'features'
    _args = {'prefix': prefix, } 

def fs_add_data_pool(fs_name: str, pool: str):
    """
    add data pool <pool>
    :param fs_name: CephString who=None req=True {}
    :param pool: CephString who=None req=True {}
    module=mds perm=rw flags=
    """
    prefix = 'fs add_data_pool'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'pool': pool} 

def fs_authorize(filesystem: str, entity: str, caps: List[str]):
    """
    add auth for <entity> to access file system <filesystem> based on following directory and permissions pairs
    :param filesystem: CephString who=None req=True {}
    :param entity: CephString who=None req=True {}
    :param caps: CephString who=None req=True {}
    module=auth perm=rwx flags=
    """
    prefix = 'fs authorize'
    _args = {'prefix': prefix, 'filesystem': filesystem, 'entity': entity, 'caps': caps} 

def fs_dump(epoch: int=None):
    """
    dump all CephFS status, optionally from epoch
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mds perm=r flags=
    """
    prefix = 'fs dump'
    _args = {'prefix': prefix, 'epoch': epoch} 

def fs_fail(fs_name: str):
    """
    bring the file system down and all of its ranks
    :param fs_name: CephString who=None req=True {}
    module=fs perm=rw flags=
    """
    prefix = 'fs fail'
    _args = {'prefix': prefix, 'fs_name': fs_name} 

def fs_flag_set(flag_name: str, val: str, yes_i_really_mean_it: bool=None):
    """
    Set a global CephFS flag
    :param flag_name: CephChoices who=None req=True {u'strings': u'enable_multiple'}
    :param val: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=fs perm=rw flags=
    """
    prefix = 'fs flag set'
    _args = {'prefix': prefix, 'flag_name': flag_name, 'val': val, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def fs_get(fs_name: str):
    """
    get info about one filesystem
    :param fs_name: CephString who=None req=True {}
    module=fs perm=r flags=
    """
    prefix = 'fs get'
    _args = {'prefix': prefix, 'fs_name': fs_name} 

def fs_ls():
    """
    list filesystems

    module=fs perm=r flags=
    """
    prefix = 'fs ls'
    _args = {'prefix': prefix, } 

def fs_new(fs_name: str, metadata: str, data: str, force: bool=None, allow_dangerous_metadata_overlay: bool=None):
    """
    make new filesystem using named pools <metadata> and <data>
    :param fs_name: CephString who=None req=True {}
    :param metadata: CephString who=None req=True {}
    :param data: CephString who=None req=True {}
    :param force: CephBool who=None req=false {}
    :param allow_dangerous_metadata_overlay: CephBool who=None req=false {}
    module=fs perm=rw flags=
    """
    prefix = 'fs new'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'metadata': metadata, 'data': data, 'force': force, 'allow_dangerous_metadata_overlay': allow_dangerous_metadata_overlay} 

def fs_reset(fs_name: str, yes_i_really_mean_it: bool=None):
    """
    disaster recovery only: reset to a single-MDS map
    :param fs_name: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=fs perm=rw flags=
    """
    prefix = 'fs reset'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def fs_rm(fs_name: str, yes_i_really_mean_it: bool=None):
    """
    disable the named filesystem
    :param fs_name: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=fs perm=rw flags=
    """
    prefix = 'fs rm'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def fs_rm_data_pool(fs_name: str, pool: str):
    """
    remove data pool <pool>
    :param fs_name: CephString who=None req=True {}
    :param pool: CephString who=None req=True {}
    module=mds perm=rw flags=
    """
    prefix = 'fs rm_data_pool'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'pool': pool} 

def fs_set(fs_name: str, var: str, val: str, yes_i_really_mean_it: bool=None):
    """
    set fs parameter <var> to <val>
    :param fs_name: CephString who=None req=True {}
    :param var: CephChoices who=None req=True {u'strings': u'max_mds|max_file_size|allow_new_snaps|inline_data|cluster_down|allow_dirfrags|balancer|standby_count_wanted|session_timeout|session_autoclose|allow_standby_replay|down|joinable|min_compat_client'}
    :param val: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=mds perm=rw flags=
    """
    prefix = 'fs set'
    _args = {'prefix': prefix, 'fs_name': fs_name, 'var': var, 'val': val, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def fs_set_default(fs_name: str):
    """
    set the default to the named filesystem
    :param fs_name: CephString who=None req=True {}
    module=fs perm=rw flags=
    """
    prefix = 'fs set-default'
    _args = {'prefix': prefix, 'fs_name': fs_name} 

def fs_set_default(fs_name: str):
    """
    set the default to the named filesystem
    :param fs_name: CephString who=None req=True {}
    module=fs perm=rw flags=deprecated
    """
    prefix = 'fs set_default'
    _args = {'prefix': prefix, 'fs_name': fs_name} 

def fs_status(fs: str=None):
    """
    Show the status of a CephFS filesystem
    :param fs: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'fs status'
    _args = {'prefix': prefix, 'fs': fs} 

def fs_subvolume_create(vol_name: str, sub_name: str, size: int=None, group_name: str=None):
    """
    Create a CephFS subvolume in a volume, and optionally, with a specific size (in bytes) and in a specific subvolume group
    :param vol_name: CephString who=None req=True {}
    :param sub_name: CephString who=None req=True {}
    :param size: CephInt who=None req=false {}
    :param group_name: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolume create'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'sub_name': sub_name, 'size': size, 'group_name': group_name} 

def fs_subvolume_getpath(vol_name: str, sub_name: str, group_name: str=None):
    """
    Get the mountpath of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
    :param vol_name: CephString who=None req=True {}
    :param sub_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolume getpath'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'sub_name': sub_name, 'group_name': group_name} 

def fs_subvolume_rm(vol_name: str, sub_name: str, group_name: str=None, force: bool=None):
    """
    Delete a CephFS subvolume in a volume, and optionally, in a specific subvolume group
    :param vol_name: CephString who=None req=True {}
    :param sub_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=false {}
    :param force: CephBool who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolume rm'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'sub_name': sub_name, 'group_name': group_name, 'force': force} 

def fs_subvolume_snapshot_create(vol_name: str, sub_name: str, snap_name: str, group_name: str=None):
    """
    Create a snapshot of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
    :param vol_name: CephString who=None req=True {}
    :param sub_name: CephString who=None req=True {}
    :param snap_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolume snapshot create'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'sub_name': sub_name, 'snap_name': snap_name, 'group_name': group_name} 

def fs_subvolume_snapshot_rm(vol_name: str, sub_name: str, snap_name: str, group_name: str=None, force: bool=None):
    """
    Delete a snapshot of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
    :param vol_name: CephString who=None req=True {}
    :param sub_name: CephString who=None req=True {}
    :param snap_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=false {}
    :param force: CephBool who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolume snapshot rm'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'sub_name': sub_name, 'snap_name': snap_name, 'group_name': group_name, 'force': force} 

def fs_subvolumegroup_create(vol_name: str, group_name: str):
    """
    Create a CephFS subvolume group in a volume
    :param vol_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolumegroup create'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'group_name': group_name} 

def fs_subvolumegroup_rm(vol_name: str, group_name: str, force: bool=None):
    """
    Delete a CephFS subvolume group in a volume
    :param vol_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=True {}
    :param force: CephBool who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolumegroup rm'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'group_name': group_name, 'force': force} 

def fs_subvolumegroup_snapshot_create(vol_name: str, group_name: str, snap_name: str):
    """
    Create a snapshot of a CephFS subvolume group in a volume
    :param vol_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=True {}
    :param snap_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolumegroup snapshot create'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'group_name': group_name, 'snap_name': snap_name} 

def fs_subvolumegroup_snapshot_rm(vol_name: str, group_name: str, snap_name: str, force: bool=None):
    """
    Delete a snapshot of a CephFS subvolume group in a volume
    :param vol_name: CephString who=None req=True {}
    :param group_name: CephString who=None req=True {}
    :param snap_name: CephString who=None req=True {}
    :param force: CephBool who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs subvolumegroup snapshot rm'
    _args = {'prefix': prefix, 'vol_name': vol_name, 'group_name': group_name, 'snap_name': snap_name, 'force': force} 

def fs_volume_create(name: str, size: str=None):
    """
    Create a CephFS volume
    :param name: CephString who=None req=True {}
    :param size: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs volume create'
    _args = {'prefix': prefix, 'name': name, 'size': size} 

def fs_volume_ls():
    """
    List volumes

    module=mgr perm=r flags=mgr
    """
    prefix = 'fs volume ls'
    _args = {'prefix': prefix, } 

def fs_volume_rm(vol_name: str):
    """
    Delete a CephFS volume
    :param vol_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'fs volume rm'
    _args = {'prefix': prefix, 'vol_name': vol_name} 

def fsid():
    """
    show cluster FSID/UUID

    module=mon perm=r flags=
    """
    prefix = 'fsid'
    _args = {'prefix': prefix, } 

def health(detail: str=None):
    """
    show cluster health
    :param detail: CephChoices who=None req=false {u'strings': u'detail'}
    module=mon perm=r flags=
    """
    prefix = 'health'
    _args = {'prefix': prefix, 'detail': detail} 

def heap(heapcmd: str):
    """
    show heap usage info (available only if compiled with tcmalloc)
    :param heapcmd: CephChoices who=None req=True {u'strings': u'dump|start_profiler|stop_profiler|release|stats'}
    module=mon perm=rw flags=no_forward
    """
    prefix = 'heap'
    _args = {'prefix': prefix, 'heapcmd': heapcmd} 

def hello(person_name: str=None):
    """
    Prints hello world to mgr.x.log
    :param person_name: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'hello'
    _args = {'prefix': prefix, 'person_name': person_name} 

def influx_config_set(key: str, value: str):
    """
    Set a configuration value
    :param key: CephString who=None req=True {}
    :param value: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'influx config-set'
    _args = {'prefix': prefix, 'key': key, 'value': value} 

def influx_config_show():
    """
    Show current configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'influx config-show'
    _args = {'prefix': prefix, } 

def influx_send():
    """
    Force sending data to Influx

    module=mgr perm=rw flags=mgr
    """
    prefix = 'influx send'
    _args = {'prefix': prefix, } 

def injectargs(injected_args: List[str]):
    """
    inject config arguments into monitor
    :param injected_args: CephString who=None req=True {}
    module=mon perm=rw flags=no_forward
    """
    prefix = 'injectargs'
    _args = {'prefix': prefix, 'injected_args': injected_args} 

def insights():
    """
    Retrieve insights report

    module=mgr perm=r flags=mgr
    """
    prefix = 'insights'
    _args = {'prefix': prefix, } 

def insights_prune_health(hours: str):
    """
    Remove health history older than <hours> hours
    :param hours: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'insights prune-health'
    _args = {'prefix': prefix, 'hours': hours} 

def iostat():
    """
    Get IO rates

    module=mgr perm=r flags=mgr, poll
    """
    prefix = 'iostat'
    _args = {'prefix': prefix, } 

def log(logtext: List[str]):
    """
    log supplied text to the monitor log
    :param logtext: CephString who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'log'
    _args = {'prefix': prefix, 'logtext': logtext} 

def log_last(num: int=None, level: str=None, channel: str=None):
    """
    print last few lines of the cluster log
    :param num: CephInt who=None req=false {u'range': u'1'}
    :param level: CephChoices who=None req=false {u'strings': u'debug|info|sec|warn|error'}
    :param channel: CephChoices who=None req=false {u'strings': u'*|cluster|audit'}
    module=mon perm=r flags=
    """
    prefix = 'log last'
    _args = {'prefix': prefix, 'num': num, 'level': level, 'channel': channel} 

def mds_add_data_pool(pool: str):
    """
    add data pool <pool>
    :param pool: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds add_data_pool'
    _args = {'prefix': prefix, 'pool': pool} 

def mds_cluster_down():
    """
    take MDS cluster down

    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds cluster_down'
    _args = {'prefix': prefix, } 

def mds_cluster_up():
    """
    bring MDS cluster up

    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds cluster_up'
    _args = {'prefix': prefix, } 

def mds_compat_rm_compat(feature: int):
    """
    remove compatible feature
    :param feature: CephInt who=None req=True {u'range': u'0'}
    module=mds perm=rw flags=
    """
    prefix = 'mds compat rm_compat'
    _args = {'prefix': prefix, 'feature': feature} 

def mds_compat_rm_incompat(feature: int):
    """
    remove incompatible feature
    :param feature: CephInt who=None req=True {u'range': u'0'}
    module=mds perm=rw flags=
    """
    prefix = 'mds compat rm_incompat'
    _args = {'prefix': prefix, 'feature': feature} 

def mds_compat_show():
    """
    show mds compatibility settings

    module=mds perm=r flags=
    """
    prefix = 'mds compat show'
    _args = {'prefix': prefix, } 

def mds_count_metadata(property: str):
    """
    count MDSs by metadata field property
    :param property: CephString who=None req=True {}
    module=mds perm=r flags=
    """
    prefix = 'mds count-metadata'
    _args = {'prefix': prefix, 'property': property} 

def mds_deactivate(role: str):
    """
    clean up specified MDS rank (use with `set max_mds` to shrink cluster)
    :param role: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds deactivate'
    _args = {'prefix': prefix, 'role': role} 

def mds_dump(epoch: int=None):
    """
    dump legacy MDS cluster info, optionally from epoch
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mds perm=r flags=obsolete
    """
    prefix = 'mds dump'
    _args = {'prefix': prefix, 'epoch': epoch} 

def mds_fail(role_or_gid: str):
    """
    Mark MDS failed: trigger a failover if a standby is available
    :param role_or_gid: CephString who=None req=True {}
    module=mds perm=rw flags=
    """
    prefix = 'mds fail'
    _args = {'prefix': prefix, 'role_or_gid': role_or_gid} 

def mds_freeze(role_or_gid: str, val: str):
    """
    freeze MDS yes/no
    :param role_or_gid: CephString who=None req=True {}
    :param val: CephString who=None req=True {}
    module=mds perm=rw flags=hidden
    """
    prefix = 'mds freeze'
    _args = {'prefix': prefix, 'role_or_gid': role_or_gid, 'val': val} 

def mds_getmap(epoch: int=None):
    """
    get MDS map, optionally from epoch
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mds perm=r flags=obsolete
    """
    prefix = 'mds getmap'
    _args = {'prefix': prefix, 'epoch': epoch} 

def mds_metadata(who: str=None):
    """
    fetch metadata for mds <role>
    :param who: CephString who=None req=false {}
    module=mds perm=r flags=
    """
    prefix = 'mds metadata'
    _args = {'prefix': prefix, 'who': who} 

def mds_newfs(metadata: int, data: int, yes_i_really_mean_it: bool=None):
    """
    make new filesystem using pools <metadata> and <data>
    :param metadata: CephInt who=None req=True {u'range': u'0'}
    :param data: CephInt who=None req=True {u'range': u'0'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds newfs'
    _args = {'prefix': prefix, 'metadata': metadata, 'data': data, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def mds_ok_to_stop(ids: List[str]):
    """
    check whether stopping the specified MDS would reduce immediate availability
    :param ids: CephString who=None req=True {}
    module=mds perm=r flags=
    """
    prefix = 'mds ok-to-stop'
    _args = {'prefix': prefix, 'ids': ids} 

def mds_remove_data_pool(pool: str):
    """
    remove data pool <pool>
    :param pool: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds remove_data_pool'
    _args = {'prefix': prefix, 'pool': pool} 

def mds_repaired(role: str):
    """
    mark a damaged MDS rank as no longer damaged
    :param role: CephString who=None req=True {}
    module=mds perm=rw flags=
    """
    prefix = 'mds repaired'
    _args = {'prefix': prefix, 'role': role} 

def mds_rm(gid: int):
    """
    remove nonactive mds
    :param gid: CephInt who=None req=True {u'range': u'0'}
    module=mds perm=rw flags=
    """
    prefix = 'mds rm'
    _args = {'prefix': prefix, 'gid': gid} 

def mds_rm_data_pool(pool: str):
    """
    remove data pool <pool>
    :param pool: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds rm_data_pool'
    _args = {'prefix': prefix, 'pool': pool} 

def mds_rmfailed(role: str, yes_i_really_mean_it: bool=None):
    """
    remove failed rank
    :param role: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=mds perm=rw flags=hidden
    """
    prefix = 'mds rmfailed'
    _args = {'prefix': prefix, 'role': role, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def mds_set(var: str, val: str, yes_i_really_mean_it: bool=None):
    """
    set mds parameter <var> to <val>
    :param var: CephChoices who=None req=True {u'strings': u'max_mds|max_file_size|inline_data|allow_new_snaps|allow_multimds|allow_multimds_snaps|allow_dirfrags'}
    :param val: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds set'
    _args = {'prefix': prefix, 'var': var, 'val': val, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def mds_set_max_mds(maxmds: int):
    """
    set max MDS index
    :param maxmds: CephInt who=None req=True {u'range': u'0'}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds set_max_mds'
    _args = {'prefix': prefix, 'maxmds': maxmds} 

def mds_set_state(gid: int, state: int):
    """
    set mds state of <gid> to <numeric-state>
    :param gid: CephInt who=None req=True {u'range': u'0'}
    :param state: CephInt who=None req=True {u'range': u'0|20'}
    module=mds perm=rw flags=hidden
    """
    prefix = 'mds set_state'
    _args = {'prefix': prefix, 'gid': gid, 'state': state} 

def mds_stat():
    """
    show MDS status

    module=mds perm=r flags=hidden
    """
    prefix = 'mds stat'
    _args = {'prefix': prefix, } 

def mds_stop(role: str):
    """
    stop mds
    :param role: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds stop'
    _args = {'prefix': prefix, 'role': role} 

def mds_tell(who: str, args: List[str]):
    """
    send command to particular mds
    :param who: CephString who=None req=True {}
    :param args: CephString who=None req=True {}
    module=mds perm=rw flags=obsolete
    """
    prefix = 'mds tell'
    _args = {'prefix': prefix, 'who': who, 'args': args} 

def mds_versions():
    """
    check running versions of MDSs

    module=mds perm=r flags=
    """
    prefix = 'mds versions'
    _args = {'prefix': prefix, } 

def mgr_count_metadata(property: str):
    """
    count ceph-mgr daemons by metadata field property
    :param property: CephString who=None req=True {}
    module=mgr perm=r flags=
    """
    prefix = 'mgr count-metadata'
    _args = {'prefix': prefix, 'property': property} 

def mgr_dump(epoch: int=None):
    """
    dump the latest MgrMap
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mgr perm=r flags=
    """
    prefix = 'mgr dump'
    _args = {'prefix': prefix, 'epoch': epoch} 

def mgr_fail(who: str):
    """
    treat the named manager daemon as failed
    :param who: CephString who=None req=True {}
    module=mgr perm=rw flags=
    """
    prefix = 'mgr fail'
    _args = {'prefix': prefix, 'who': who} 

def mgr_metadata(who: str=None):
    """
    dump metadata for all daemons or a specific daemon
    :param who: CephString who=None req=false {}
    module=mgr perm=r flags=
    """
    prefix = 'mgr metadata'
    _args = {'prefix': prefix, 'who': who} 

def mgr_module_disable(module: str):
    """
    disable mgr module
    :param module: CephString who=None req=True {}
    module=mgr perm=rw flags=
    """
    prefix = 'mgr module disable'
    _args = {'prefix': prefix, 'module': module} 

def mgr_module_enable(module: str, force: str=None):
    """
    enable mgr module
    :param module: CephString who=None req=True {}
    :param force: CephChoices who=None req=false {u'strings': u'--force'}
    module=mgr perm=rw flags=
    """
    prefix = 'mgr module enable'
    _args = {'prefix': prefix, 'module': module, 'force': force} 

def mgr_module_ls():
    """
    list active mgr modules

    module=mgr perm=r flags=
    """
    prefix = 'mgr module ls'
    _args = {'prefix': prefix, } 

def mgr_self_test_background_start(workload: str):
    """
    Activate a background workload (one of command_spam, throw_exception)
    :param workload: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test background start'
    _args = {'prefix': prefix, 'workload': workload} 

def mgr_self_test_background_stop():
    """
    Stop background workload if any is running

    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test background stop'
    _args = {'prefix': prefix, } 

def mgr_self_test_cluster_log(channel: str, priority: str, message: str):
    """
    Create an audit log record.
    :param channel: CephString who=None req=True {}
    :param priority: CephString who=None req=True {}
    :param message: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test cluster-log'
    _args = {'prefix': prefix, 'channel': channel, 'priority': priority, 'message': message} 

def mgr_self_test_config_get(key: str):
    """
    Peek at a configuration value
    :param key: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test config get'
    _args = {'prefix': prefix, 'key': key} 

def mgr_self_test_config_get_localized(key: str):
    """
    Peek at a configuration value (localized variant)
    :param key: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test config get_localized'
    _args = {'prefix': prefix, 'key': key} 

def mgr_self_test_health_clear(checks: List[str]):
    """
    Clear health checks by name. If no names provided, clear all.
    :param checks: CephString who=None req=False {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test health clear'
    _args = {'prefix': prefix, 'checks': checks} 

def mgr_self_test_health_set(checks: str):
    """
    Set a health check from a JSON-formatted description.
    :param checks: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test health set'
    _args = {'prefix': prefix, 'checks': checks} 

def mgr_self_test_insights_set_now_offset(hours: str):
    """
    Set the now time for the insights module.
    :param hours: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test insights_set_now_offset'
    _args = {'prefix': prefix, 'hours': hours} 

def mgr_self_test_module(module: str):
    """
    Run another module's self_test() method
    :param module: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test module'
    _args = {'prefix': prefix, 'module': module} 

def mgr_self_test_remote():
    """
    Test inter-module calls

    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test remote'
    _args = {'prefix': prefix, } 

def mgr_self_test_run():
    """
    Run mgr python interface tests

    module=mgr perm=rw flags=mgr
    """
    prefix = 'mgr self-test run'
    _args = {'prefix': prefix, } 

def mgr_services():
    """
    list service endpoints provided by mgr modules

    module=mgr perm=r flags=
    """
    prefix = 'mgr services'
    _args = {'prefix': prefix, } 

def mgr_versions():
    """
    check running versions of ceph-mgr daemons

    module=mgr perm=r flags=
    """
    prefix = 'mgr versions'
    _args = {'prefix': prefix, } 

def mon_add(name: str, addr: str):
    """
    add new monitor named <name> at <addr>
    :param name: CephString who=None req=True {}
    :param addr: CephIPAddr who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'mon add'
    _args = {'prefix': prefix, 'name': name, 'addr': addr} 

def mon_compact():
    """
    cause compaction of monitor's leveldb/rocksdb storage

    module=mon perm=rw flags=no_forward
    """
    prefix = 'mon compact'
    _args = {'prefix': prefix, } 

def mon_count_metadata(property: str):
    """
    count mons by metadata field property
    :param property: CephString who=None req=True {}
    module=mon perm=r flags=
    """
    prefix = 'mon count-metadata'
    _args = {'prefix': prefix, 'property': property} 

def mon_dump(epoch: int=None):
    """
    dump formatted monmap (optionally from epoch)
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mon perm=r flags=
    """
    prefix = 'mon dump'
    _args = {'prefix': prefix, 'epoch': epoch} 

def mon_enable_msgr2():
    """
    enable the msgr2 protocol on port 3300

    module=mon perm=rw flags=
    """
    prefix = 'mon enable-msgr2'
    _args = {'prefix': prefix, } 

def mon_feature_ls(with_value: str=None):
    """
    list available mon map features to be set/unset
    :param with_value: CephChoices who=None req=false {u'strings': u'--with-value'}
    module=mon perm=r flags=
    """
    prefix = 'mon feature ls'
    _args = {'prefix': prefix, 'with_value': with_value} 

def mon_feature_set(feature_name: str, yes_i_really_mean_it: bool=None):
    """
    set provided feature on mon map
    :param feature_name: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=mon perm=rw flags=
    """
    prefix = 'mon feature set'
    _args = {'prefix': prefix, 'feature_name': feature_name, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def mon_getmap(epoch: int=None):
    """
    get monmap
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=mon perm=r flags=
    """
    prefix = 'mon getmap'
    _args = {'prefix': prefix, 'epoch': epoch} 

def mon_metadata(id_: str=None):
    """
    fetch metadata for mon <id>
    :param id: CephString who=None req=false {}
    module=mon perm=r flags=
    """
    prefix = 'mon metadata'
    _args = {'prefix': prefix, 'id': id_} 

def mon_ok_to_add_offline():
    """
    check whether adding a mon and not starting it would break quorum

    module=mon perm=r flags=
    """
    prefix = 'mon ok-to-add-offline'
    _args = {'prefix': prefix, } 

def mon_ok_to_rm(id_: str):
    """
    check whether removing the specified mon would break quorum
    :param id: CephString who=None req=True {}
    module=mon perm=r flags=
    """
    prefix = 'mon ok-to-rm'
    _args = {'prefix': prefix, 'id': id_} 

def mon_ok_to_stop(ids: List[str]):
    """
    check whether mon(s) can be safely stopped without reducing immediate availability
    :param ids: CephString who=None req=True {}
    module=mon perm=r flags=
    """
    prefix = 'mon ok-to-stop'
    _args = {'prefix': prefix, 'ids': ids} 

def mon_remove(name: str):
    """
    remove monitor named <name>
    :param name: CephString who=None req=True {}
    module=mon perm=rw flags=deprecated
    """
    prefix = 'mon remove'
    _args = {'prefix': prefix, 'name': name} 

def mon_rm(name: str):
    """
    remove monitor named <name>
    :param name: CephString who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'mon rm'
    _args = {'prefix': prefix, 'name': name} 

def mon_scrub():
    """
    scrub the monitor stores

    module=mon perm=rw flags=
    """
    prefix = 'mon scrub'
    _args = {'prefix': prefix, } 

def mon_set_addrs(name: str, addrs: str):
    """
    set the addrs (IPs and ports) a specific monitor binds to
    :param name: CephString who=None req=True {}
    :param addrs: CephString who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'mon set-addrs'
    _args = {'prefix': prefix, 'name': name, 'addrs': addrs} 

def mon_set_rank(name: str, rank: int):
    """
    set the rank for the specified mon
    :param name: CephString who=None req=True {}
    :param rank: CephInt who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'mon set-rank'
    _args = {'prefix': prefix, 'name': name, 'rank': rank} 

def mon_set_weight(name: str, weight: int):
    """
    set the weight for the specified mon
    :param name: CephString who=None req=True {}
    :param weight: CephInt who=None req=True {u'range': u'0|65535'}
    module=mon perm=rw flags=
    """
    prefix = 'mon set-weight'
    _args = {'prefix': prefix, 'name': name, 'weight': weight} 

def mon_stat():
    """
    summarize monitor status

    module=mon perm=r flags=
    """
    prefix = 'mon stat'
    _args = {'prefix': prefix, } 

def mon_sync_force(yes_i_really_mean_it: bool=None, i_know_what_i_am_doing: bool=None):
    """
    force sync of and clear monitor store
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    :param i_know_what_i_am_doing: CephBool who=None req=false {}
    module=mon perm=rw flags=no_forward
    """
    prefix = 'mon sync force'
    _args = {'prefix': prefix, 'yes_i_really_mean_it': yes_i_really_mean_it, 'i_know_what_i_am_doing': i_know_what_i_am_doing} 

def mon_versions():
    """
    check running versions of monitors

    module=mon perm=r flags=
    """
    prefix = 'mon versions'
    _args = {'prefix': prefix, } 

def mon_status():
    """
    report status of monitors

    module=mon perm=r flags=no_forward
    """
    prefix = 'mon_status'
    _args = {'prefix': prefix, } 

def node_ls(type: str=None):
    """
    list all nodes in cluster [type]
    :param type: CephChoices who=None req=false {u'strings': u'all|osd|mon|mds|mgr'}
    module=mon perm=r flags=
    """
    prefix = 'node ls'
    _args = {'prefix': prefix, 'type': type} 

def orchestrator_device_ls(host: List[str]=None, format: str=None, refresh: bool=None):
    """
    List devices on a node
    :param host: CephString who=None req=false {}
    :param format: CephChoices who=None req=false {u'strings': u'json|plain'}
    :param refresh: CephBool who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'orchestrator device ls'
    _args = {'prefix': prefix, 'host': host, 'format': format, 'refresh': refresh} 

def orchestrator_host_add(host: str):
    """
    Add a host
    :param host: CephString who=None req=true {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator host add'
    _args = {'prefix': prefix, 'host': host} 

def orchestrator_host_ls():
    """
    List hosts

    module=mgr perm=r flags=mgr
    """
    prefix = 'orchestrator host ls'
    _args = {'prefix': prefix, } 

def orchestrator_host_rm(host: str):
    """
    Remove a host
    :param host: CephString who=None req=true {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator host rm'
    _args = {'prefix': prefix, 'host': host} 

def orchestrator_mds_add(svc_arg: str):
    """
    Create an MDS service
    :param svc_arg: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator mds add'
    _args = {'prefix': prefix, 'svc_arg': svc_arg} 

def orchestrator_mds_rm(svc_id: str):
    """
    Remove an MDS service
    :param svc_id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator mds rm'
    _args = {'prefix': prefix, 'svc_id': svc_id} 

def orchestrator_mgr_update(num: int, hosts: List[str]=None):
    """
    Update the number of manager instances
    :param num: CephInt who=None req=true {}
    :param hosts: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator mgr update'
    _args = {'prefix': prefix, 'num': num, 'hosts': hosts} 

def orchestrator_mon_update(num: int, hosts: List[str]=None):
    """
    Update the number of monitor instances
    :param num: CephInt who=None req=true {}
    :param hosts: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator mon update'
    _args = {'prefix': prefix, 'num': num, 'hosts': hosts} 

def orchestrator_nfs_add(svc_arg: str, pool: str, namespace: str=None):
    """
    Create an NFS service
    :param svc_arg: CephString who=None req=True {}
    :param pool: CephString who=None req=True {}
    :param namespace: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator nfs add'
    _args = {'prefix': prefix, 'svc_arg': svc_arg, 'pool': pool, 'namespace': namespace} 

def orchestrator_nfs_rm(svc_id: str):
    """
    Remove an NFS service
    :param svc_id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator nfs rm'
    _args = {'prefix': prefix, 'svc_id': svc_id} 

def orchestrator_nfs_update(svc_id: str, num: int):
    """
    Scale an NFS service
    :param svc_id: CephString who=None req=True {}
    :param num: CephInt who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator nfs update'
    _args = {'prefix': prefix, 'svc_id': svc_id, 'num': num} 

def orchestrator_osd_create(svc_arg: str=None):
    """
    Create an OSD service. Either --svc_arg=host:drives or -i <drive_group>
    :param svc_arg: CephString who=None req=false {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator osd create'
    _args = {'prefix': prefix, 'svc_arg': svc_arg} 

def orchestrator_osd_rm(svc_id: List[str]):
    """
    Remove OSD services
    :param svc_id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator osd rm'
    _args = {'prefix': prefix, 'svc_id': svc_id} 

def orchestrator_rgw_add(svc_arg: str):
    """
    Create an RGW service
    :param svc_arg: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator rgw add'
    _args = {'prefix': prefix, 'svc_arg': svc_arg} 

def orchestrator_rgw_rm(svc_id: str):
    """
    Remove an RGW service
    :param svc_id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator rgw rm'
    _args = {'prefix': prefix, 'svc_id': svc_id} 

def orchestrator_service(action: str, svc_type: str, svc_name: str):
    """
    Start, stop or reload an entire service (i.e. all daemons)
    :param action: CephChoices who=None req=True {u'strings': u'start|stop|reload'}
    :param svc_type: CephString who=None req=True {}
    :param svc_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator service'
    _args = {'prefix': prefix, 'action': action, 'svc_type': svc_type, 'svc_name': svc_name} 

def orchestrator_service_ls(host: str=None, svc_type: str=None, svc_id: str=None, format: str=None):
    """
    List services known to orchestrator
    :param host: CephString who=None req=false {}
    :param svc_type: CephChoices who=None req=false {u'strings': u'mon|mgr|osd|mds|nfs|rgw|rbd-mirror'}
    :param svc_id: CephString who=None req=false {}
    :param format: CephChoices who=None req=false {u'strings': u'json|plain'}
    module=mgr perm=r flags=mgr
    """
    prefix = 'orchestrator service ls'
    _args = {'prefix': prefix, 'host': host, 'svc_type': svc_type, 'svc_id': svc_id, 'format': format} 

def orchestrator_service_instance(action: str, svc_type: str, svc_id: str):
    """
    Start, stop or reload a specific service instance
    :param action: CephChoices who=None req=True {u'strings': u'start|stop|reload'}
    :param svc_type: CephString who=None req=True {}
    :param svc_id: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator service-instance'
    _args = {'prefix': prefix, 'action': action, 'svc_type': svc_type, 'svc_id': svc_id} 

def orchestrator_set_backend(module_name: str):
    """
    Select orchestrator module backend
    :param module_name: CephString who=None req=true {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'orchestrator set backend'
    _args = {'prefix': prefix, 'module_name': module_name} 

def orchestrator_status():
    """
    Report configured backend and its status

    module=mgr perm=r flags=mgr
    """
    prefix = 'orchestrator status'
    _args = {'prefix': prefix, } 

def osd_add_nodown(ids: List[str]):
    """
    mark osd(s) <id> [<id>...] as nodown, or use <all|any> to mark all osds as nodown
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd add-nodown'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_add_noin(ids: List[str]):
    """
    mark osd(s) <id> [<id>...] as noin, or use <all|any> to mark all osds as noin
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd add-noin'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_add_noout(ids: List[str]):
    """
    mark osd(s) <id> [<id>...] as noout, or use <all|any> to mark all osds as noout
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd add-noout'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_add_noup(ids: List[str]):
    """
    mark osd(s) <id> [<id>...] as noup, or use <all|any> to mark all osds as noup
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd add-noup'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_blacklist(blacklistop: str, addr: str, expire: float=None):
    """
    add (optionally until <expire> seconds from now) or remove <addr> from blacklist
    :param blacklistop: CephChoices who=None req=True {u'strings': u'add|rm'}
    :param addr: CephEntityAddr who=None req=True {}
    :param expire: CephFloat who=None req=false {u'range': u'0.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd blacklist'
    _args = {'prefix': prefix, 'blacklistop': blacklistop, 'addr': addr, 'expire': expire} 

def osd_blacklist_clear():
    """
    clear all blacklisted clients

    module=osd perm=rw flags=
    """
    prefix = 'osd blacklist clear'
    _args = {'prefix': prefix, } 

def osd_blacklist_ls():
    """
    show blacklisted clients

    module=osd perm=r flags=
    """
    prefix = 'osd blacklist ls'
    _args = {'prefix': prefix, } 

def osd_blocked_by():
    """
    print histogram of which OSDs are blocking their peers

    module=osd perm=r flags=mgr
    """
    prefix = 'osd blocked-by'
    _args = {'prefix': prefix, } 

def osd_count_metadata(property: str):
    """
    count OSDs by metadata field property
    :param property: CephString who=None req=True {}
    module=osd perm=r flags=
    """
    prefix = 'osd count-metadata'
    _args = {'prefix': prefix, 'property': property} 

def osd_create(uuid: str=None, id_: str=None):
    """
    create new osd (with optional UUID and ID)
    :param uuid: CephUUID who=None req=false {}
    :param id: CephOsdName who=None req=false {}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd create'
    _args = {'prefix': prefix, 'uuid': uuid, 'id': id_} 

def osd_crush_add(id_: str, weight: float, args: List[str]):
    """
    add or update crushmap position and weight for <name> with <weight> and location <args>
    :param id: CephOsdName who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    :param args: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush add'
    _args = {'prefix': prefix, 'id': id_, 'weight': weight, 'args': args} 

def osd_crush_add_bucket(name: str, type: str, args: List[str]=None):
    """
    add no-parent (probably root) crush bucket <name> of type <type> to location <args>
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param type: CephString who=None req=True {}
    :param args: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush add-bucket'
    _args = {'prefix': prefix, 'name': name, 'type': type, 'args': args} 

def osd_crush_class_create(class_: str):
    """
    create crush device class <class>
    :param class: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush class create'
    _args = {'prefix': prefix, 'class': class_} 

def osd_crush_class_ls():
    """
    list all crush device classes

    module=osd perm=r flags=
    """
    prefix = 'osd crush class ls'
    _args = {'prefix': prefix, } 

def osd_crush_class_ls_osd(class_: str):
    """
    list all osds belonging to the specific <class>
    :param class: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_]'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush class ls-osd'
    _args = {'prefix': prefix, 'class': class_} 

def osd_crush_class_rename(srcname: str, dstname: str):
    """
    rename crush device class <srcname> to <dstname>
    :param srcname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_]'}
    :param dstname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush class rename'
    _args = {'prefix': prefix, 'srcname': srcname, 'dstname': dstname} 

def osd_crush_class_rm(class_: str):
    """
    remove crush device class <class>
    :param class: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush class rm'
    _args = {'prefix': prefix, 'class': class_} 

def osd_crush_create_or_move(id_: str, weight: float, args: List[str]):
    """
    create entry or move existing entry for <name> <weight> at/to location <args>
    :param id: CephOsdName who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    :param args: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush create-or-move'
    _args = {'prefix': prefix, 'id': id_, 'weight': weight, 'args': args} 

def osd_crush_dump():
    """
    dump crush map

    module=osd perm=r flags=
    """
    prefix = 'osd crush dump'
    _args = {'prefix': prefix, } 

def osd_crush_get_device_class(ids: List[str]):
    """
    get classes of specified osd(s) <id> [<id>...]
    :param ids: CephString who=None req=True {}
    module=osd perm=r flags=
    """
    prefix = 'osd crush get-device-class'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_crush_get_tunable(tunable: str):
    """
    get crush tunable <tunable>
    :param tunable: CephChoices who=None req=True {u'strings': u'straw_calc_version'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush get-tunable'
    _args = {'prefix': prefix, 'tunable': tunable} 

def osd_crush_link(name: str, args: List[str]):
    """
    link existing entry for <name> under location <args>
    :param name: CephString who=None req=True {}
    :param args: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush link'
    _args = {'prefix': prefix, 'name': name, 'args': args} 

def osd_crush_ls(node: str):
    """
    list items beneath a node in the CRUSH tree
    :param node: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush ls'
    _args = {'prefix': prefix, 'node': node} 

def osd_crush_move(name: str, args: List[str]):
    """
    move existing entry for <name> to location <args>
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param args: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush move'
    _args = {'prefix': prefix, 'name': name, 'args': args} 

def osd_crush_remove(name: str, ancestor: str=None):
    """
    remove <name> from crush map (everywhere, or just at <ancestor>)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param ancestor: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd crush remove'
    _args = {'prefix': prefix, 'name': name, 'ancestor': ancestor} 

def osd_crush_rename_bucket(srcname: str, dstname: str):
    """
    rename bucket <srcname> to <dstname>
    :param srcname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param dstname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rename-bucket'
    _args = {'prefix': prefix, 'srcname': srcname, 'dstname': dstname} 

def osd_crush_reweight(name: str, weight: float):
    """
    change <name>'s weight to <weight> in crush map
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush reweight'
    _args = {'prefix': prefix, 'name': name, 'weight': weight} 

def osd_crush_reweight_all():
    """
    recalculate the weights for the tree to ensure they sum correctly

    module=osd perm=rw flags=
    """
    prefix = 'osd crush reweight-all'
    _args = {'prefix': prefix, } 

def osd_crush_reweight_subtree(name: str, weight: float):
    """
    change all leaf items beneath <name> to <weight> in crush map
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush reweight-subtree'
    _args = {'prefix': prefix, 'name': name, 'weight': weight} 

def osd_crush_rm(name: str, ancestor: str=None):
    """
    remove <name> from crush map (everywhere, or just at <ancestor>)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param ancestor: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rm'
    _args = {'prefix': prefix, 'name': name, 'ancestor': ancestor} 

def osd_crush_rm_device_class(ids: List[str]):
    """
    remove class of the osd(s) <id> [<id>...],or use <all|any> to remove all.
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rm-device-class'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_crush_rule_create_erasure(name: str, profile: str=None):
    """
    create crush rule <name> for erasure coded pool created with <profile> (default default)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param profile: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rule create-erasure'
    _args = {'prefix': prefix, 'name': name, 'profile': profile} 

def osd_crush_rule_create_replicated(name: str, root: str, type: str, class_: str=None):
    """
    create crush rule <name> for replicated pool to start from <root>, replicate across buckets of type <type>, use devices of type <class> (ssd or hdd)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param root: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param type: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param class: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rule create-replicated'
    _args = {'prefix': prefix, 'name': name, 'root': root, 'type': type, 'class': class_} 

def osd_crush_rule_create_simple(name: str, root: str, type: str, mode: str=None):
    """
    create crush rule <name> to start from <root>, replicate across buckets of type <type>, using a choose mode of <firstn|indep> (default firstn; indep best for erasure pools)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param root: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param type: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param mode: CephChoices who=None req=false {u'strings': u'firstn|indep'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rule create-simple'
    _args = {'prefix': prefix, 'name': name, 'root': root, 'type': type, 'mode': mode} 

def osd_crush_rule_dump(name: str=None):
    """
    dump crush rule <name> (default all)
    :param name: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush rule dump'
    _args = {'prefix': prefix, 'name': name} 

def osd_crush_rule_list():
    """
    list crush rules

    module=osd perm=r flags=deprecated
    """
    prefix = 'osd crush rule list'
    _args = {'prefix': prefix, } 

def osd_crush_rule_ls():
    """
    list crush rules

    module=osd perm=r flags=
    """
    prefix = 'osd crush rule ls'
    _args = {'prefix': prefix, } 

def osd_crush_rule_ls_by_class(class_: str):
    """
    list all crush rules that reference the same <class>
    :param class: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush rule ls-by-class'
    _args = {'prefix': prefix, 'class': class_} 

def osd_crush_rule_rename(srcname: str, dstname: str):
    """
    rename crush rule <srcname> to <dstname>
    :param srcname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param dstname: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rule rename'
    _args = {'prefix': prefix, 'srcname': srcname, 'dstname': dstname} 

def osd_crush_rule_rm(name: str):
    """
    remove crush rule <name>
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush rule rm'
    _args = {'prefix': prefix, 'name': name} 

def osd_crush_set(prior_version: int=None):
    """
    set crush map from input file
    :param prior_version: CephInt who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush set'
    _args = {'prefix': prefix, 'prior_version': prior_version} 

def osd_crush_set(id_: str, weight: float, args: List[str]):
    """
    update crushmap position and weight for <name> to <weight> with location <args>
    :param id: CephOsdName who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    :param args: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush set'
    _args = {'prefix': prefix, 'id': id_, 'weight': weight, 'args': args} 

def osd_crush_set_all_straw_buckets_to_straw2():
    """
    convert all CRUSH current straw buckets to use the straw2 algorithm

    module=osd perm=rw flags=
    """
    prefix = 'osd crush set-all-straw-buckets-to-straw2'
    _args = {'prefix': prefix, } 

def osd_crush_set_device_class(class_: str, ids: List[str]):
    """
    set the <class> of the osd(s) <id> [<id>...],or use <all|any> to set all.
    :param class: CephString who=None req=True {}
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush set-device-class'
    _args = {'prefix': prefix, 'class': class_, 'ids': ids} 

def osd_crush_set_tunable(tunable: str, value: int):
    """
    set crush tunable <tunable> to <value>
    :param tunable: CephChoices who=None req=True {u'strings': u'straw_calc_version'}
    :param value: CephInt who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush set-tunable'
    _args = {'prefix': prefix, 'tunable': tunable, 'value': value} 

def osd_crush_show_tunables():
    """
    show current crush tunables

    module=osd perm=r flags=
    """
    prefix = 'osd crush show-tunables'
    _args = {'prefix': prefix, } 

def osd_crush_swap_bucket(source: str, dest: str, yes_i_really_mean_it: bool=None):
    """
    swap existing bucket contents from (orphan) bucket <source> and <target>
    :param source: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param dest: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush swap-bucket'
    _args = {'prefix': prefix, 'source': source, 'dest': dest, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_crush_tree(shadow: str=None):
    """
    dump crush buckets and items in a tree view
    :param shadow: CephChoices who=None req=false {u'strings': u'--show-shadow'}
    module=osd perm=r flags=
    """
    prefix = 'osd crush tree'
    _args = {'prefix': prefix, 'shadow': shadow} 

def osd_crush_tunables(profile: str):
    """
    set crush tunables values to <profile>
    :param profile: CephChoices who=None req=True {u'strings': u'legacy|argonaut|bobtail|firefly|hammer|jewel|optimal|default'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush tunables'
    _args = {'prefix': prefix, 'profile': profile} 

def osd_crush_unlink(name: str, ancestor: str=None):
    """
    unlink <name> from crush map (everywhere, or just at <ancestor>)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param ancestor: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush unlink'
    _args = {'prefix': prefix, 'name': name, 'ancestor': ancestor} 

def osd_crush_weight_set_create(pool: str, mode: str):
    """
    create a weight-set for a given pool
    :param pool: CephPoolname who=None req=True {}
    :param mode: CephChoices who=None req=True {u'strings': u'flat|positional'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set create'
    _args = {'prefix': prefix, 'pool': pool, 'mode': mode} 

def osd_crush_weight_set_create_compat():
    """
    create a default backward-compatible weight-set

    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set create-compat'
    _args = {'prefix': prefix, } 

def osd_crush_weight_set_dump():
    """
    dump crush weight sets

    module=osd perm=r flags=
    """
    prefix = 'osd crush weight-set dump'
    _args = {'prefix': prefix, } 

def osd_crush_weight_set_ls():
    """
    list crush weight sets

    module=osd perm=r flags=
    """
    prefix = 'osd crush weight-set ls'
    _args = {'prefix': prefix, } 

def osd_crush_weight_set_reweight(pool: str, item: str, weight: List[float]):
    """
    set weight for an item (bucket or osd) in a pool's weight-set
    :param pool: CephPoolname who=None req=True {}
    :param item: CephString who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set reweight'
    _args = {'prefix': prefix, 'pool': pool, 'item': item, 'weight': weight} 

def osd_crush_weight_set_reweight_compat(item: str, weight: List[float]):
    """
    set weight for an item (bucket or osd) in the backward-compatible weight-set
    :param item: CephString who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set reweight-compat'
    _args = {'prefix': prefix, 'item': item, 'weight': weight} 

def osd_crush_weight_set_rm(pool: str):
    """
    remove the weight-set for a given pool
    :param pool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set rm'
    _args = {'prefix': prefix, 'pool': pool} 

def osd_crush_weight_set_rm_compat():
    """
    remove the backward-compatible weight-set

    module=osd perm=rw flags=
    """
    prefix = 'osd crush weight-set rm-compat'
    _args = {'prefix': prefix, } 

def osd_deep_scrub(who: str):
    """
    initiate deep scrub on osd <who>, or use <all|any> to deep scrub all
    :param who: CephString who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd deep-scrub'
    _args = {'prefix': prefix, 'who': who} 

def osd_destroy(id_: str, force: bool=None, yes_i_really_mean_it: bool=None):
    """
    mark osd as being destroyed. Keeps the ID intact (allowing reuse), but removes cephx keys, config-key data and lockbox keys, rendering data permanently unreadable.
    :param id: CephOsdName who=None req=True {}
    :param force: CephBool who=None req=false {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd destroy'
    _args = {'prefix': prefix, 'id': id_, 'force': force, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_destroy_actual(id_: str, yes_i_really_mean_it: bool=None):
    """
    mark osd as being destroyed. Keeps the ID intact (allowing reuse), but removes cephx keys, config-key data and lockbox keys, rendering data permanently unreadable.
    :param id: CephOsdName who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=hidden
    """
    prefix = 'osd destroy-actual'
    _args = {'prefix': prefix, 'id': id_, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_df(output_method: str=None, filter_by: str=None, filter: str=None):
    """
    show OSD utilization
    :param output_method: CephChoices who=None req=false {u'strings': u'plain|tree'}
    :param filter_by: CephChoices who=None req=false {u'strings': u'class|name'}
    :param filter: CephString who=None req=false {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd df'
    _args = {'prefix': prefix, 'output_method': output_method, 'filter_by': filter_by, 'filter': filter} 

def osd_down(ids: List[str]):
    """
    set osd(s) <id> [<id>...] down, or use <any|all> to set all osds down
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd down'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_dump(epoch: int=None):
    """
    print summary of OSD map
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=osd perm=r flags=
    """
    prefix = 'osd dump'
    _args = {'prefix': prefix, 'epoch': epoch} 

def osd_erasure_code_profile_get(name: str):
    """
    get erasure code profile <name>
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=r flags=
    """
    prefix = 'osd erasure-code-profile get'
    _args = {'prefix': prefix, 'name': name} 

def osd_erasure_code_profile_ls():
    """
    list all erasure code profiles

    module=osd perm=r flags=
    """
    prefix = 'osd erasure-code-profile ls'
    _args = {'prefix': prefix, } 

def osd_erasure_code_profile_rm(name: str):
    """
    remove erasure code profile <name>
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd erasure-code-profile rm'
    _args = {'prefix': prefix, 'name': name} 

def osd_erasure_code_profile_set(name: str, profile: List[str]=None, force: bool=None):
    """
    create erasure code profile <name> with [<key[=value]> ...] pairs. Add a --force at the end to override an existing profile (VERY DANGEROUS)
    :param name: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param profile: CephString who=None req=false {}
    :param force: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd erasure-code-profile set'
    _args = {'prefix': prefix, 'name': name, 'profile': profile, 'force': force} 

def osd_find(id_: str):
    """
    find osd <id> in the CRUSH map and show its location
    :param id: CephOsdName who=None req=True {}
    module=osd perm=r flags=
    """
    prefix = 'osd find'
    _args = {'prefix': prefix, 'id': id_} 

def osd_force_create_pg(pgid: str, yes_i_really_mean_it: bool=None):
    """
    force creation of pg <pgid>
    :param pgid: CephPgid who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd force-create-pg'
    _args = {'prefix': prefix, 'pgid': pgid, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_get_require_min_compat_client():
    """
    get the minimum client version we will maintain compatibility with

    module=osd perm=r flags=
    """
    prefix = 'osd get-require-min-compat-client'
    _args = {'prefix': prefix, } 

def osd_getcrushmap(epoch: int=None):
    """
    get CRUSH map
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=osd perm=r flags=
    """
    prefix = 'osd getcrushmap'
    _args = {'prefix': prefix, 'epoch': epoch} 

def osd_getmap(epoch: int=None):
    """
    get OSD map
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=osd perm=r flags=
    """
    prefix = 'osd getmap'
    _args = {'prefix': prefix, 'epoch': epoch} 

def osd_getmaxosd():
    """
    show largest OSD id

    module=osd perm=r flags=
    """
    prefix = 'osd getmaxosd'
    _args = {'prefix': prefix, } 

def osd_in(ids: List[str]):
    """
    set osd(s) <id> [<id>...] in, can use <any|all> to automatically set all previously out osds in
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd in'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_last_stat_seq(id_: str):
    """
    get the last pg stats sequence number reported for this osd
    :param id: CephOsdName who=None req=True {}
    module=osd perm=r flags=
    """
    prefix = 'osd last-stat-seq'
    _args = {'prefix': prefix, 'id': id_} 

def osd_lost(id_: str, yes_i_really_mean_it: bool=None):
    """
    mark osd as permanently lost. THIS DESTROYS DATA IF NO MORE REPLICAS EXIST, BE CAREFUL
    :param id: CephOsdName who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd lost'
    _args = {'prefix': prefix, 'id': id_, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_ls(epoch: int=None):
    """
    show all OSD ids
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    module=osd perm=r flags=
    """
    prefix = 'osd ls'
    _args = {'prefix': prefix, 'epoch': epoch} 

def osd_ls_tree(epoch: int=None, name: str):
    """
    show OSD ids under bucket <name> in the CRUSH map
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    :param name: CephString who=None req=true {}
    module=osd perm=r flags=
    """
    prefix = 'osd ls-tree'
    _args = {'prefix': prefix, 'epoch': epoch, 'name': name} 

def osd_lspools():
    """
    list pools

    module=osd perm=r flags=deprecated
    """
    prefix = 'osd lspools'
    _args = {'prefix': prefix, } 

def osd_map(pool: str, object: str, nspace: str=None):
    """
    find pg for <object> in <pool> with [namespace]
    :param pool: CephPoolname who=None req=True {}
    :param object: CephObjectname who=None req=True {}
    :param nspace: CephString who=None req=false {}
    module=osd perm=r flags=
    """
    prefix = 'osd map'
    _args = {'prefix': prefix, 'pool': pool, 'object': object, 'nspace': nspace} 

def osd_metadata(id_: str=None):
    """
    fetch metadata for osd {id} (default all)
    :param id: CephOsdName who=None req=false {}
    module=osd perm=r flags=
    """
    prefix = 'osd metadata'
    _args = {'prefix': prefix, 'id': id_} 

def osd_new(uuid: str, id_: str=None):
    """
    Create a new OSD. If supplied, the `id` to be replaced needs to exist and have been previously destroyed. Reads secrets from JSON file via `-i <file>` (see man page).
    :param uuid: CephUUID who=None req=true {}
    :param id: CephOsdName who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd new'
    _args = {'prefix': prefix, 'uuid': uuid, 'id': id_} 

def osd_numa_status():
    """
    show NUMA status of OSDs

    module=osd perm=r flags=
    """
    prefix = 'osd numa-status'
    _args = {'prefix': prefix, } 

def osd_ok_to_stop(ids: List[str]):
    """
    check whether osd(s) can be safely stopped without reducing immediate data availability
    :param ids: CephString who=None req=True {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd ok-to-stop'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_out(ids: List[str]):
    """
    set osd(s) <id> [<id>...] out, or use <any|all> to set all osds out
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd out'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_pause():
    """
    pause osd

    module=osd perm=rw flags=
    """
    prefix = 'osd pause'
    _args = {'prefix': prefix, } 

def osd_perf():
    """
    print dump of OSD perf summary stats

    module=osd perm=r flags=mgr
    """
    prefix = 'osd perf'
    _args = {'prefix': prefix, } 

def osd_perf_counters_get(query_id: int):
    """
    fetch osd perf counters
    :param query_id: CephInt who=None req=true {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'osd perf counters get'
    _args = {'prefix': prefix, 'query_id': query_id} 

def osd_perf_query_add(query: str):
    """
    add osd perf query
    :param query: CephChoices who=None req=True {u'strings': u'client_id|rbd_image_id|all_subkeys'}
    module=mgr perm=w flags=mgr
    """
    prefix = 'osd perf query add'
    _args = {'prefix': prefix, 'query': query} 

def osd_perf_query_remove(query_id: int):
    """
    remove osd perf query
    :param query_id: CephInt who=None req=true {}
    module=mgr perm=w flags=mgr
    """
    prefix = 'osd perf query remove'
    _args = {'prefix': prefix, 'query_id': query_id} 

def osd_pg_temp(pgid: str, id_: List[str]=None):
    """
    set pg_temp mapping pgid:[<id> [<id>...]] (developers only)
    :param pgid: CephPgid who=None req=True {}
    :param id: CephOsdName who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pg-temp'
    _args = {'prefix': prefix, 'pgid': pgid, 'id': id_} 

def osd_pg_upmap(pgid: str, id_: List[str]):
    """
    set pg_upmap mapping <pgid>:[<id> [<id>...]] (developers only)
    :param pgid: CephPgid who=None req=True {}
    :param id: CephOsdName who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pg-upmap'
    _args = {'prefix': prefix, 'pgid': pgid, 'id': id_} 

def osd_pg_upmap_items(pgid: str, id_: List[str]):
    """
    set pg_upmap_items mapping <pgid>:{<id> to <id>, [...]} (developers only)
    :param pgid: CephPgid who=None req=True {}
    :param id: CephOsdName who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pg-upmap-items'
    _args = {'prefix': prefix, 'pgid': pgid, 'id': id_} 

def osd_pool_application_disable(pool: str, app: str, yes_i_really_mean_it: bool=None):
    """
    disables use of an application <app> on pool <poolname>
    :param pool: CephPoolname who=None req=True {}
    :param app: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool application disable'
    _args = {'prefix': prefix, 'pool': pool, 'app': app, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_pool_application_enable(pool: str, app: str, yes_i_really_mean_it: bool=None):
    """
    enable use of an application <app> [cephfs,rbd,rgw] on pool <poolname>
    :param pool: CephPoolname who=None req=True {}
    :param app: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool application enable'
    _args = {'prefix': prefix, 'pool': pool, 'app': app, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_pool_application_get(pool: str, app: str=None, key: str=None):
    """
    get value of key <key> of application <app> on pool <poolname>
    :param pool: CephPoolname who=None req=fasle {}
    :param app: CephString who=None req=false {}
    :param key: CephString who=None req=false {}
    module=osd perm=r flags=
    """
    prefix = 'osd pool application get'
    _args = {'prefix': prefix, 'pool': pool, 'app': app, 'key': key} 

def osd_pool_application_rm(pool: str, app: str, key: str):
    """
    removes application <app> metadata key <key> on pool <poolname>
    :param pool: CephPoolname who=None req=True {}
    :param app: CephString who=None req=True {}
    :param key: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool application rm'
    _args = {'prefix': prefix, 'pool': pool, 'app': app, 'key': key} 

def osd_pool_application_set(pool: str, app: str, key: str, value: str):
    """
    sets application <app> metadata key <key> to <value> on pool <poolname>
    :param pool: CephPoolname who=None req=True {}
    :param app: CephString who=None req=True {}
    :param key: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param value: CephString who=None req=True {u'goodchars': u'[A-Za-z0-9-_.=]'}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool application set'
    _args = {'prefix': prefix, 'pool': pool, 'app': app, 'key': key, 'value': value} 

def osd_pool_autoscale_status():
    """
    report on pool pg_num sizing recommendation and intent

    module=mgr perm=r flags=mgr
    """
    prefix = 'osd pool autoscale-status'
    _args = {'prefix': prefix, } 

def osd_pool_cancel_force_backfill(who: List[str]):
    """
    restore normal recovery priority of specified pool <who>
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool cancel-force-backfill'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_cancel_force_recovery(who: List[str]):
    """
    restore normal recovery priority of specified pool <who>
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool cancel-force-recovery'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_create(pool: str, pg_num: int, pgp_num: int=None, pool_type: str=None, erasure_code_profile: str=None, rule: str=None, expected_num_objects: int=None, size: int=None, pg_num_min: int=None, target_size_bytes: int=None, target_size_ratio: float=None):
    """
    create pool
    :param pool: CephPoolname who=None req=True {}
    :param pg_num: CephInt who=None req=True {u'range': u'0'}
    :param pgp_num: CephInt who=None req=false {u'range': u'0'}
    :param pool_type: CephChoices who=None req=false {u'strings': u'replicated|erasure'}
    :param erasure_code_profile: CephString who=None req=false {u'goodchars': u'[A-Za-z0-9-_.]'}
    :param rule: CephString who=None req=false {}
    :param expected_num_objects: CephInt who=None req=false {}
    :param size: CephInt who=None req=false {}
    :param pg_num_min: CephInt who=None req=false {u'range': u'0'}
    :param target_size_bytes: CephInt who=None req=false {u'range': u'0'}
    :param target_size_ratio: CephFloat who=None req=false {u'range': u'0|1'}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool create'
    _args = {'prefix': prefix, 'pool': pool, 'pg_num': pg_num, 'pgp_num': pgp_num, 'pool_type': pool_type, 'erasure_code_profile': erasure_code_profile, 'rule': rule, 'expected_num_objects': expected_num_objects, 'size': size, 'pg_num_min': pg_num_min, 'target_size_bytes': target_size_bytes, 'target_size_ratio': target_size_ratio} 

def osd_pool_deep_scrub(who: List[str]):
    """
    initiate deep-scrub on pool <who>
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool deep-scrub'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_delete(pool: str, pool2: str=None, yes_i_really_really_mean_it: bool=None, yes_i_really_really_mean_it_not_faking: bool=None):
    """
    delete pool
    :param pool: CephPoolname who=None req=True {}
    :param pool2: CephPoolname who=None req=false {}
    :param yes_i_really_really_mean_it: CephBool who=None req=false {}
    :param yes_i_really_really_mean_it_not_faking: CephBool who=None req=false {}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd pool delete'
    _args = {'prefix': prefix, 'pool': pool, 'pool2': pool2, 'yes_i_really_really_mean_it': yes_i_really_really_mean_it, 'yes_i_really_really_mean_it_not_faking': yes_i_really_really_mean_it_not_faking} 

def osd_pool_force_backfill(who: List[str]):
    """
    force backfill of specified pool <who> first
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool force-backfill'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_force_recovery(who: List[str]):
    """
    force recovery of specified pool <who> first
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool force-recovery'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_get(pool: str, var: str):
    """
    get pool parameter <var>
    :param pool: CephPoolname who=None req=True {}
    :param var: CephChoices who=None req=True {u'strings': u'size|min_size|pg_num|pgp_num|crush_rule|hashpspool|nodelete|nopgchange|nosizechange|write_fadvise_dontneed|noscrub|nodeep-scrub|hit_set_type|hit_set_period|hit_set_count|hit_set_fpp|use_gmt_hitset|target_max_objects|target_max_bytes|cache_target_dirty_ratio|cache_target_dirty_high_ratio|cache_target_full_ratio|cache_min_flush_age|cache_min_evict_age|erasure_code_profile|min_read_recency_for_promote|all|min_write_recency_for_promote|fast_read|hit_set_grade_decay_rate|hit_set_search_last_n|scrub_min_interval|scrub_max_interval|deep_scrub_interval|recovery_priority|recovery_op_priority|scrub_priority|compression_mode|compression_algorithm|compression_required_ratio|compression_max_blob_size|compression_min_blob_size|csum_type|csum_min_block|csum_max_block|allow_ec_overwrites|fingerprint_algorithm|pg_autoscale_mode|pg_autoscale_bias|pg_num_min|target_size_bytes|target_size_ratio'}
    module=osd perm=r flags=
    """
    prefix = 'osd pool get'
    _args = {'prefix': prefix, 'pool': pool, 'var': var} 

def osd_pool_get_quota(pool: str):
    """
    obtain object or byte limits for pool
    :param pool: CephPoolname who=None req=True {}
    module=osd perm=r flags=
    """
    prefix = 'osd pool get-quota'
    _args = {'prefix': prefix, 'pool': pool} 

def osd_pool_ls(detail: str=None):
    """
    list pools
    :param detail: CephChoices who=None req=false {u'strings': u'detail'}
    module=osd perm=r flags=
    """
    prefix = 'osd pool ls'
    _args = {'prefix': prefix, 'detail': detail} 

def osd_pool_mksnap(pool: str, snap: str):
    """
    make snapshot <snap> in <pool>
    :param pool: CephPoolname who=None req=True {}
    :param snap: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool mksnap'
    _args = {'prefix': prefix, 'pool': pool, 'snap': snap} 

def osd_pool_rename(srcpool: str, destpool: str):
    """
    rename <srcpool> to <destpool>
    :param srcpool: CephPoolname who=None req=True {}
    :param destpool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool rename'
    _args = {'prefix': prefix, 'srcpool': srcpool, 'destpool': destpool} 

def osd_pool_repair(who: List[str]):
    """
    initiate repair on pool <who>
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool repair'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_rm(pool: str, pool2: str=None, yes_i_really_really_mean_it: bool=None, yes_i_really_really_mean_it_not_faking: bool=None):
    """
    remove pool
    :param pool: CephPoolname who=None req=True {}
    :param pool2: CephPoolname who=None req=false {}
    :param yes_i_really_really_mean_it: CephBool who=None req=false {}
    :param yes_i_really_really_mean_it_not_faking: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool rm'
    _args = {'prefix': prefix, 'pool': pool, 'pool2': pool2, 'yes_i_really_really_mean_it': yes_i_really_really_mean_it, 'yes_i_really_really_mean_it_not_faking': yes_i_really_really_mean_it_not_faking} 

def osd_pool_rmsnap(pool: str, snap: str):
    """
    remove snapshot <snap> from <pool>
    :param pool: CephPoolname who=None req=True {}
    :param snap: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool rmsnap'
    _args = {'prefix': prefix, 'pool': pool, 'snap': snap} 

def osd_pool_scrub(who: List[str]):
    """
    initiate scrub on pool <who>
    :param who: CephPoolname who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd pool scrub'
    _args = {'prefix': prefix, 'who': who} 

def osd_pool_set(pool: str, var: str, val: str, yes_i_really_mean_it: bool=None):
    """
    set pool parameter <var> to <val>
    :param pool: CephPoolname who=None req=True {}
    :param var: CephChoices who=None req=True {u'strings': u'size|min_size|pg_num|pgp_num|pgp_num_actual|crush_rule|hashpspool|nodelete|nopgchange|nosizechange|write_fadvise_dontneed|noscrub|nodeep-scrub|hit_set_type|hit_set_period|hit_set_count|hit_set_fpp|use_gmt_hitset|target_max_bytes|target_max_objects|cache_target_dirty_ratio|cache_target_dirty_high_ratio|cache_target_full_ratio|cache_min_flush_age|cache_min_evict_age|min_read_recency_for_promote|min_write_recency_for_promote|fast_read|hit_set_grade_decay_rate|hit_set_search_last_n|scrub_min_interval|scrub_max_interval|deep_scrub_interval|recovery_priority|recovery_op_priority|scrub_priority|compression_mode|compression_algorithm|compression_required_ratio|compression_max_blob_size|compression_min_blob_size|csum_type|csum_min_block|csum_max_block|allow_ec_overwrites|fingerprint_algorithm|pg_autoscale_mode|pg_autoscale_bias|pg_num_min|target_size_bytes|target_size_ratio'}
    :param val: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool set'
    _args = {'prefix': prefix, 'pool': pool, 'var': var, 'val': val, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_pool_set_quota(pool: str, field: str, val: str):
    """
    set object or byte limit on pool
    :param pool: CephPoolname who=None req=True {}
    :param field: CephChoices who=None req=True {u'strings': u'max_objects|max_bytes'}
    :param val: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd pool set-quota'
    _args = {'prefix': prefix, 'pool': pool, 'field': field, 'val': val} 

def osd_pool_stats(pool_name: str=None):
    """
    obtain stats from all pools, or from specified pool
    :param pool_name: CephPoolname who=None req=false {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd pool stats'
    _args = {'prefix': prefix, 'pool_name': pool_name} 

def osd_primary_affinity(id_: str, weight: float):
    """
    adjust osd primary-affinity from 0.0 <= <weight> <= 1.0
    :param id: CephOsdName who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0|1.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd primary-affinity'
    _args = {'prefix': prefix, 'id': id_, 'weight': weight} 

def osd_primary_temp(pgid: str, id_: str):
    """
    set primary_temp mapping pgid:<id>|-1 (developers only)
    :param pgid: CephPgid who=None req=True {}
    :param id: CephOsdName who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd primary-temp'
    _args = {'prefix': prefix, 'pgid': pgid, 'id': id_} 

def osd_purge(id_: str, force: bool=None, yes_i_really_mean_it: bool=None):
    """
    purge all osd data from the monitors including the OSD id and CRUSH position
    :param id: CephOsdName who=None req=True {}
    :param force: CephBool who=None req=false {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd purge'
    _args = {'prefix': prefix, 'id': id_, 'force': force, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_purge_actual(id_: str, yes_i_really_mean_it: bool=None):
    """
    purge all osd data from the monitors. Combines `osd destroy`, `osd rm`, and `osd crush rm`.
    :param id: CephOsdName who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=hidden
    """
    prefix = 'osd purge-actual'
    _args = {'prefix': prefix, 'id': id_, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_purge_new(id_: str, yes_i_really_mean_it: bool=None):
    """
    purge all traces of an OSD that was partially created but never started
    :param id: CephOsdName who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd purge-new'
    _args = {'prefix': prefix, 'id': id_, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_repair(who: str):
    """
    initiate repair on osd <who>, or use <all|any> to repair all
    :param who: CephString who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd repair'
    _args = {'prefix': prefix, 'who': who} 

def osd_require_osd_release(release: str, yes_i_really_mean_it: bool=None):
    """
    set the minimum allowed OSD release to participate in the cluster
    :param release: CephChoices who=None req=True {u'strings': u'luminous|mimic|nautilus|octopus'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd require-osd-release'
    _args = {'prefix': prefix, 'release': release, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_reweight(id_: str, weight: float):
    """
    reweight osd to 0.0 < <weight> < 1.0
    :param id: CephOsdName who=None req=True {}
    :param weight: CephFloat who=None req=True {u'range': u'0.0|1.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd reweight'
    _args = {'prefix': prefix, 'id': id_, 'weight': weight} 

def osd_reweight_by_pg(oload: int=None, max_change: float=None, max_osds: int=None, pools: List[str]=None):
    """
    reweight OSDs by PG distribution [overload-percentage-for-consideration, default 120]
    :param oload: CephInt who=None req=false {}
    :param max_change: CephFloat who=None req=false {}
    :param max_osds: CephInt who=None req=false {}
    :param pools: CephPoolname who=None req=false {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd reweight-by-pg'
    _args = {'prefix': prefix, 'oload': oload, 'max_change': max_change, 'max_osds': max_osds, 'pools': pools} 

def osd_reweight_by_utilization(oload: int=None, max_change: float=None, max_osds: int=None, no_increasing: str=None):
    """
    reweight OSDs by utilization [overload-percentage-for-consideration, default 120]
    :param oload: CephInt who=None req=false {}
    :param max_change: CephFloat who=None req=false {}
    :param max_osds: CephInt who=None req=false {}
    :param no_increasing: CephChoices who=None req=false {u'strings': u'--no-increasing'}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd reweight-by-utilization'
    _args = {'prefix': prefix, 'oload': oload, 'max_change': max_change, 'max_osds': max_osds, 'no_increasing': no_increasing} 

def osd_reweightn(weights: str):
    """
    reweight osds with {<id>: <weight>,...})
    :param weights: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd reweightn'
    _args = {'prefix': prefix, 'weights': weights} 

def osd_rm(ids: List[str]):
    """
    remove osd(s) <id> [<id>...], or use <any|all> to remove all osds
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd rm'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_rm_nodown(ids: List[str]):
    """
    allow osd(s) <id> [<id>...] to be marked down (if they are currently marked as nodown), can use <all|any> to automatically filter out all nodown osds
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-nodown'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_rm_noin(ids: List[str]):
    """
    allow osd(s) <id> [<id>...] to be marked in (if they are currently marked as noin), can use <all|any> to automatically filter out all noin osds
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-noin'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_rm_noout(ids: List[str]):
    """
    allow osd(s) <id> [<id>...] to be marked out (if they are currently marked as noout), can use <all|any> to automatically filter out all noout osds
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-noout'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_rm_noup(ids: List[str]):
    """
    allow osd(s) <id> [<id>...] to be marked up (if they are currently marked as noup), can use <all|any> to automatically filter out all noup osds
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-noup'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_rm_pg_upmap(pgid: str):
    """
    clear pg_upmap mapping for <pgid> (developers only)
    :param pgid: CephPgid who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-pg-upmap'
    _args = {'prefix': prefix, 'pgid': pgid} 

def osd_rm_pg_upmap_items(pgid: str):
    """
    clear pg_upmap_items mapping for <pgid> (developers only)
    :param pgid: CephPgid who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd rm-pg-upmap-items'
    _args = {'prefix': prefix, 'pgid': pgid} 

def osd_safe_to_destroy(ids: List[str]):
    """
    check whether osd(s) can be safely destroyed without reducing data durability
    :param ids: CephString who=None req=True {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd safe-to-destroy'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_scrub(who: str):
    """
    initiate scrub on osd <who>, or use <all|any> to scrub all
    :param who: CephString who=None req=True {}
    module=osd perm=rw flags=mgr
    """
    prefix = 'osd scrub'
    _args = {'prefix': prefix, 'who': who} 

def osd_set(key: str, yes_i_really_mean_it: bool=None):
    """
    set <key>
    :param key: CephChoices who=None req=True {u'strings': u'full|pause|noup|nodown|noout|noin|nobackfill|norebalance|norecover|noscrub|nodeep-scrub|notieragent|nosnaptrim|pglog_hardlimit'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd set'
    _args = {'prefix': prefix, 'key': key, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_set_backfillfull_ratio(ratio: float):
    """
    set usage ratio at which OSDs are marked too full to backfill
    :param ratio: CephFloat who=None req=True {u'range': u'0.0|1.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd set-backfillfull-ratio'
    _args = {'prefix': prefix, 'ratio': ratio} 

def osd_set_full_ratio(ratio: float):
    """
    set usage ratio at which OSDs are marked full
    :param ratio: CephFloat who=None req=True {u'range': u'0.0|1.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd set-full-ratio'
    _args = {'prefix': prefix, 'ratio': ratio} 

def osd_set_nearfull_ratio(ratio: float):
    """
    set usage ratio at which OSDs are marked near-full
    :param ratio: CephFloat who=None req=True {u'range': u'0.0|1.0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd set-nearfull-ratio'
    _args = {'prefix': prefix, 'ratio': ratio} 

def osd_set_require_min_compat_client(version: str, yes_i_really_mean_it: bool=None):
    """
    set the minimum client version we will maintain compatibility with
    :param version: CephString who=None req=True {}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd set-require-min-compat-client'
    _args = {'prefix': prefix, 'version': version, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_setcrushmap(prior_version: int=None):
    """
    set crush map from input file
    :param prior_version: CephInt who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd setcrushmap'
    _args = {'prefix': prefix, 'prior_version': prior_version} 

def osd_setmaxosd(newmax: int):
    """
    set new maximum osd value
    :param newmax: CephInt who=None req=True {u'range': u'0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd setmaxosd'
    _args = {'prefix': prefix, 'newmax': newmax} 

def osd_stat():
    """
    print summary of OSD map

    module=osd perm=r flags=
    """
    prefix = 'osd stat'
    _args = {'prefix': prefix, } 

def osd_status(bucket: str=None):
    """
    Show the status of OSDs within a bucket, or all
    :param bucket: CephString who=None req=false {}
    module=mgr perm=r flags=mgr
    """
    prefix = 'osd status'
    _args = {'prefix': prefix, 'bucket': bucket} 

def osd_stop(ids: List[str]):
    """
    stop the corresponding osd daemons and mark them as down
    :param ids: CephString who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd stop'
    _args = {'prefix': prefix, 'ids': ids} 

def osd_test_reweight_by_pg(oload: int=None, max_change: float=None, max_osds: int=None, pools: List[str]=None):
    """
    dry run of reweight OSDs by PG distribution [overload-percentage-for-consideration, default 120]
    :param oload: CephInt who=None req=false {}
    :param max_change: CephFloat who=None req=false {}
    :param max_osds: CephInt who=None req=false {}
    :param pools: CephPoolname who=None req=false {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd test-reweight-by-pg'
    _args = {'prefix': prefix, 'oload': oload, 'max_change': max_change, 'max_osds': max_osds, 'pools': pools} 

def osd_test_reweight_by_utilization(oload: int=None, max_change: float=None, max_osds: int=None, no_increasing: bool=None):
    """
    dry run of reweight OSDs by utilization [overload-percentage-for-consideration, default 120]
    :param oload: CephInt who=None req=false {}
    :param max_change: CephFloat who=None req=false {}
    :param max_osds: CephInt who=None req=false {}
    :param no_increasing: CephBool who=None req=false {}
    module=osd perm=r flags=mgr
    """
    prefix = 'osd test-reweight-by-utilization'
    _args = {'prefix': prefix, 'oload': oload, 'max_change': max_change, 'max_osds': max_osds, 'no_increasing': no_increasing} 

def osd_tier_add(pool: str, tierpool: str, force_nonempty: str=None):
    """
    add the tier <tierpool> (the second one) to base pool <pool> (the first one)
    :param pool: CephPoolname who=None req=True {}
    :param tierpool: CephPoolname who=None req=True {}
    :param force_nonempty: CephChoices who=None req=false {u'strings': u'--force-nonempty'}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier add'
    _args = {'prefix': prefix, 'pool': pool, 'tierpool': tierpool, 'force_nonempty': force_nonempty} 

def osd_tier_add_cache(pool: str, tierpool: str, size: int):
    """
    add a cache <tierpool> (the second one) of size <size> to existing pool <pool> (the first one)
    :param pool: CephPoolname who=None req=True {}
    :param tierpool: CephPoolname who=None req=True {}
    :param size: CephInt who=None req=True {u'range': u'0'}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier add-cache'
    _args = {'prefix': prefix, 'pool': pool, 'tierpool': tierpool, 'size': size} 

def osd_tier_cache_mode(pool: str, mode: str, yes_i_really_mean_it: bool=None):
    """
    specify the caching mode for cache tier <pool>
    :param pool: CephPoolname who=None req=True {}
    :param mode: CephChoices who=None req=True {u'strings': u'none|writeback|forward|readonly|readforward|proxy|readproxy'}
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier cache-mode'
    _args = {'prefix': prefix, 'pool': pool, 'mode': mode, 'yes_i_really_mean_it': yes_i_really_mean_it} 

def osd_tier_remove(pool: str, tierpool: str):
    """
    remove the tier <tierpool> (the second one) from base pool <pool> (the first one)
    :param pool: CephPoolname who=None req=True {}
    :param tierpool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd tier remove'
    _args = {'prefix': prefix, 'pool': pool, 'tierpool': tierpool} 

def osd_tier_remove_overlay(pool: str):
    """
    remove the overlay pool for base pool <pool>
    :param pool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=deprecated
    """
    prefix = 'osd tier remove-overlay'
    _args = {'prefix': prefix, 'pool': pool} 

def osd_tier_rm(pool: str, tierpool: str):
    """
    remove the tier <tierpool> (the second one) from base pool <pool> (the first one)
    :param pool: CephPoolname who=None req=True {}
    :param tierpool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier rm'
    _args = {'prefix': prefix, 'pool': pool, 'tierpool': tierpool} 

def osd_tier_rm_overlay(pool: str):
    """
    remove the overlay pool for base pool <pool>
    :param pool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier rm-overlay'
    _args = {'prefix': prefix, 'pool': pool} 

def osd_tier_set_overlay(pool: str, overlaypool: str):
    """
    set the overlay pool for base pool <pool> to be <overlaypool>
    :param pool: CephPoolname who=None req=True {}
    :param overlaypool: CephPoolname who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'osd tier set-overlay'
    _args = {'prefix': prefix, 'pool': pool, 'overlaypool': overlaypool} 

def osd_tree(epoch: int=None, states: List[str]=None):
    """
    print OSD tree
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    :param states: CephChoices who=None req=false {u'strings': u'up|down|in|out|destroyed'}
    module=osd perm=r flags=
    """
    prefix = 'osd tree'
    _args = {'prefix': prefix, 'epoch': epoch, 'states': states} 

def osd_tree_from(epoch: int=None, bucket: str, states: List[str]=None):
    """
    print OSD tree in bucket
    :param epoch: CephInt who=None req=false {u'range': u'0'}
    :param bucket: CephString who=None req=True {}
    :param states: CephChoices who=None req=false {u'strings': u'up|down|in|out|destroyed'}
    module=osd perm=r flags=
    """
    prefix = 'osd tree-from'
    _args = {'prefix': prefix, 'epoch': epoch, 'bucket': bucket, 'states': states} 

def osd_unpause():
    """
    unpause osd

    module=osd perm=rw flags=
    """
    prefix = 'osd unpause'
    _args = {'prefix': prefix, } 

def osd_unset(key: str):
    """
    unset <key>
    :param key: CephChoices who=None req=True {u'strings': u'full|pause|noup|nodown|noout|noin|nobackfill|norebalance|norecover|noscrub|nodeep-scrub|notieragent|nosnaptrim'}
    module=osd perm=rw flags=
    """
    prefix = 'osd unset'
    _args = {'prefix': prefix, 'key': key} 

def osd_utilization():
    """
    get basic pg distribution stats

    module=osd perm=r flags=
    """
    prefix = 'osd utilization'
    _args = {'prefix': prefix, } 

def osd_versions():
    """
    check running versions of OSDs

    module=osd perm=r flags=
    """
    prefix = 'osd versions'
    _args = {'prefix': prefix, } 

def pg_cancel_force_backfill(pgid: List[str]):
    """
    restore normal backfill priority of <pgid>
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg cancel-force-backfill'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_cancel_force_recovery(pgid: List[str]):
    """
    restore normal recovery priority of <pgid>
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg cancel-force-recovery'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_debug(debugop: str):
    """
    show debug info about pgs
    :param debugop: CephChoices who=None req=True {u'strings': u'unfound_objects_exist|degraded_pgs_exist'}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg debug'
    _args = {'prefix': prefix, 'debugop': debugop} 

def pg_deep_scrub(pgid: str):
    """
    start deep-scrub on <pgid>
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg deep-scrub'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_dump(dumpcontents: List[str]=None):
    """
    show human-readable versions of pg map (only 'all' valid with plain)
    :param dumpcontents: CephChoices who=None req=false {u'strings': u'all|summary|sum|delta|pools|osds|pgs|pgs_brief'}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg dump'
    _args = {'prefix': prefix, 'dumpcontents': dumpcontents} 

def pg_dump_json(dumpcontents: List[str]=None):
    """
    show human-readable version of pg map in json only
    :param dumpcontents: CephChoices who=None req=false {u'strings': u'all|summary|sum|pools|osds|pgs'}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg dump_json'
    _args = {'prefix': prefix, 'dumpcontents': dumpcontents} 

def pg_dump_pools_json():
    """
    show pg pools info in json only

    module=pg perm=r flags=mgr
    """
    prefix = 'pg dump_pools_json'
    _args = {'prefix': prefix, } 

def pg_dump_stuck(stuckops: List[str]=None, threshold: int=None):
    """
    show information about stuck pgs
    :param stuckops: CephChoices who=None req=false {u'strings': u'inactive|unclean|stale|undersized|degraded'}
    :param threshold: CephInt who=None req=false {}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg dump_stuck'
    _args = {'prefix': prefix, 'stuckops': stuckops, 'threshold': threshold} 

def pg_force_backfill(pgid: List[str]):
    """
    force backfill of <pgid> first
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg force-backfill'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_force_recovery(pgid: List[str]):
    """
    force recovery of <pgid> first
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg force-recovery'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_getmap():
    """
    get binary pg map to -o/stdout

    module=pg perm=r flags=mgr
    """
    prefix = 'pg getmap'
    _args = {'prefix': prefix, } 

def pg_ls(pool: int=None, states: List[str]=None):
    """
    list pg with specific pool, osd, state
    :param pool: CephInt who=None req=false {}
    :param states: CephString who=None req=false {}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg ls'
    _args = {'prefix': prefix, 'pool': pool, 'states': states} 

def pg_ls_by_osd(osd: str, pool: int=None, states: List[str]=None):
    """
    list pg on osd [osd]
    :param osd: CephOsdName who=None req=True {}
    :param pool: CephInt who=None req=false {}
    :param states: CephString who=None req=false {}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg ls-by-osd'
    _args = {'prefix': prefix, 'osd': osd, 'pool': pool, 'states': states} 

def pg_ls_by_pool(poolstr: str, states: List[str]=None):
    """
    list pg with pool = [poolname]
    :param poolstr: CephString who=None req=True {}
    :param states: CephString who=None req=false {}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg ls-by-pool'
    _args = {'prefix': prefix, 'poolstr': poolstr, 'states': states} 

def pg_ls_by_primary(osd: str, pool: int=None, states: List[str]=None):
    """
    list pg with primary = [osd]
    :param osd: CephOsdName who=None req=True {}
    :param pool: CephInt who=None req=false {}
    :param states: CephString who=None req=false {}
    module=pg perm=r flags=mgr
    """
    prefix = 'pg ls-by-primary'
    _args = {'prefix': prefix, 'osd': osd, 'pool': pool, 'states': states} 

def pg_map(pgid: str):
    """
    show mapping of pg to osds
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=r flags=
    """
    prefix = 'pg map'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_repair(pgid: str):
    """
    start repair on <pgid>
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg repair'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_repeer(pgid: str):
    """
    force a PG to repeer
    :param pgid: CephPgid who=None req=True {}
    module=osd perm=rw flags=
    """
    prefix = 'pg repeer'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_scrub(pgid: str):
    """
    start scrub on <pgid>
    :param pgid: CephPgid who=None req=True {}
    module=pg perm=rw flags=mgr
    """
    prefix = 'pg scrub'
    _args = {'prefix': prefix, 'pgid': pgid} 

def pg_stat():
    """
    show placement group status.

    module=pg perm=r flags=mgr
    """
    prefix = 'pg stat'
    _args = {'prefix': prefix, } 

def progress():
    """
    Show progress of recovery operations

    module=mgr perm=r flags=mgr
    """
    prefix = 'progress'
    _args = {'prefix': prefix, } 

def progress_clear():
    """
    Reset progress tracking

    module=mgr perm=rw flags=mgr
    """
    prefix = 'progress clear'
    _args = {'prefix': prefix, } 

def progress_json():
    """
    Show machine readable progress information

    module=mgr perm=r flags=mgr
    """
    prefix = 'progress json'
    _args = {'prefix': prefix, } 

def prometheus_file_sd_config():
    """
    Return file_sd compatible prometheus config for mgr cluster

    module=mgr perm=r flags=mgr
    """
    prefix = 'prometheus file_sd_config'
    _args = {'prefix': prefix, } 

def quorum(quorumcmd: str):
    """
    enter or exit quorum
    :param quorumcmd: CephChoices who=None req=True {u'strings': u'enter|exit'}
    module=mon perm=rw flags=
    """
    prefix = 'quorum'
    _args = {'prefix': prefix, 'quorumcmd': quorumcmd} 

def quorum_status():
    """
    report status of monitor quorum

    module=mon perm=r flags=
    """
    prefix = 'quorum_status'
    _args = {'prefix': prefix, } 

def rbd_perf_image_counters(pool_spec: str=None, sort_by: str=None):
    """
    Retrieve current RBD IO performance counters
    :param pool_spec: CephString who=None req=false {}
    :param sort_by: CephChoices who=None req=false {u'strings': u'write_ops|write_bytes|write_latency|read_ops|read_bytes|read_latency'}
    module=mgr perm=r flags=mgr
    """
    prefix = 'rbd perf image counters'
    _args = {'prefix': prefix, 'pool_spec': pool_spec, 'sort_by': sort_by} 

def rbd_perf_image_stats(pool_spec: str=None, sort_by: str=None):
    """
    Retrieve current RBD IO performance stats
    :param pool_spec: CephString who=None req=false {}
    :param sort_by: CephChoices who=None req=false {u'strings': u'write_ops|write_bytes|write_latency|read_ops|read_bytes|read_latency'}
    module=mgr perm=r flags=mgr
    """
    prefix = 'rbd perf image stats'
    _args = {'prefix': prefix, 'pool_spec': pool_spec, 'sort_by': sort_by} 

def report(tags: List[str]=None):
    """
    report full status of cluster, optional title tag strings
    :param tags: CephString who=None req=false {}
    module=mon perm=r flags=
    """
    prefix = 'report'
    _args = {'prefix': prefix, 'tags': tags} 

def restful_create_key(key_name: str):
    """
    Create an API key with this name
    :param key_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'restful create-key'
    _args = {'prefix': prefix, 'key_name': key_name} 

def restful_create_self_signed_cert():
    """
    Create localized self signed certificate

    module=mgr perm=rw flags=mgr
    """
    prefix = 'restful create-self-signed-cert'
    _args = {'prefix': prefix, } 

def restful_delete_key(key_name: str):
    """
    Delete an API key with this name
    :param key_name: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'restful delete-key'
    _args = {'prefix': prefix, 'key_name': key_name} 

def restful_list_keys():
    """
    List all API keys

    module=mgr perm=r flags=mgr
    """
    prefix = 'restful list-keys'
    _args = {'prefix': prefix, } 

def restful_restart():
    """
    Restart API server

    module=mgr perm=rw flags=mgr
    """
    prefix = 'restful restart'
    _args = {'prefix': prefix, } 

def scrub():
    """
    scrub the monitor stores

    module=mon perm=rw flags=deprecated
    """
    prefix = 'scrub'
    _args = {'prefix': prefix, } 

def service_dump():
    """
    dump service map

    module=service perm=r flags=mgr
    """
    prefix = 'service dump'
    _args = {'prefix': prefix, } 

def service_status():
    """
    dump service state

    module=service perm=r flags=mgr
    """
    prefix = 'service status'
    _args = {'prefix': prefix, } 

def smart(devid: str=None):
    """
    Query health metrics for underlying device
    :param devid: CephString who=None req=false {}
    module=mon perm=rw flags=hidden
    """
    prefix = 'smart'
    _args = {'prefix': prefix, 'devid': devid} 

def ssh_clear_ssh_config():
    """
    Clear the ssh_config file

    module=mgr perm=rw flags=mgr
    """
    prefix = 'ssh clear-ssh-config'
    _args = {'prefix': prefix, } 

def ssh_set_ssh_config():
    """
    Set the ssh_config file (use -i <ssh_config>)

    module=mgr perm=rw flags=mgr
    """
    prefix = 'ssh set-ssh-config'
    _args = {'prefix': prefix, } 

def status():
    """
    show cluster status

    module=mon perm=r flags=
    """
    prefix = 'status'
    _args = {'prefix': prefix, } 

def sync_force(yes_i_really_mean_it: bool=None, i_know_what_i_am_doing: bool=None):
    """
    force sync of and clear monitor store
    :param yes_i_really_mean_it: CephBool who=None req=false {}
    :param i_know_what_i_am_doing: CephBool who=None req=false {}
    module=mon perm=rw flags=deprecated, no_forward
    """
    prefix = 'sync force'
    _args = {'prefix': prefix, 'yes_i_really_mean_it': yes_i_really_mean_it, 'i_know_what_i_am_doing': i_know_what_i_am_doing} 

def telegraf_config_set(key: str, value: str):
    """
    Set a configuration value
    :param key: CephString who=None req=True {}
    :param value: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'telegraf config-set'
    _args = {'prefix': prefix, 'key': key, 'value': value} 

def telegraf_config_show():
    """
    Show current configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'telegraf config-show'
    _args = {'prefix': prefix, } 

def telegraf_send():
    """
    Force sending data to Telegraf

    module=mgr perm=rw flags=mgr
    """
    prefix = 'telegraf send'
    _args = {'prefix': prefix, } 

def telemetry_off():
    """
    Disable telemetry reports from this cluster

    module=mgr perm=rw flags=mgr
    """
    prefix = 'telemetry off'
    _args = {'prefix': prefix, } 

def telemetry_on():
    """
    Enable telemetry reports from this cluster

    module=mgr perm=rw flags=mgr
    """
    prefix = 'telemetry on'
    _args = {'prefix': prefix, } 

def telemetry_send():
    """
    Force sending data to Ceph telemetry

    module=mgr perm=rw flags=mgr
    """
    prefix = 'telemetry send'
    _args = {'prefix': prefix, } 

def telemetry_show():
    """
    Show last report or report to be sent

    module=mgr perm=r flags=mgr
    """
    prefix = 'telemetry show'
    _args = {'prefix': prefix, } 

def telemetry_status():
    """
    Show current configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'telemetry status'
    _args = {'prefix': prefix, } 

def tell(target: str, args: List[str]):
    """
    send a command to a specific daemon
    :param target: CephName who=None req=True {}
    :param args: CephString who=None req=True {}
    module=mon perm=rw flags=
    """
    prefix = 'tell'
    _args = {'prefix': prefix, 'target': target, 'args': args} 

def time_sync_status():
    """
    show time sync status

    module=mon perm=r flags=
    """
    prefix = 'time-sync-status'
    _args = {'prefix': prefix, } 

def version():
    """
    show mon daemon version

    module=mon perm=r flags=no_forward
    """
    prefix = 'version'
    _args = {'prefix': prefix, } 

def versions():
    """
    check running versions of ceph daemons

    module=mon perm=r flags=
    """
    prefix = 'versions'
    _args = {'prefix': prefix, } 

def zabbix_config_set(key: str, value: str):
    """
    Set a configuration value
    :param key: CephString who=None req=True {}
    :param value: CephString who=None req=True {}
    module=mgr perm=rw flags=mgr
    """
    prefix = 'zabbix config-set'
    _args = {'prefix': prefix, 'key': key, 'value': value} 

def zabbix_config_show():
    """
    Show current configuration

    module=mgr perm=r flags=mgr
    """
    prefix = 'zabbix config-show'
    _args = {'prefix': prefix, } 

def zabbix_discovery():
    """
    Discovering Zabbix data

    module=mgr perm=r flags=mgr
    """
    prefix = 'zabbix discovery'
    _args = {'prefix': prefix, } 

def zabbix_send():
    """
    Force sending data to Zabbix

    module=mgr perm=rw flags=mgr
    """
    prefix = 'zabbix send'
    _args = {'prefix': prefix, } 

