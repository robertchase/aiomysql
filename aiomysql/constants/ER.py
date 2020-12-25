"""error codes"""
# pylint: disable=invalid-name
ERROR_FIRST = 1000
HASHCHK = 1000
NISAMCHK = 1001
NO = 1002
YES = 1003
CANT_CREATE_FILE = 1004
CANT_CREATE_TABLE = 1005
CANT_CREATE_DB = 1006
DB_CREATE_EXISTS = 1007
DB_DROP_EXISTS = 1008
DB_DROP_DELETE = 1009
DB_DROP_RMDIR = 1010
CANT_DELETE_FILE = 1011
CANT_FIND_SYSTEM_REC = 1012
CANT_GET_STAT = 1013
CANT_GET_WD = 1014
CANT_LOCK = 1015
CANT_OPEN_FILE = 1016
FILE_NOT_FOUND = 1017
CANT_READ_DIR = 1018
CANT_SET_WD = 1019
CHECKREAD = 1020
DISK_FULL = 1021
DUP_KEY = 1022
ERROR_ON_CLOSE = 1023
ERROR_ON_READ = 1024
ERROR_ON_RENAME = 1025
ERROR_ON_WRITE = 1026
FILE_USED = 1027
FILSORT_ABORT = 1028
FORM_NOT_FOUND = 1029
GET_ERRNO = 1030
ILLEGAL_HA = 1031
KEY_NOT_FOUND = 1032
NOT_FORM_FILE = 1033
NOT_KEYFILE = 1034
OLD_KEYFILE = 1035
OPEN_AS_READONLY = 1036
OUTOFMEMORY = 1037
OUT_OF_SORTMEMORY = 1038
UNEXPECTED_EOF = 1039
CON_COUNT_ERROR = 1040
OUT_OF_RESOURCES = 1041
BAD_HOST_ERROR = 1042
HANDSHAKE_ERROR = 1043
DBACCESS_DENIED_ERROR = 1044
ACCESS_DENIED_ERROR = 1045
NO_DB_ERROR = 1046
UNKNOWN_COM_ERROR = 1047
BAD_NULL_ERROR = 1048
BAD_DB_ERROR = 1049
TABLE_EXISTS_ERROR = 1050
BAD_TABLE_ERROR = 1051
NON_UNIQ_ERROR = 1052
SERVER_SHUTDOWN = 1053
BAD_FIELD_ERROR = 1054
WRONG_FIELD_WITH_GROUP = 1055
WRONG_GROUP_FIELD = 1056
WRONG_SUM_SELECT = 1057
WRONG_VALUE_COUNT = 1058
TOO_LONG_IDENT = 1059
DUP_FIELDNAME = 1060
DUP_KEYNAME = 1061
DUP_ENTRY = 1062
WRONG_FIELD_SPEC = 1063
PARSE_ERROR = 1064
EMPTY_QUERY = 1065
NONUNIQ_TABLE = 1066
INVALID_DEFAULT = 1067
MULTIPLE_PRI_KEY = 1068
TOO_MANY_KEYS = 1069
TOO_MANY_KEY_PARTS = 1070
TOO_LONG_KEY = 1071
KEY_COLUMN_DOES_NOT_EXITS = 1072
BLOB_USED_AS_KEY = 1073
TOO_BIG_FIELDLENGTH = 1074
WRONG_AUTO_KEY = 1075
READY = 1076
NORMAL_SHUTDOWN = 1077
GOT_SIGNAL = 1078
SHUTDOWN_COMPLETE = 1079
FORCING_CLOSE = 1080
IPSOCK_ERROR = 1081
NO_SUCH_INDEX = 1082
WRONG_FIELD_TERMINATORS = 1083
BLOBS_AND_NO_TERMINATED = 1084
TEXTFILE_NOT_READABLE = 1085
FILE_EXISTS_ERROR = 1086
LOAD_INFO = 1087
ALTER_INFO = 1088
WRONG_SUB_KEY = 1089
CANT_REMOVE_ALL_FIELDS = 1090
CANT_DROP_FIELD_OR_KEY = 1091
INSERT_INFO = 1092
UPDATE_TABLE_USED = 1093
NO_SUCH_THREAD = 1094
KILL_DENIED_ERROR = 1095
NO_TABLES_USED = 1096
TOO_BIG_SET = 1097
NO_UNIQUE_LOGFILE = 1098
TABLE_NOT_LOCKED_FOR_WRITE = 1099
TABLE_NOT_LOCKED = 1100
BLOB_CANT_HAVE_DEFAULT = 1101
WRONG_DB_NAME = 1102
WRONG_TABLE_NAME = 1103
TOO_BIG_SELECT = 1104
UNKNOWN_ERROR = 1105
UNKNOWN_PROCEDURE = 1106
WRONG_PARAMCOUNT_TO_PROCEDURE = 1107
WRONG_PARAMETERS_TO_PROCEDURE = 1108
UNKNOWN_TABLE = 1109
FIELD_SPECIFIED_TWICE = 1110
INVALID_GROUP_FUNC_USE = 1111
UNSUPPORTED_EXTENSION = 1112
TABLE_MUST_HAVE_COLUMNS = 1113
RECORD_FILE_FULL = 1114
UNKNOWN_CHARACTER_SET = 1115
TOO_MANY_TABLES = 1116
TOO_MANY_FIELDS = 1117
TOO_BIG_ROWSIZE = 1118
STACK_OVERRUN = 1119
WRONG_OUTER_JOIN = 1120
NULL_COLUMN_IN_INDEX = 1121
CANT_FIND_UDF = 1122
CANT_INITIALIZE_UDF = 1123
UDF_NO_PATHS = 1124
UDF_EXISTS = 1125
CANT_OPEN_LIBRARY = 1126
CANT_FIND_DL_ENTRY = 1127
FUNCTION_NOT_DEFINED = 1128
HOST_IS_BLOCKED = 1129
HOST_NOT_PRIVILEGED = 1130
PASSWORD_ANONYMOUS_USER = 1131
PASSWORD_NOT_ALLOWED = 1132
PASSWORD_NO_MATCH = 1133
UPDATE_INFO = 1134
CANT_CREATE_THREAD = 1135
WRONG_VALUE_COUNT_ON_ROW = 1136
CANT_REOPEN_TABLE = 1137
INVALID_USE_OF_NULL = 1138
REGEXP_ERROR = 1139
MIX_OF_GROUP_FUNC_AND_FIELDS = 1140
NONEXISTING_GRANT = 1141
TABLEACCESS_DENIED_ERROR = 1142
COLUMNACCESS_DENIED_ERROR = 1143
ILLEGAL_GRANT_FOR_TABLE = 1144
GRANT_WRONG_HOST_OR_USER = 1145
NO_SUCH_TABLE = 1146
NONEXISTING_TABLE_GRANT = 1147
NOT_ALLOWED_COMMAND = 1148
SYNTAX_ERROR = 1149
DELAYED_CANT_CHANGE_LOCK = 1150
TOO_MANY_DELAYED_THREADS = 1151
ABORTING_CONNECTION = 1152
NET_PACKET_TOO_LARGE = 1153
NET_READ_ERROR_FROM_PIPE = 1154
NET_FCNTL_ERROR = 1155
NET_PACKETS_OUT_OF_ORDER = 1156
NET_UNCOMPRESS_ERROR = 1157
NET_READ_ERROR = 1158
NET_READ_INTERRUPTED = 1159
NET_ERROR_ON_WRITE = 1160
NET_WRITE_INTERRUPTED = 1161
TOO_LONG_STRING = 1162
TABLE_CANT_HANDLE_BLOB = 1163
TABLE_CANT_HANDLE_AUTO_INCREMENT = 1164
DELAYED_INSERT_TABLE_LOCKED = 1165
WRONG_COLUMN_NAME = 1166
WRONG_KEY_COLUMN = 1167
WRONG_MRG_TABLE = 1168
DUP_UNIQUE = 1169
BLOB_KEY_WITHOUT_LENGTH = 1170
PRIMARY_CANT_HAVE_NULL = 1171
TOO_MANY_ROWS = 1172
REQUIRES_PRIMARY_KEY = 1173
NO_RAID_COMPILED = 1174
UPDATE_WITHOUT_KEY_IN_SAFE_MODE = 1175
KEY_DOES_NOT_EXITS = 1176
CHECK_NO_SUCH_TABLE = 1177
CHECK_NOT_IMPLEMENTED = 1178
CANT_DO_THIS_DURING_AN_TRANSACTION = 1179
ERROR_DURING_COMMIT = 1180
ERROR_DURING_ROLLBACK = 1181
ERROR_DURING_FLUSH_LOGS = 1182
ERROR_DURING_CHECKPOINT = 1183
NEW_ABORTING_CONNECTION = 1184
DUMP_NOT_IMPLEMENTED = 1185
FLUSH_MASTER_BINLOG_CLOSED = 1186
INDEX_REBUILD = 1187
MASTER = 1188
MASTER_NET_READ = 1189
MASTER_NET_WRITE = 1190
FT_MATCHING_KEY_NOT_FOUND = 1191
LOCK_OR_ACTIVE_TRANSACTION = 1192
UNKNOWN_SYSTEM_VARIABLE = 1193
CRASHED_ON_USAGE = 1194
CRASHED_ON_REPAIR = 1195
WARNING_NOT_COMPLETE_ROLLBACK = 1196
TRANS_CACHE_FULL = 1197
SLAVE_MUST_STOP = 1198
SLAVE_NOT_RUNNING = 1199
BAD_SLAVE = 1200
MASTER_INFO = 1201
SLAVE_THREAD = 1202
TOO_MANY_USER_CONNECTIONS = 1203
SET_CONSTANTS_ONLY = 1204
LOCK_WAIT_TIMEOUT = 1205
LOCK_TABLE_FULL = 1206
READ_ONLY_TRANSACTION = 1207
DROP_DB_WITH_READ_LOCK = 1208
CREATE_DB_WITH_READ_LOCK = 1209
WRONG_ARGUMENTS = 1210
NO_PERMISSION_TO_CREATE_USER = 1211
UNION_TABLES_IN_DIFFERENT_DIR = 1212
LOCK_DEADLOCK = 1213
TABLE_CANT_HANDLE_FT = 1214
CANNOT_ADD_FOREIGN = 1215
NO_REFERENCED_ROW = 1216
ROW_IS_REFERENCED = 1217
CONNECT_TO_MASTER = 1218
QUERY_ON_MASTER = 1219
ERROR_WHEN_EXECUTING_COMMAND = 1220
WRONG_USAGE = 1221
WRONG_NUMBER_OF_COLUMNS_IN_SELECT = 1222
CANT_UPDATE_WITH_READLOCK = 1223
MIXING_NOT_ALLOWED = 1224
DUP_ARGUMENT = 1225
USER_LIMIT_REACHED = 1226
SPECIFIC_ACCESS_DENIED_ERROR = 1227
LOCAL_VARIABLE = 1228
GLOBAL_VARIABLE = 1229
NO_DEFAULT = 1230
WRONG_VALUE_FOR_VAR = 1231
WRONG_TYPE_FOR_VAR = 1232
VAR_CANT_BE_READ = 1233
CANT_USE_OPTION_HERE = 1234
NOT_SUPPORTED_YET = 1235
MASTER_FATAL_ERROR_READING_BINLOG = 1236
SLAVE_IGNORED_TABLE = 1237
INCORRECT_GLOBAL_LOCAL_VAR = 1238
WRONG_FK_DEF = 1239
KEY_REF_DO_NOT_MATCH_TABLE_REF = 1240
OPERAND_COLUMNS = 1241
SUBQUERY_NO_1_ROW = 1242
UNKNOWN_STMT_HANDLER = 1243
CORRUPT_HELP_DB = 1244
CYCLIC_REFERENCE = 1245
AUTO_CONVERT = 1246
ILLEGAL_REFERENCE = 1247
DERIVED_MUST_HAVE_ALIAS = 1248
SELECT_REDUCED = 1249
TABLENAME_NOT_ALLOWED_HERE = 1250
NOT_SUPPORTED_AUTH_MODE = 1251
SPATIAL_CANT_HAVE_NULL = 1252
COLLATION_CHARSET_MISMATCH = 1253
SLAVE_WAS_RUNNING = 1254
SLAVE_WAS_NOT_RUNNING = 1255
TOO_BIG_FOR_UNCOMPRESS = 1256
ZLIB_Z_MEM_ERROR = 1257
ZLIB_Z_BUF_ERROR = 1258
ZLIB_Z_DATA_ERROR = 1259
CUT_VALUE_GROUP_CONCAT = 1260
WARN_TOO_FEW_RECORDS = 1261
WARN_TOO_MANY_RECORDS = 1262
WARN_NULL_TO_NOTNULL = 1263
WARN_DATA_OUT_OF_RANGE = 1264
WARN_DATA_TRUNCATED = 1265
WARN_USING_OTHER_HANDLER = 1266
CANT_AGGREGATE_2COLLATIONS = 1267
DROP_USER = 1268
REVOKE_GRANTS = 1269
CANT_AGGREGATE_3COLLATIONS = 1270
CANT_AGGREGATE_NCOLLATIONS = 1271
VARIABLE_IS_NOT_STRUCT = 1272
UNKNOWN_COLLATION = 1273
SLAVE_IGNORED_SSL_PARAMS = 1274
SERVER_IS_IN_SECURE_AUTH_MODE = 1275
WARN_FIELD_RESOLVED = 1276
BAD_SLAVE_UNTIL_COND = 1277
MISSING_SKIP_SLAVE = 1278
UNTIL_COND_IGNORED = 1279
WRONG_NAME_FOR_INDEX = 1280
WRONG_NAME_FOR_CATALOG = 1281
WARN_QC_RESIZE = 1282
BAD_FT_COLUMN = 1283
UNKNOWN_KEY_CACHE = 1284
WARN_HOSTNAME_WONT_WORK = 1285
UNKNOWN_STORAGE_ENGINE = 1286
WARN_DEPRECATED_SYNTAX = 1287
NON_UPDATABLE_TABLE = 1288
FEATURE_DISABLED = 1289
OPTION_PREVENTS_STATEMENT = 1290
DUPLICATED_VALUE_IN_TYPE = 1291
TRUNCATED_WRONG_VALUE = 1292
TOO_MUCH_AUTO_TIMESTAMP_COLS = 1293
INVALID_ON_UPDATE = 1294
UNSUPPORTED_PS = 1295
GET_ERRMSG = 1296
GET_TEMPORARY_ERRMSG = 1297
UNKNOWN_TIME_ZONE = 1298
WARN_INVALID_TIMESTAMP = 1299
INVALID_CHARACTER_STRING = 1300
WARN_ALLOWED_PACKET_OVERFLOWED = 1301
CONFLICTING_DECLARATIONS = 1302
SP_NO_RECURSIVE_CREATE = 1303
SP_ALREADY_EXISTS = 1304
SP_DOES_NOT_EXIST = 1305
SP_DROP_FAILED = 1306
SP_STORE_FAILED = 1307
SP_LILABEL_MISMATCH = 1308
SP_LABEL_REDEFINE = 1309
SP_LABEL_MISMATCH = 1310
SP_UNINIT_VAR = 1311
SP_BADSELECT = 1312
SP_BADRETURN = 1313
SP_BADSTATEMENT = 1314
UPDATE_LOG_DEPRECATED_IGNORED = 1315
UPDATE_LOG_DEPRECATED_TRANSLATED = 1316
QUERY_INTERRUPTED = 1317
SP_WRONG_NO_OF_ARGS = 1318
SP_COND_MISMATCH = 1319
SP_NORETURN = 1320
SP_NORETURNEND = 1321
SP_BAD_CURSOR_QUERY = 1322
SP_BAD_CURSOR_SELECT = 1323
SP_CURSOR_MISMATCH = 1324
SP_CURSOR_ALREADY_OPEN = 1325
SP_CURSOR_NOT_OPEN = 1326
SP_UNDECLARED_VAR = 1327
SP_WRONG_NO_OF_FETCH_ARGS = 1328
SP_FETCH_NO_DATA = 1329
SP_DUP_PARAM = 1330
SP_DUP_VAR = 1331
SP_DUP_COND = 1332
SP_DUP_CURS = 1333
SP_CANT_ALTER = 1334
SP_SUBSELECT_NYI = 1335
STMT_NOT_ALLOWED_IN_SF_OR_TRG = 1336
SP_VARCOND_AFTER_CURSHNDLR = 1337
SP_CURSOR_AFTER_HANDLER = 1338
SP_CASE_NOT_FOUND = 1339
FPARSER_TOO_BIG_FILE = 1340
FPARSER_BAD_HEADER = 1341
FPARSER_EOF_IN_COMMENT = 1342
FPARSER_ERROR_IN_PARAMETER = 1343
FPARSER_EOF_IN_UNKNOWN_PARAMETER = 1344
VIEW_NO_EXPLAIN = 1345
FRM_UNKNOWN_TYPE = 1346
WRONG_OBJECT = 1347
NONUPDATEABLE_COLUMN = 1348
VIEW_SELECT_DERIVED = 1349
VIEW_SELECT_CLAUSE = 1350
VIEW_SELECT_VARIABLE = 1351
VIEW_SELECT_TMPTABLE = 1352
VIEW_WRONG_LIST = 1353
WARN_VIEW_MERGE = 1354
WARN_VIEW_WITHOUT_KEY = 1355
VIEW_INVALID = 1356
SP_NO_DROP_SP = 1357
SP_GOTO_IN_HNDLR = 1358
TRG_ALREADY_EXISTS = 1359
TRG_DOES_NOT_EXIST = 1360
TRG_ON_VIEW_OR_TEMP_TABLE = 1361
TRG_CANT_CHANGE_ROW = 1362
TRG_NO_SUCH_ROW_IN_TRG = 1363
NO_DEFAULT_FOR_FIELD = 1364
DIVISION_BY_ZERO = 1365
TRUNCATED_WRONG_VALUE_FOR_FIELD = 1366
ILLEGAL_VALUE_FOR_TYPE = 1367
VIEW_NONUPD_CHECK = 1368
VIEW_CHECK_FAILED = 1369
PROCACCESS_DENIED_ERROR = 1370
RELAY_LOG_FAIL = 1371
PASSWD_LENGTH = 1372
UNKNOWN_TARGET_BINLOG = 1373
IO_ERR_LOG_INDEX_READ = 1374
BINLOG_PURGE_PROHIBITED = 1375
FSEEK_FAIL = 1376
BINLOG_PURGE_FATAL_ERR = 1377
LOG_IN_USE = 1378
LOG_PURGE_UNKNOWN_ERR = 1379
RELAY_LOG_INIT = 1380
NO_BINARY_LOGGING = 1381
RESERVED_SYNTAX = 1382
WSAS_FAILED = 1383
DIFF_GROUPS_PROC = 1384
NO_GROUP_FOR_PROC = 1385
ORDER_WITH_PROC = 1386
LOGGING_PROHIBIT_CHANGING_OF = 1387
NO_FILE_MAPPING = 1388
WRONG_MAGIC = 1389
PS_MANY_PARAM = 1390
KEY_PART_0 = 1391
VIEW_CHECKSUM = 1392
VIEW_MULTIUPDATE = 1393
VIEW_NO_INSERT_FIELD_LIST = 1394
VIEW_DELETE_MERGE_VIEW = 1395
CANNOT_USER = 1396
XAER_NOTA = 1397
XAER_INVAL = 1398
XAER_RMFAIL = 1399
XAER_OUTSIDE = 1400
XAER_RMERR = 1401
XA_RBROLLBACK = 1402
NONEXISTING_PROC_GRANT = 1403
PROC_AUTO_GRANT_FAIL = 1404
PROC_AUTO_REVOKE_FAIL = 1405
DATA_TOO_LONG = 1406
SP_BAD_SQLSTATE = 1407
STARTUP = 1408
LOAD_FROM_FIXED_SIZE_ROWS_TO_VAR = 1409
CANT_CREATE_USER_WITH_GRANT = 1410
WRONG_VALUE_FOR_TYPE = 1411
TABLE_DEF_CHANGED = 1412
SP_DUP_HANDLER = 1413
SP_NOT_VAR_ARG = 1414
SP_NO_RETSET = 1415
CANT_CREATE_GEOMETRY_OBJECT = 1416
FAILED_ROUTINE_BREAK_BINLOG = 1417
BINLOG_UNSAFE_ROUTINE = 1418
BINLOG_CREATE_ROUTINE_NEED_SUPER = 1419
EXEC_STMT_WITH_OPEN_CURSOR = 1420
STMT_HAS_NO_OPEN_CURSOR = 1421
COMMIT_NOT_ALLOWED_IN_SF_OR_TRG = 1422
NO_DEFAULT_FOR_VIEW_FIELD = 1423
SP_NO_RECURSION = 1424
TOO_BIG_SCALE = 1425
TOO_BIG_PRECISION = 1426
M_BIGGER_THAN_D = 1427
WRONG_LOCK_OF_SYSTEM_TABLE = 1428
CONNECT_TO_FOREIGN_DATA_SOURCE = 1429
QUERY_ON_FOREIGN_DATA_SOURCE = 1430
FOREIGN_DATA_SOURCE_DOESNT_EXIST = 1431
FOREIGN_DATA_STRING_INVALID_CANT_CREATE = 1432
FOREIGN_DATA_STRING_INVALID = 1433
CANT_CREATE_FEDERATED_TABLE = 1434
TRG_IN_WRONG_SCHEMA = 1435
STACK_OVERRUN_NEED_MORE = 1436
TOO_LONG_BODY = 1437
WARN_CANT_DROP_DEFAULT_KEYCACHE = 1438
TOO_BIG_DISPLAYWIDTH = 1439
XAER_DUPID = 1440
DATETIME_FUNCTION_OVERFLOW = 1441
CANT_UPDATE_USED_TABLE_IN_SF_OR_TRG = 1442
VIEW_PREVENT_UPDATE = 1443
PS_NO_RECURSION = 1444
SP_CANT_SET_AUTOCOMMIT = 1445
MALFORMED_DEFINER = 1446
VIEW_FRM_NO_USER = 1447
VIEW_OTHER_USER = 1448
NO_SUCH_USER = 1449
FORBID_SCHEMA_CHANGE = 1450
ROW_IS_REFERENCED_2 = 1451
NO_REFERENCED_ROW_2 = 1452
SP_BAD_VAR_SHADOW = 1453
TRG_NO_DEFINER = 1454
OLD_FILE_FORMAT = 1455
SP_RECURSION_LIMIT = 1456
SP_PROC_TABLE_CORRUPT = 1457
SP_WRONG_NAME = 1458
TABLE_NEEDS_UPGRADE = 1459
SP_NO_AGGREGATE = 1460
MAX_PREPARED_STMT_COUNT_REACHED = 1461
VIEW_RECURSIVE = 1462
NON_GROUPING_FIELD_USED = 1463
TABLE_CANT_HANDLE_SPKEYS = 1464
NO_TRIGGERS_ON_SYSTEM_SCHEMA = 1465
USERNAME = 1466
HOSTNAME = 1467
WRONG_STRING_LENGTH = 1468
ERROR_LAST = 1468