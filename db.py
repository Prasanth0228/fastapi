# coding: utf-8
import self as self
from sqlalchemy import CHAR, CheckConstraint, Column, DECIMAL, Date, DateTime, Float, ForeignKey,alias, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGBLOB, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_emp_dept = Table(
    'emp_dept', metadata,
    Column('EMPNO', SMALLINT(6)),
    Column('ENAME', String(10)),
    Column('SAL', DECIMAL(7, 2)),
    Column('DNAME', String(14))
)


class LtaSubmission(Base):
    __tablename__ = 'lta_submissions'

    SUBMISSION_ID = Column(Float(asdecimal=True), primary_key=True)
    TITLE = Column(String(255), nullable=False)
    DOC_TYPE = Column(Float(asdecimal=True))
    REMARKS = Column(String(4000))
    CREATED_DATE = Column(DateTime)
    RECEIVED_DATE = Column(DateTime)
    DOC_CATEGORY = Column(Float(asdecimal=True))
    APP_NAME = Column(String(20), nullable=False, server_default=text("'EPCS'"))


t_raw_report = Table(
    'raw_report', metadata,
    Column('DATE12', String(200)),
    Column('IMPRESSIONS', String(200)),
    Column('CLICKS', String(200)),
    Column('EARNING', String(200))
)


class RstAddres(Base):
    __tablename__ = 'rst_address'

    ADDRESS_ID = Column(Float(asdecimal=True), primary_key=True)
    ADDRESS_LINE1 = Column(String(255))
    ADDRESS_LINE2 = Column(String(255))
    CITY = Column(String(55))
    STATE = Column(String(55))
    COUNTRY = Column(String(55))
    ZIPCODE = Column(String(20))
    CREATED_ON = Column(DATETIME(fsp=6))
    CREATED_BY = Column(BIGINT(20))
    FIRST_NAME = Column(String(50))
    LAST_NAME = Column(String(50))
    CONTACT_NO = Column(String(50))


class RstAdvance(Base):
    __tablename__ = 'rst_advance'

    ADV_ID = Column(Float(asdecimal=True), primary_key=True)
    JOB_ID = Column(Float(asdecimal=True), nullable=False)
    USER_ID = Column(Float(asdecimal=True), nullable=False)
    ADV_AMT = Column(Float(asdecimal=True))
    UPIID = Column(String(50))
    RCVD_BY = Column(Float(asdecimal=True))
    RCVD_DT = Column(DateTime)
    REMARKS = Column(String(300))
    PAYMENT_TYPE = Column(String(50), server_default=text("'Cash'"))


class RstAgreementTermCond(Base):
    __tablename__ = 'rst_agreement_term_cond'

    COMPANY_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    PARAGRAPH_NO = Column(SMALLINT(6), primary_key=True, nullable=False)
    FORM_TYPE = Column(String(20), primary_key=True, nullable=False)
    PARAGRAPH_CONTENT = Column(String(2000))
    AGREEMENT_TYPE = Column(String(20), nullable=False)
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    CREATED_BY = Column(BIGINT(20), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    AGREEMENT_ID = Column(BIGINT(20), nullable=False)
    CONTENT_TYPE = Column(String(20), server_default=text("'TEXT'"))
    TERMS_CONDITIONS_FILE = Column(LONGBLOB)
    ATTACHMENT_NAME = Column(String(110))


class RstAudit(Base):
    __tablename__ = 'rst_audit'

    AUDIT_ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20), nullable=False)
    AUDIT_DT = Column(DATETIME(fsp=2), nullable=False)
    ACTION = Column(String(255), nullable=False)
    MODULE = Column(String(255), nullable=False)
    KEY_TABLE = Column(String(255), nullable=False)
    KEY_FIELD = Column(String(255))
    KEY_FIELD_VALUE = Column(String(255))
    COMPANY_ID = Column(BIGINT(20))


class RstBranch(Base):
    __tablename__ = 'rst_branch'
    __table_args__ = (
        CheckConstraint('`BRANCH_CODE` is not null'),
        CheckConstraint('`PARTNER_CODE` is not null')
    )

    branch_id = Column(BIGINT(20), primary_key=True)
    PARTNER_CODE = Column(String(20))
    BRANCH_CODE = Column(String(20))
    ADDRESS = Column(String(155))
    LOCATION = Column(String(100))
    EMAIL_ID = Column(String(50))
    QR_CODE_FILE = Column(LONGBLOB)
    QR_CODE_NAME = Column(String(55))
    UPDATED_DT = Column(DateTime, server_default=text("current_timestamp()"))
    CREATED_BY = Column(DECIMAL(19, 0))
    UPDATED_BY = Column(DECIMAL(19, 0))
    ACTIVE_STATUS = Column(BIGINT(20))


class RstBrand(Base):
    __tablename__ = 'rst_brands'

    BRAND_ID = Column(BIGINT(20), primary_key=True)
    BRAND_NAME = Column(String(55), nullable=False)
    BRAND_IMAGE = Column(LONGBLOB)
    SYSTEM_CREATED = Column(TINYINT(4), server_default=text("0"))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    IMAGE_NAME = Column(String(255))
    BRAND_NAME_UP = Column(String(55), nullable=False)
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_DT = Column(DateTime)


t_rst_brands_01312020 = Table(
    'rst_brands_01312020', metadata,
    Column('BRAND_ID', BIGINT(20), nullable=False),
    Column('BRAND_NAME', String(55), nullable=False),
    Column('BRAND_IMAGE', LONGBLOB),
    Column('SYSTEM_CREATED', TINYINT(4)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('IMAGE_NAME', String(255)),
    Column('BRAND_NAME_UP', String(55), nullable=False),
    Column('UPDATED_BY', Float(asdecimal=True)),
    Column('UPDATED_DT', DateTime),
    Column('SERIES_ID', DECIMAL(30, 0))
)


class RstCallLogCase(Base):
    __tablename__ = 'rst_call_log_cases'

    CASE_ID = Column(Float(asdecimal=True), primary_key=True)
    ASSOCIATED_TO = Column(Float(asdecimal=True), nullable=False)
    CONSUMER_ID = Column(Float(asdecimal=True))
    CONSUMER_NAME = Column(String(255))
    CONTACT_NO = Column(String(55))
    CALL_CATEGORY = Column(Float(asdecimal=True))
    CREATED_ON = Column(DATETIME(fsp=6))
    CREATED_BY = Column(Float(asdecimal=True))
    CASE_STATUS = Column(Float(asdecimal=True), server_default=text("1"))
    MIGRATED_CASE_NO = Column(Float(asdecimal=True))
    CLOSED_ON = Column(DATETIME(fsp=6))
    CASE_NUMBER = Column(String(55))
    CALL_CATEGORY_BK = Column(Float(asdecimal=True))


class RstChildCompanyType(Base):
    __tablename__ = 'rst_child_company_types'
    __table_args__ = (
        Index('RST_CHILD_COMPANY_TYPES_UK1', 'PARENT_COMPANY_TYPE', 'CHILD_COMPANY_TYPE', unique=True),
    )

    REL_ID = Column(Float(asdecimal=True), primary_key=True)
    PARENT_COMPANY_TYPE = Column(String(255))
    CHILD_COMPANY_TYPE = Column(String(255))
    IS_ACTIVE = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    IS_PARTNERSHIP_ALLOWED = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    BRANCH_CREATION_ALLOWED = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))


class RstCodeType(Base):
    __tablename__ = 'rst_code_type'

    CODE_TYPE_ID = Column(BIGINT(20), primary_key=True)
    SYSTEM_CREATED = Column(TINYINT(4))
    CODE_TYPE = Column(String(20), unique=True)
    TYPE_DESC = Column(String(255))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    CREATED_DT = Column(DATETIME(fsp=2))
    IS_EDITABLE = Column(TINYINT(4), server_default=text("0"))


class RstCompany(Base):
    __tablename__ = 'rst_company'

    COMPANY_ID = Column(BIGINT(20), primary_key=True)
    COMPANY_NAME = Column(String(255), nullable=False)
    COMPANY_TYPE = Column(String(55), nullable=False)
    COMPANY_CODE = Column(String(55))
    REG_REF = Column(String(255))
    COMPANY_DESC = Column(String(55))
    IS_HEAD = Column(TINYINT(4), nullable=False)
    ADDRESS1 = Column(String(255))
    ADDRESS2 = Column(String(255))
    CITY = Column(String(255))
    CURRENCY_CODE = Column(String(20))
    GST_PERCENTAGE = Column(DECIMAL(10, 2))
    SMS_MESSAGE = Column(String(160))
    NO_OF_DECIMAL_PLACES = Column(BIGINT(20))
    STOCK_CLOSED_DT = Column(DATETIME(fsp=2))
    WORKING_HRS = Column(String(255))
    SERVICE_CHRG_1 = Column(DECIMAL(10, 2))
    SERVICE_CHRG_2 = Column(DECIMAL(10, 2))
    PHONE = Column(String(255))
    FAX = Column(String(55))
    COUNTRY_CODE = Column(String(55), nullable=False)
    POSTAL_CODE = Column(String(55))
    STATE = Column(String(255))
    CONTACT_PERSON = Column(String(55))
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2))
    CREATED_BY = Column(String(55))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    COMPANY_NAME_UP = Column(String(255))
    CITY_UP = Column(String(255))
    HAS_REGISTERED = Column(TINYINT(4))
    GLOBIX_CITY_LAT = Column(DECIMAL(20, 6))
    GLOBIX_CITY_LANG = Column(DECIMAL(20, 6))
    CONTACT_EMAIL = Column(String(120))
    MOBILE = Column(String(55))
    MOBILE_COUNTRY_CODE = Column(String(5))
    DOMAIN_NAME = Column(String(55))
    ROW_INDENTIFIER_1 = Column(String(55))
    TIMEZONE = Column(String(55), nullable=False)
    BRAND_ID = Column(String(20))


t_rst_company_10022020 = Table(
    'rst_company_10022020', metadata,
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('COMPANY_NAME', String(255), nullable=False),
    Column('COMPANY_TYPE', String(55), nullable=False),
    Column('COMPANY_CODE', String(55)),
    Column('REG_REF', String(255)),
    Column('COMPANY_DESC', String(55)),
    Column('IS_HEAD', TINYINT(4), nullable=False),
    Column('ADDRESS1', String(255)),
    Column('ADDRESS2', String(255)),
    Column('CITY', String(255)),
    Column('CURRENCY_CODE', String(20)),
    Column('GST_PERCENTAGE', DECIMAL(10, 2)),
    Column('SMS_MESSAGE', String(160)),
    Column('NO_OF_DECIMAL_PLACES', BIGINT(20)),
    Column('STOCK_CLOSED_DT', DATETIME(fsp=2)),
    Column('WORKING_HRS', String(255)),
    Column('SERVICE_CHRG_1', DECIMAL(10, 2)),
    Column('SERVICE_CHRG_2', DECIMAL(10, 2)),
    Column('PHONE', String(255)),
    Column('FAX', String(55)),
    Column('COUNTRY_CODE', String(55), nullable=False),
    Column('POSTAL_CODE', String(55)),
    Column('STATE', String(255)),
    Column('CONTACT_PERSON', String(55)),
    Column('ACTIVE_STATUS', TINYINT(4), nullable=False),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('CREATED_BY', String(55)),
    Column('UPDATED_DT', DATETIME(fsp=2)),
    Column('UPDATED_BY', BIGINT(20)),
    Column('COMPANY_NAME_UP', String(255)),
    Column('CITY_UP', String(255)),
    Column('HAS_REGISTERED', TINYINT(4)),
    Column('GLOBIX_CITY_LAT', DECIMAL(20, 6)),
    Column('GLOBIX_CITY_LANG', DECIMAL(20, 6)),
    Column('CONTACT_EMAIL', String(120)),
    Column('MOBILE', String(55)),
    Column('MOBILE_COUNTRY_CODE', String(5)),
    Column('DOMAIN_NAME', String(55)),
    Column('ROW_INDENTIFIER_1', String(55)),
    Column('TIMEZONE', String(55), nullable=False)
)


t_rst_company_brands = Table(
    'rst_company_brands', metadata,
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('BRAND_ID', DECIMAL(38, 0)),
    Column('IS_AUTHORISED', TINYINT(4)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2)),
    Column('COMPANY_BRAND_ID', Float(asdecimal=True))
)


t_rst_company_brands_new = Table(
    'rst_company_brands_new', metadata,
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('BRAND_ID', BIGINT(20), nullable=False),
    Column('IS_AUTHORISED', TINYINT(4), server_default=text("0")),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2)),
    Column('COMPANY_BRAND_ID', Float(asdecimal=True))
)


class RstCompanyChild(Base):
    __tablename__ = 'rst_company_child'

    PARENT_COMP_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    CHILD_COMP_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    ACTIVE_STATUS = Column(BIGINT(20), server_default=text("1"))
    IS_PARTNER = Column(TINYINT(4), server_default=text("0"))


t_rst_company_creation = Table(
    'rst_company_creation', metadata,
    Column('COMPANY_TYPE', String(20), nullable=False),
    Column('ALLOWED_CO_TYPE', String(20)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2))
)


class RstCompanyDetail(Base):
    __tablename__ = 'rst_company_details'

    COMPANY_ID = Column(BIGINT(20), primary_key=True)
    COMPANY_PO_LOGO = Column(LONGBLOB, nullable=False)


class RstCompanyNew(Base):
    __tablename__ = 'rst_company_new'

    COMPANY_ID = Column(BIGINT(20), primary_key=True)
    COMPANY_NAME = Column(String(255), nullable=False)
    COMPANY_TYPE = Column(String(55), nullable=False)
    COMPANY_CODE = Column(String(55))
    REG_REF = Column(String(255))
    COMPANY_DESC = Column(String(55))
    IS_HEAD = Column(TINYINT(4), nullable=False, server_default=text("0"))
    ADDRESS1 = Column(String(255))
    ADDRESS2 = Column(String(255))
    CITY = Column(String(255))
    CURRENCY_CODE = Column(String(20))
    GST_PERCENTAGE = Column(DECIMAL(10, 2))
    SMS_MESSAGE = Column(String(160))
    NO_OF_DECIMAL_PLACES = Column(BIGINT(20))
    STOCK_CLOSED_DT = Column(DATETIME(fsp=2))
    WORKING_HRS = Column(String(255))
    SERVICE_CHRG_1 = Column(DECIMAL(10, 2))
    SERVICE_CHRG_2 = Column(DECIMAL(10, 2))
    PHONE = Column(String(255))
    FAX = Column(String(55))
    COUNTRY_CODE = Column(String(55), nullable=False)
    POSTAL_CODE = Column(String(55))
    STATE = Column(String(255))
    CONTACT_PERSON = Column(String(55))
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    CREATED_DT = Column(DATETIME(fsp=2))
    CREATED_BY = Column(String(55))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    COMPANY_NAME_UP = Column(String(255))
    CITY_UP = Column(String(255))
    HAS_REGISTERED = Column(TINYINT(4), server_default=text("1"))
    GLOBIX_CITY_LAT = Column(DECIMAL(20, 6))
    GLOBIX_CITY_LANG = Column(DECIMAL(20, 6))
    CONTACT_EMAIL = Column(String(120))
    MOBILE = Column(String(55))
    MOBILE_COUNTRY_CODE = Column(String(5))
    DOMAIN_NAME = Column(String(55))
    ROW_INDENTIFIER_1 = Column(String(55))
    TIMEZONE = Column(String(55), nullable=False, server_default=text("'Asia/Singapore'"))


class RstCompanyType(Base):
    __tablename__ = 'rst_company_types'

    COMPANY_TYPE_ID = Column(Float(asdecimal=True), primary_key=True)
    COMPANY_TYPE = Column(String(55), unique=True)
    DISPLAY_NAME = Column(String(255))
    LICENSE_PRICE = Column(Float(asdecimal=True))
    NO_OF_LICENSE = Column(Float(asdecimal=True))
    VALIDITY_PERIOD = Column(Float(asdecimal=True))
    VALIDITY_PERIOD_UNIT = Column(String(20))
    DEFAULT_ROLE = Column(String(20))
    PARENT_COMPANY_TYPE = Column(String(55))
    CURRENCY_CODE = Column(String(20))
    IS_FREE = Column(TINYINT(4), server_default=text("0"))
    IS_PRICE_UNDISCLOSED = Column(TINYINT(4), server_default=text("0"))
    IS_ACTIVE = Column(TINYINT(4), server_default=text("0"))
    NEW_LICENSE_CONFIG_NAME = Column(String(55))


t_rst_companytype_payment_cfg = Table(
    'rst_companytype_payment_cfg', metadata,
    Column('COMPANY_TYPE', String(55)),
    Column('PAYMENT_CONFIG_NAME', String(55)),
    Column('ACTIVE_STATUS', Float(asdecimal=True), nullable=False, server_default=text("1")),
    Column('SHOW_ALWAYS', Float(asdecimal=True), nullable=False, server_default=text("0"))
)


class RstCompanytypeReportconfig(Base):
    __tablename__ = 'rst_companytype_reportconfig'
    __table_args__ = (
        Index('RST_COMPANYTYPE_REPORTCON_UK1', 'COMPANY_TYPE', 'REPORT_CONFIG_ID', unique=True),
    )

    ID = Column(Float(asdecimal=True), primary_key=True)
    COMPANY_TYPE = Column(String(55), nullable=False)
    REPORT_CONFIG_ID = Column(Float(asdecimal=True), nullable=False)


class RstCountryList(Base):
    __tablename__ = 'rst_country_list'

    COUNTRY_ID = Column(BIGINT(20), primary_key=True)
    NAME = Column(String(55), nullable=False)
    CODE2 = Column(String(2), nullable=False)
    CODE3 = Column(String(3), nullable=False)
    COUNTRY_NUM = Column(BIGINT(20))
    IDD = Column(BIGINT(20), nullable=False)
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False)
    NAME_UP = Column(String(55))


class RstCreditLimit(Base):
    __tablename__ = 'rst_credit_limits'

    CREDIT_LIMIT_ID = Column(Float(asdecimal=True), primary_key=True)
    CREDIT_TYPE = Column(String(55))
    CREDIT_LIMIT = Column(Float(asdecimal=True))
    COMPANY_ID = Column(Float(asdecimal=True))


class RstDespatchDetail(Base):
    __tablename__ = 'rst_despatch_details'

    DESPATCH_ID = Column(String(50), primary_key=True)
    TRACKING_NUMBER = Column(String(50))
    SHIPMENT_STATUS = Column(String(50))
    REF_TYPE = Column(String(50))
    INVOICE_NUMBER = Column(String(50))
    SHIPPED_DATE = Column(String(50))
    DELIVERED_DATE = Column(String(50))


t_rst_discount = Table(
    'rst_discount', metadata,
    Column('DISCOUNT_ID', Float(asdecimal=True), nullable=False),
    Column('ASC_LABOR', Float(asdecimal=True)),
    Column('ASC_PARTS', Float(asdecimal=True)),
    Column('ASC_TRANSPORT', Float(asdecimal=True)),
    Column('SVC_LABOR', Float(asdecimal=True)),
    Column('SVC_PARTS', Float(asdecimal=True)),
    Column('SVC_TRANSPORT', Float(asdecimal=True)),
    Column('SVC_OTHER', Float(asdecimal=True)),
    Column('ASC_OTHER', Float(asdecimal=True))
)


t_rst_dup_type_category_mapping = Table(
    'rst_dup_type_category_mapping', metadata,
    Column('ID', Float(asdecimal=True), nullable=False),
    Column('PROD_TYPE', String(100), nullable=False),
    Column('CAT_DESC', String(100), nullable=False),
    Column('IMAGE', LONGBLOB)
)


class RstEmailAudit(Base):
    __tablename__ = 'rst_email_audit'

    EMAIL_AUDIT_ID = Column(String(20), primary_key=True)
    COMPANY_ID = Column(Float(asdecimal=True))
    NO_OF_EMAILS = Column(Float(asdecimal=True))
    SENT_DATE = Column(DATETIME(fsp=6))
    EMAIL_CREDIT_USED = Column(Float(asdecimal=True))
    SUCCESS_COUNT = Column(Float(asdecimal=True))
    EMAIL_TYPE = Column(String(55))


class RstEmailTemplate(Base):
    __tablename__ = 'rst_email_templates'

    TEMPLATE_ID = Column(Float(asdecimal=True), primary_key=True)
    EMAIL_TYPE = Column(String(55))
    COMPANY_ID = Column(Float(asdecimal=True))
    SUBJECT = Column(String(1024), nullable=False)
    FROM_EMAIL = Column(String(255), nullable=False)
    REPLY_TO_EMAIL = Column(String(255))
    TRIGGER_EMAIL = Column(TINYINT(4), nullable=False, server_default=text("1"))
    LOCALE = Column(String(20), nullable=False, server_default=text("'EN_US'"))
    TEMPLATE_TYPE = Column(String(20), nullable=False, server_default=text("'EMAIL'"))
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_ON = Column(DATETIME(fsp=6))
    ALLOWED_PLACE_HOLDERS = Column(String(4000))
    EMAIL_BODY = Column(LONGTEXT)


class RstEmailType(Base):
    __tablename__ = 'rst_email_types'

    TYPE_ID = Column(Float(asdecimal=True), primary_key=True)
    EMAIL_TYPE = Column(String(55))
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    DISPLAY_NAME = Column(String(255))
    TRIGGER_EMAIL = Column(TINYINT(4))
    DESCRIPTION = Column(String(1024))
    ALLOWED_PLACE_HOLDERS = Column(String(1024))


t_rst_emailtypes_vs_companytype = Table(
    'rst_emailtypes_vs_companytype', metadata,
    Column('EMAIL_TYPE', String(55), nullable=False),
    Column('COMPANY_TYPE', String(55), nullable=False),
    Index('RST_EMAILTYPES_VS_COMPANY_UK1', 'EMAIL_TYPE', 'COMPANY_TYPE', unique=True)
)


class RstEqpmtStkRelation(Base):
    __tablename__ = 'rst_eqpmt_stk_relation'

    EQ_STOCK_ID_PARENT = Column(BIGINT(20), primary_key=True, nullable=False)
    EQ_STOCK_ID_CHILD = Column(BIGINT(20), primary_key=True, nullable=False)
    CREATED_BY = Column(BIGINT(20), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))


class RstEquipmtStock(Base):
    __tablename__ = 'rst_equipmt_stock'
    __table_args__ = (
        Index('RST_EQUIPMT_STOCK_UK1', 'SERIAL_NO_UP', 'PRODUCT_ID', unique=True),
    )

    EQ_STOCK_ID = Column(BIGINT(20), primary_key=True)
    SERIAL_NO = Column(String(55))
    PRODUCT_ID = Column(BIGINT(20))
    EQUIPMT_TYPE = Column(String(55))
    STATUS = Column(BIGINT(20))
    HOLDER_TYPE = Column(String(55))
    HOLDER_ID = Column(BIGINT(20))
    REMARKS = Column(String(255))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    REFERENCE_NO = Column(String(55))
    REFERENCE_TYPE = Column(String(55))
    SERIAL_NO_UP = Column(String(55), nullable=False)
    OWNER_ID = Column(BIGINT(20))
    PRODUCT_CONDITION = Column(TINYINT(4), server_default=text("1"))
    ON_HOLD_MIGRATION = Column(String(20))
    SENT_TO_WAREHOUSE = Column(String(2), server_default=text("'N'"))
    CAPACITY = Column(String(20))
    RACK_NO = Column(String(20))
    PRODUCT_NUMBER = Column(String(20))


class RstEquipmtDetail(RstEquipmtStock):
    __tablename__ = 'rst_equipmt_details'

    EQ_STOCK_ID = Column(ForeignKey('rst_equipmt_stock.EQ_STOCK_ID'), primary_key=True)
    CEI_SERIAL_NUMBER = Column(String(55))
    SKU_NUMBER = Column(String(55))
    IMEI_NO = Column(String(55))
    DEVICE_CODE = Column(String(55))
    BLUE_MAC_CODE = Column(String(55))
    WI_FI_MAC = Column(String(55))


class RstEquipmtStockBk(Base):
    __tablename__ = 'rst_equipmt_stock_bk'

    EQ_STOCK_ID = Column(BIGINT(20), primary_key=True)
    SERIAL_NO = Column(String(55))
    PRODUCT_ID = Column(BIGINT(20))
    EQUIPMT_TYPE = Column(String(55))
    STATUS = Column(BIGINT(20))
    HOLDER_TYPE = Column(String(55))
    HOLDER_ID = Column(BIGINT(20))
    REMARKS = Column(String(255))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    REFERENCE_NO = Column(String(55))
    REFERENCE_TYPE = Column(String(55))
    SERIAL_NO_UP = Column(String(55), nullable=False)
    OWNER_ID = Column(BIGINT(20))
    PRODUCT_CONDITION = Column(TINYINT(4), server_default=text("1"))
    ON_HOLD_MIGRATION = Column(String(20))
    RETAINED_EQ_STOCK_ID = Column(BIGINT(20))


class RstEquipmtTrack(Base):
    __tablename__ = 'rst_equipmt_track'

    TRACK_ID = Column(BIGINT(20), primary_key=True)
    SERIAL_NO = Column(String(55))
    PART_NO = Column(String(55))
    EQUIPMT_TYPE = Column(String(55))
    STATUS = Column(BIGINT(20), nullable=False)
    HOLDER_TYPE = Column(String(55))
    HOLDER_ID = Column(BIGINT(20))
    REMARK = Column(String(255))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    REFERENCE_NO = Column(String(55))
    REFERENCE_TYPE = Column(String(55))
    SERIAL_NO_UP = Column(String(55))
    PREV_HOLDER_TYPE = Column(String(55))
    PREV_HOLDER_ID = Column(BIGINT(20))
    SEQUENCE = Column(BIGINT(20))
    REASON = Column(BIGINT(20))
    PRODUCT_ID = Column(BIGINT(20))
    REASON_BK = Column(Float(asdecimal=True))


class RstEwPlanFeaturesMaster(Base):
    __tablename__ = 'rst_ew_plan_features_master'

    NAME_OF_THE_FEATURE = Column(String(500))
    FEATURE_ID = Column(BIGINT(20), primary_key=True)
    PLAN_ID = Column(Float(asdecimal=True))


class RstEwPlanList(Base):
    __tablename__ = 'rst_ew_plan_list'

    PLAN_ID = Column(Float(asdecimal=True), primary_key=True)
    PLAN_TITLE = Column(String(50), nullable=False)
    COMPANY_ID = Column(BIGINT(20), nullable=False)
    CREATED_BY = Column(String(55))
    CREATED_ON = Column(DATETIME(fsp=2))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))
    PLAN_SELLING_PRICE = Column(DECIMAL(38, 2), nullable=False, server_default=text("0.00"))
    PLAN_VTY_IN_MTHS = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    CURRENCY_OF_SELLING_PRICE = Column(String(3), nullable=False)
    PLAN_TNC = Column(LONGBLOB)
    MIN_PRODUCT_COST = Column(DECIMAL(38, 2), server_default=text("0.00"))
    CURRENCY_OF_MIN_PRODUCT_COST = Column(String(3))
    MF_WARRANTY_AGE_IN_DAYS = Column(Float(asdecimal=True), server_default=text("0"))
    PLAN_IMG = Column(LONGBLOB)
    PLAN_TYPE = Column(String(20))
    PLAN_IMAGE = Column(String(20))
    CURRENCY_OF_MAX_PRODUCT_COST = Column(String(3))
    MAX_PRODUCT_COST = Column(DECIMAL(38, 2))


t_rst_ew_plan_list_new = Table(
    'rst_ew_plan_list_new', metadata,
    Column('PLAN_ID', Float(asdecimal=True), nullable=False),
    Column('PLAN_TITLE', String(50), nullable=False),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('CREATED_BY', String(55)),
    Column('CREATED_ON', String(55)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('PLAN_SELLING_PRICE', DECIMAL(38, 2), nullable=False),
    Column('PLAN_VTY_IN_MTHS', Float(asdecimal=True), nullable=False),
    Column('CURRENCY_OF_SELLING_PRICE', String(3), nullable=False),
    Column('PLAN_TNC', LONGBLOB),
    Column('MIN_PRODUCT_COST', DECIMAL(38, 2)),
    Column('CURRENCY_OF_MIN_PRODUCT_COST', String(3)),
    Column('MF_WARRANTY_AGE_IN_DAYS', Float(asdecimal=True)),
    Column('PLAN_IMG', LONGBLOB),
    Column('PLAN_TYPE', String(20)),
    Column('PLAN_IMAGE', String(20)),
    Column('CURRENCY_OF_MAX_PRODUCT_COST', String(3)),
    Column('MAX_PRODUCT_COST', DECIMAL(38, 2))
)


t_rst_ew_price_matrix = Table(
    'rst_ew_price_matrix', metadata,
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('MIN_PRODUCT_COST', Float(asdecimal=True)),
    Column('MAX_PRODUCT_COST', Float(asdecimal=True)),
    Column('WARRANTY_MONTHS', Float(asdecimal=True)),
    Column('PRICE', Float(asdecimal=True))
)


t_rst_ew_setup = Table(
    'rst_ew_setup', metadata,
    Column('COMPANY_ID', Float(asdecimal=True), nullable=False),
    Column('MINIMUM_COST_OF_PRODUCT', Float(asdecimal=True)),
    Column('PRODUCT_AGE', Float(asdecimal=True)),
    Column('EXCHANGE_RATE', Float(asdecimal=True))
)


t_rst_function_code = Table(
    'rst_function_code', metadata,
    Column('FUNCTION_CODE', String(55)),
    Column('FUNCTION_DESCRIPTION', String(255)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('DISPLAYNAME', String(55)),
    Column('SEQUENCE', SMALLINT(6)),
    Column('FUNCTION_ID', Float(asdecimal=True)),
    Column('CATEGORY', String(50)),
    Column('REQD_PORTAL_GROUP_ACCESS', String(55))
)


t_rst_function_groups = Table(
    'rst_function_groups', metadata,
    Column('GROUP_NAME', String(55)),
    Column('FUNCTION_CODE', String(55))
)


t_rst_globix_admin = Table(
    'rst_globix_admin', metadata,
    Column('CC1', String(20)),
    Column('ADM1_CODE', String(20)),
    Column('ADM1_NAME', String(55)),
    Column('ADM1_NAME_ND', String(55)),
    Column('POSTAL_ABBREVIATION', String(20)),
    Column('ADM1_NAME_UP', String(55))
)


t_rst_globix_cc = Table(
    'rst_globix_cc', metadata,
    Column('COUNTRY_NAME', String(55)),
    Column('FIPS_10_4', String(20)),
    Column('COUNTRY_CODE', String(20)),
    Column('INTERNET_CODE', String(20)),
    Column('COMMENTS', String(255)),
    Column('COUNTRY_NAME_UP', String(55)),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1")),
    Column('CURRENCY_CODE', String(10)),
    Column('ISD_CODE', String(10))
)


class RstGlobixCity(Base):
    __tablename__ = 'rst_globix_cities'

    GLOBIX_CITY_ID = Column(BIGINT(20), primary_key=True)
    FEATURE_CODE = Column(String(20))
    REGION_ID = Column(BIGINT(20))
    SUB_REG_ID = Column(String(20))
    CC1 = Column(String(20))
    CHARS = Column(String(20))
    FULL_NAME = Column(String(300))
    FULL_NAME_ND = Column(String(300))
    ADM1 = Column(String(20))
    ADM2 = Column(String(255))
    LAT = Column(DECIMAL(11, 2))
    LANG = Column(DECIMAL(11, 2))
    DMS_LAT = Column(BIGINT(20))
    DMS_LONG = Column(BIGINT(20))
    FULL_NAME_UP = Column(String(300))


t_rst_globix_feature_code = Table(
    'rst_globix_feature_code', metadata,
    Column('FEATURE_CODE', String(55), nullable=False),
    Column('DESCRIPTION', String(255))
)


t_rst_globix_region = Table(
    'rst_globix_region', metadata,
    Column('REGION_ID', BIGINT(20), nullable=False),
    Column('REGION_NAME', String(55), nullable=False)
)


t_rst_globix_sub_region = Table(
    'rst_globix_sub_region', metadata,
    Column('SUB_REG_ID', String(5), nullable=False),
    Column('SUB_REG_NAME', String(55), nullable=False)
)


class RstGssSamsungSaBih(Base):
    __tablename__ = 'rst_gss_samsung_sa_bih'

    ID = Column(Float(asdecimal=True), primary_key=True)
    SHIP_TO_BRANCH_CODE = Column(String(20))
    SHIP_TO_BRANCH = Column(String(100))
    INVOICE_DATE = Column(String(20))
    INVOICE_NO = Column(String(20), unique=True)
    LOCAL_INVOICE_NO = Column(String(20))
    DELIVERY_NO = Column(String(20))
    ITEMS = Column(String(20))
    AMOUNT = Column(String(20))
    SGST_UTGST = Column(String(20))
    CGST = Column(String(20))
    IGST = Column(String(20))
    CESS = Column(String(20))
    TAX = Column(String(20))
    TOTAL = Column(String(20))
    GR_STATUS = Column(CHAR(1))


class RstGssSamsungSaDse(Base):
    __tablename__ = 'rst_gss_samsung_sa_dse'

    ID = Column(Float(asdecimal=True), primary_key=True)
    SERVICE_ORDER_NO = Column(Float(asdecimal=True), unique=True)
    LAST_UPDATED_USER = Column(String(55))
    BILLING_USER = Column(String(55))
    BILLING_DATE = Column(String(55))
    GOODS_DELIVERY_DATE = Column(String(55))
    BRANCH_NAME = Column(String(55))
    ENGINEER_ID = Column(String(20))
    ENGINEER_NAME = Column(String(20))
    PRODUCT_TYPE = Column(String(20))
    PRODUCT_TYPE_NAME = Column(String(20))
    IN_WARRANTY = Column(Float(asdecimal=True))
    IN_WARRANTY_LABOR = Column(String(20))
    IN_WARRANTY_PARTS = Column(String(20))
    IN_WARRANTY_TRANSPORT = Column(String(20))
    IN_WARRANTY_OTHERS = Column(String(20))
    IN_WARRANTY_TAX = Column(String(20))
    IN_WARRANTY_TOTAL = Column(String(20))
    OUT_WARRANTY = Column(Float(asdecimal=True))
    OUT_WARRANTY_LABOR = Column(String(20))
    OUT_WARRANTY_PARTS = Column(String(20))
    OUT_WARRANTY_TRANSPORT = Column(String(20))
    OUT_WARRANTY_OTHERS = Column(String(20))
    OUT_WARRANTY_TAX = Column(String(20))
    OUT_WARRANTY_TOTAL = Column(String(20))


class RstGssSamsungSaSi(Base):
    __tablename__ = 'rst_gss_samsung_sa_si'

    ID = Column(Float(asdecimal=True), primary_key=True)
    BRANCH = Column(String(20))
    PARTS_NO = Column(String(50))
    DESCRIPTION = Column(String(255))
    TOTAL_STOCK_QTY = Column(String(10))
    WAREHOUSE_STOCK_QTY = Column(String(10))
    ENGINEER_STOCK_QTY = Column(String(10))
    LOCATION1 = Column(String(50))
    LOCATION2 = Column(String(50))
    LOCATION3 = Column(String(50))
    MAP = Column(String(20))
    TOTAL_STOCK_VALUE = Column(String(20))
    STATUS = Column(String(10))
    LATEST_MODIFY_DATE = Column(String(20))


class RstGtinMaster(Base):
    __tablename__ = 'rst_gtin_master'

    ID = Column(DECIMAL(20, 0), primary_key=True)
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))


t_rst_instant_fix = Table(
    'rst_instant_fix', metadata,
    Column('FIX_ID', Float(asdecimal=True)),
    Column('ISSUE_ID', Float(asdecimal=True)),
    Column('SERVICE_CENTER_ID', Float(asdecimal=True)),
    Column('USER_ID', Float(asdecimal=True)),
    Column('FIX_PRICE', String(20)),
    Column('PRODUCT_ID', Float(asdecimal=True)),
    Column('PICKUP_TIMESTAMP', DATETIME(fsp=6)),
    Column('DELIVERY_CHARGE', String(20)),
    Column('CREATED_BY', Float(asdecimal=True)),
    Column('CREATED_ON', DATETIME(fsp=6)),
    Column('EQ_STOCK_ID', Float(asdecimal=True)),
    Column('INVOICE_NUMBER', String(512)),
    Column('SERVICE_REQUEST_STATUS', String(20)),
    Column('MODEL_ID', Float(asdecimal=True)),
    Column('CUSTOMER_NAME', String(50)),
    Column('CUSTOMER_ADDRESS', String(500)),
    Column('MOBILE_NO', String(50)),
    Column('EMAIL_ID', String(50)),
    Column('JOB_STATUS_CODE', DECIMAL(11, 2)),
    Column('CUSTOMER_LATITUDE', DECIMAL(20, 6)),
    Column('CUSTOMER_LONGITUDE', DECIMAL(20, 6)),
    Column('FCM_KEY', String(200)),
    Column('REMARKS', String(200)),
    Column('WARRANTY_TYPE', String(5)),
    Column('MESSAGE', String(200)),
    Column('ADDRESS2', String(255)),
    Column('CITY', String(55)),
    Column('STATE', String(100)),
    Column('POSTAL_CODE', String(20)),
    Column('COUNTRY_CODE', String(55))
)


t_rst_instant_fix_new = Table(
    'rst_instant_fix_new', metadata,
    Column('FIX_ID', Float(asdecimal=True)),
    Column('ISSUE_ID', Float(asdecimal=True)),
    Column('SERVICE_CENTER_ID', Float(asdecimal=True)),
    Column('USER_ID', Float(asdecimal=True)),
    Column('FIX_PRICE', String(20)),
    Column('PRODUCT_ID', Float(asdecimal=True)),
    Column('PICKUP_TIMESTAMP', DATETIME(fsp=6)),
    Column('DELIVERY_CHARGE', String(20)),
    Column('CREATED_BY', Float(asdecimal=True)),
    Column('CREATED_ON', DATETIME(fsp=6)),
    Column('EQ_STOCK_ID', Float(asdecimal=True)),
    Column('INVOICE_NUMBER', String(512)),
    Column('SERVICE_REQUEST_STATUS', String(20))
)


class RstInventoryTransfer(Base):
    __tablename__ = 'rst_inventory_transfer'

    INVENTORY_ID = Column(BIGINT(20), primary_key=True)
    COMPANY_ID = Column(BIGINT(20), nullable=False)
    PRODUCT_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    TRANSACTION_TYPE = Column(String(55))
    TRANSACTION_REF_NO = Column(String(55))
    RECEIPENT_COMP_ID = Column(BIGINT(20))
    RECEIPENT_ADDR = Column(String(255))
    RECEIPENT_CONTACT_NO = Column(String(55))
    RECEIPENT_NOTES = Column(String(255))
    ACK_STATUS = Column(TINYINT(4), server_default=text("0"))
    REMARKS = Column(String(4000))
    CURRENT_PROCESSED_ROW = Column(BIGINT(20), server_default=text("0"))
    RECEIPENT_NOTES_BK = Column(String(255))
    MERGED_TO = Column(Float(asdecimal=True))


class RstInvitation(Base):
    __tablename__ = 'rst_invitation'

    ID = Column(String(55), primary_key=True)
    INVITER = Column(Float(asdecimal=True), nullable=False)
    RECEIVER = Column(String(255), nullable=False)
    INVITED_ON = Column(DateTime)
    ACCEPTED_ON = Column(DateTime)
    ACCEPTANCE_STATUS = Column(String(20), nullable=False, server_default=text("'PENDING'"))


t_rst_ip2location_full = Table(
    'rst_ip2location_full', metadata,
    Column('IP_FROM', DECIMAL(25, 2)),
    Column('IP_TO', DECIMAL(25, 2)),
    Column('COUNTRY_CODE', String(2)),
    Column('COUNTRY_NAME', String(255)),
    Column('REGION', String(255)),
    Column('CITY', String(255)),
    Column('LATITUDE', DECIMAL(25, 2)),
    Column('LONGITUDE', DECIMAL(25, 2)),
    Column('ZIPCODE', String(255)),
    Column('TIME_ZONE', String(255))
)


class RstIssue(Base):
    __tablename__ = 'rst_issue'

    ISSUE_ID = Column(String(20), primary_key=True)
    PRODUCT_TYPE = Column(String(55))
    ISSUE_DESC = Column(String(255))
    ISSUE_IMG = Column(LONGBLOB)
    WARRANTY_TYPE = Column(String(10))


class RstJobPart(Base):
    __tablename__ = 'rst_job_parts'

    JOB_PARTS_ID = Column(BIGINT(20), primary_key=True)
    PRODUCT_ID = Column(BIGINT(20), nullable=False)
    QTY = Column(BIGINT(20))
    REMARKS = Column(String(2000))
    PCB_LOCATION = Column(String(55))
    FAIL_CODE = Column(String(20))
    REPAIR_CODE = Column(String(20))
    COMPANY_ID = Column(BIGINT(20), nullable=False)
    EQ_STOCK_ID = Column(BIGINT(20))
    SR_ID = Column(Float(asdecimal=True))


t_rst_job_parts_used = Table(
    'rst_job_parts_used', metadata,
    Column('JOB_PARTS_ID', BIGINT(20), nullable=False),
    Column('QTY', BIGINT(20)),
    Column('REMARKS', String(2000)),
    Column('PCB_LOCATION', String(55)),
    Column('FAIL_CODE', String(20)),
    Column('REPAIR_CODE', String(20)),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('EQ_STOCK_ID', BIGINT(20)),
    Column('JOB_ID', Float(asdecimal=True)),
    Column('PART_SERIAL_NO', String(100)),
    Column('PART_NO', String(55)),
    Column('ADV_AMT', DECIMAL(11, 2)),
    Column('ADV_QTY', BIGINT(20))
)


class RstJobQc(Base):
    __tablename__ = 'rst_job_qc'

    JOB_ID = Column(Float(asdecimal=True), primary_key=True, nullable=False)
    QC_ID = Column(Float(asdecimal=True), primary_key=True, nullable=False)
    VALUE = Column(String(20))


class RstJobRepairHistory(Base):
    __tablename__ = 'rst_job_repair_history'

    JOB_ID = Column(Float(asdecimal=True), nullable=False)
    CREATED_BY = Column(Float(asdecimal=True), nullable=False)
    CREATED_DATE = Column(DateTime, nullable=False)
    REPAIR_HISTORY_ID = Column(Float(asdecimal=True), primary_key=True)
    REPAIR_NOTES = Column(String(4000), nullable=False)


t_rst_labor_chrg = Table(
    'rst_labor_chrg', metadata,
    Column('LEVEL_CODE', DECIMAL(11, 2)),
    Column('DESCRIPTION', String(255)),
    Column('LABOR_CHRG', Float(asdecimal=True)),
    Column('TYPE', String(20))
)


class RstLicMainFunc(Base):
    __tablename__ = 'rst_lic_main_func'

    FUNC_ID = Column(BIGINT(20), primary_key=True)
    FUNC_NAME = Column(String(55), nullable=False)
    FUNC_DESCRIPTION = Column(String(255))
    ORDER_SEQ = Column(BIGINT(20))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    CREATED_BY = Column(BIGINT(20), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))


class RstLicSubFunc(Base):
    __tablename__ = 'rst_lic_sub_func'

    FUNC_SUB_ID = Column(BIGINT(20), primary_key=True)
    FUNC_ID = Column(BIGINT(20), nullable=False)
    FUNC_SUB_DESCRIPTION = Column(String(255))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))


t_rst_lic_type_main_sub_func = Table(
    'rst_lic_type_main_sub_func', metadata,
    Column('FUNC_SUB_ID', BIGINT(20), nullable=False),
    Column('FUNC_ID', BIGINT(20), nullable=False),
    Column('LICENSE_TYPE_ID', BIGINT(20), nullable=False),
    Column('CHECKED', TINYINT(4), nullable=False),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1")),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2))
)


class RstLicense(Base):
    __tablename__ = 'rst_license'

    LICENSE_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    COMPANY_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    NO_OF_LIC = Column(BIGINT(20))
    NO_OF_LIC_LEFT = Column(BIGINT(20))
    AMOUNT = Column(DECIMAL(12, 2))
    EXPIRY_DT = Column(DATETIME(fsp=6))
    HAS_PAID = Column(TINYINT(4), nullable=False, server_default=text("-1"))
    REMARKS = Column(String(255))
    LICENSE_TYPE_ID = Column(BIGINT(20))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    PAYMENT_ID = Column(BIGINT(20))
    CURRENCY_CODE = Column(String(55))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    INVOICE_NO = Column(String(55))
    PAYMENT_CONFIG_NAME = Column(String(55))
    PARENT_LICENSE_ID = Column(Float(asdecimal=True))


class RstLicenseType(Base):
    __tablename__ = 'rst_license_type'

    LICENSE_TYPE_ID = Column(BIGINT(20), primary_key=True)
    NAME = Column(String(55), nullable=False, unique=True)
    PRICE = Column(BIGINT(20), nullable=False)
    CURRENCY_CODE = Column(String(55), nullable=False)
    CREATED_BY = Column(BIGINT(20), nullable=False)
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    NO_LICENSES = Column(BIGINT(20), nullable=False, server_default=text("1"))
    LIC_PERIOD = Column(INTEGER(11), nullable=False, server_default=text("1"))


t_rst_license_type_grp = Table(
    'rst_license_type_grp', metadata,
    Column('LICENSE_TYPE_ID', BIGINT(20), nullable=False),
    Column('ACCESSGROUP', BIGINT(20)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2))
)


t_rst_licensed_partners = Table(
    'rst_licensed_partners', metadata,
    Column('PAYMENT_CONFIG_NAME', String(55)),
    Column('COMPANY_TYPE', String(55))
)


t_rst_logistic_contacts = Table(
    'rst_logistic_contacts', metadata,
    Column('COMPANY_NAME', String(55)),
    Column('COUNTRY_CODE', String(5)),
    Column('COUNTRY_NAME', String(55)),
    Column('CONTACT_NO', String(55)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('HAS_ONLINE_PICKUP', String(1), server_default=text("'N'"))
)


t_rst_logistics_request = Table(
    'rst_logistics_request', metadata,
    Column('LOGISTICS_REQ_ID', Float(asdecimal=True), nullable=False),
    Column('USER_ID', Float(asdecimal=True)),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('CREATED_DT', DateTime),
    Column('SHIP_FROM', BIGINT(20)),
    Column('DECLARED_VALUE', DECIMAL(11, 2)),
    Column('PACKAGE_WEIGHT', String(30)),
    Column('NO_OF_PACKAGE', BIGINT(20)),
    Column('CURRENCY_CODE', String(20)),
    Column('REF_NUMBER', String(55)),
    Column('REF_TYPE', String(55)),
    Column('SHIP_TO', Float(asdecimal=True)),
    Column('RECEIVER_CONTACT_NO', String(50)),
    Column('RECEIVER_NAME', String(55)),
    Column('LENGTH', INTEGER(11)),
    Column('WIDTH', INTEGER(11)),
    Column('PACK_TYPE', String(55)),
    Column('WEIGHT_TYPE', String(3)),
    Column('SERVICE_CODE', String(20)),
    Column('PICKUP_TYPE', String(2)),
    Column('IS_APPROVED', TINYINT(4), server_default=text("0")),
    Column('HEIGHT', INTEGER(11)),
    Column('SHIPPING_LABEL', LONGBLOB),
    Column('EQ_STOCK_ID', Float(asdecimal=True)),
    Column('INVOICE_NUMBER', String(55)),
    Column('IS_CANCELED', TINYINT(4), server_default=text("0")),
    Column('SHIPMENT_PENDING', TINYINT(4), server_default=text("1")),
    Column('SHIPMENT_DIGEST', LONGBLOB),
    Column('HTML_IMAGE', LONGBLOB),
    Column('PICKUP_REF_NO', String(55)),
    Column('PICKUP_DATE', DateTime),
    Column('PICKUP_TIME', String(10)),
    Column('WEIGHT_MEASUREMENT_UNIT', String(5)),
    Column('DIMENSION_MEASUREMENT_UNIT', String(5)),
    Column('SHIP_DATE', DateTime),
    Column('SERVICE_NAME', String(255)),
    Column('LOGISTICS_COMPANY_NAME', String(20)),
    Column('SHIPMENT_METHOD', String(255)),
    Column('SHIPMENT_STATUS', String(50)),
    Column('SENT_TO_WAREHOUSE', String(2), server_default=text("'N'")),
    Column('ORDER_REF_NUMBER', String(255)),
    Column('SHIP_TO_COMPANY', String(255))
)


t_rst_lucky_draw = Table(
    'rst_lucky_draw', metadata,
    Column('LUCKY_DRAW_ID', Float(asdecimal=True)),
    Column('WINNER_ID', Float(asdecimal=True)),
    Column('DRAWN_ON', DateTime),
    Column('PRIZE', String(255))
)


t_rst_models = Table(
    'rst_models', metadata,
    Column('MODEL_ID', BIGINT(20), nullable=False),
    Column('MODEL_NAME', String(255), nullable=False),
    Column('IMEI_REF_LENGTH', BIGINT(20)),
    Column('IMEI_REF_CHARS', String(255)),
    Column('BY_IMEI_NO', TINYINT(4)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('IS_AUTO_DATE', TINYINT(4)),
    Column('IS_AUTO_IMEI', TINYINT(4)),
    Column('BRAND_ID', BIGINT(20), nullable=False),
    Column('COMPANY_ID', BIGINT(20)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('MODEL_NAME_UP', String(255)),
    Column('PRODUCT_TYPE', String(55)),
    Column('PRODUCT_TYPE_UP', String(55)),
    Column('UPDATED_BY', Float(asdecimal=True)),
    Column('UPDATED_DT', DateTime),
    Column('IMAGE', LONGBLOB),
    Column('SERIES_ID', DECIMAL(30, 0))
)


t_rst_models_01312020 = Table(
    'rst_models_01312020', metadata,
    Column('MODEL_ID', BIGINT(20)),
    Column('MODEL_NAME', String(255), nullable=False),
    Column('IMEI_REF_LENGTH', BIGINT(20)),
    Column('IMEI_REF_CHARS', String(255)),
    Column('BY_IMEI_NO', TINYINT(4)),
    Column('ACTIVE_STATUS', TINYINT(4)),
    Column('IS_AUTO_DATE', TINYINT(4)),
    Column('IS_AUTO_IMEI', TINYINT(4)),
    Column('BRAND_ID', BIGINT(20), nullable=False),
    Column('COMPANY_ID', BIGINT(20)),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('MODEL_NAME_UP', String(255)),
    Column('PRODUCT_TYPE', String(55)),
    Column('PRODUCT_TYPE_UP', String(55)),
    Column('UPDATED_BY', Float(asdecimal=True)),
    Column('UPDATED_DT', DateTime),
    Column('IMAGE', LONGBLOB),
    Column('SERIES_ID', DECIMAL(30, 0))
)


class RstModelsMob(Base):
    __tablename__ = 'rst_models_mob'

    MODEL_ID = Column(BIGINT(20), primary_key=True)
    MODEL_NAME = Column(String(255), nullable=False)
    IMEI_REF_LENGTH = Column(BIGINT(20))
    IMEI_REF_CHARS = Column(String(255))
    BY_IMEI_NO = Column(TINYINT(4))
    ACTIVE_STATUS = Column(TINYINT(4))
    IS_AUTO_DATE = Column(TINYINT(4))
    IS_AUTO_IMEI = Column(TINYINT(4))
    BRAND_ID = Column(BIGINT(20), nullable=False)
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    MODEL_NAME_UP = Column(String(255))
    PRODUCT_TYPE = Column(String(55))
    PRODUCT_TYPE_UP = Column(String(55))
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_DT = Column(DateTime)


class RstModelsOrg(Base):
    __tablename__ = 'rst_models_org'

    MODEL_ID = Column(BIGINT(20), primary_key=True)
    MODEL_NAME = Column(String(255), nullable=False)
    IMEI_REF_LENGTH = Column(BIGINT(20))
    IMEI_REF_CHARS = Column(String(255))
    BY_IMEI_NO = Column(TINYINT(4))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    IS_AUTO_DATE = Column(TINYINT(4), server_default=text("0"))
    IS_AUTO_IMEI = Column(TINYINT(4), server_default=text("0"))
    BRAND_ID = Column(BIGINT(20), nullable=False)
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    MODEL_NAME_UP = Column(String(255))
    PRODUCT_TYPE = Column(String(55))
    PRODUCT_TYPE_UP = Column(String(55))
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_DT = Column(DateTime)


class RstPart(Base):
    __tablename__ = 'rst_parts'

    PART_NO = Column(String(55), nullable=False)
    DESCRIPTION = Column(String(55))
    HSN_CODE = Column(String(20))
    BASE_PRICE = Column(DECIMAL(11, 2))
    CUSTOMER_PRICE = Column(BIGINT(20))
    STOCK_AVAILABILITY = Column(String(20))
    ETD = Column(DateTime)
    CGST = Column(DECIMAL(11, 2))
    SGST = Column(DECIMAL(11, 2))
    PRODUCT = Column(String(50))
    MODELNO = Column(String(50))
    COLOR = Column(String(25))
    QTY = Column(Float(asdecimal=True))
    PART_ID = Column(BIGINT(20), primary_key=True)


class RstPaymentConfig(Base):
    __tablename__ = 'rst_payment_config'

    PAYMENT_CONFIG_ID = Column(Float(asdecimal=True), primary_key=True)
    CONFIG_NAME = Column(String(255))
    DESCRIPTION = Column(String(255))
    PRICE = Column(Float(asdecimal=True))
    CURRENCY_CODE = Column(String(20))
    GROUP_CODE = Column(String(55))
    EXT_LICENSE_QTY_BY = Column(Float(asdecimal=True))
    EXT_LICENSE_BY_MONTHS = Column(Float(asdecimal=True))


class RstPaymentCrypt(Base):
    __tablename__ = 'rst_payment_crypt'

    CRYPT_ID = Column(Float(asdecimal=True), primary_key=True)
    SESSION_ID = Column(String(4000), nullable=False)
    USER_SESSION_OBJ = Column(LONGBLOB, nullable=False)


t_rst_payment_portal_clients = Table(
    'rst_payment_portal_clients', metadata,
    Column('CLIENT_ID', Float(asdecimal=True), nullable=False),
    Column('SECRET_KEY1', String(255)),
    Column('SECRET_KEY2', String(255)),
    Column('EMAIL_RECIPIENTS', String(4000))
)


class RstPayment(Base):
    __tablename__ = 'rst_payments'

    PAYMENT_ID = Column(BIGINT(20), primary_key=True)
    PAYMENT_TYPE = Column(String(55), nullable=False)
    PAYMENT_AMOUNT = Column(Float(asdecimal=True), nullable=False)
    CURRENCY_CODE = Column(String(55), nullable=False)
    GATEWAY_TRANS_NUMBER = Column(String(55))
    TRANSACTION_STATUS = Column(TINYINT(4), nullable=False)
    COMPANY_ID = Column(BIGINT(20), nullable=False)
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2), nullable=False)
    INVOICE_NUMBER = Column(String(55), nullable=False)
    STATUS_TEXT = Column(String(255))
    APPROVAL_CODE = Column(String(25))
    IP_ADDRESS = Column(String(32))
    PAYMENT_CONFIG_NAME = Column(String(55))
    ITEM_TYPE = Column(String(2000))
    ITEM_QTY = Column(BIGINT(20))
    IS_CANCELED = Column(TINYINT(4), server_default=text("0"))


class RstPlan(Base):
    __tablename__ = 'rst_plan'

    ID = Column(DECIMAL(19, 0), primary_key=True)
    ACTIVE_STATUS = Column(BIGINT(20))
    CREATED_DATE = Column(DateTime)
    NAME = Column(String(255), nullable=False)
    PRICE = Column(BIGINT(20))
    CATEGORY = Column(String(255))
    SKU_ID = Column(String(255), nullable=False, unique=True)
    UNITS = Column(BIGINT(20))
    VALIDITY_MONTHS = Column(BIGINT(20))
    COMPANY_ID = Column(LONGTEXT)
    PRODUCT_VALIDITY = Column(String(100))
    PRODUCT_CATEGORY = Column(String(100))
    SERVICE_CATEGORY = Column(String(100))
    SALES_CHANNEL = Column(String(100))
    PRODUCT_CATEGORY_CODE = Column(String(20))
    PRODUCT_PRICE_FROM = Column(DECIMAL(20, 2))
    PRODUCT_PRICE_TO = Column(DECIMAL(20, 2))
    GTIN = Column(DECIMAL(20, 0))


class RstPoList(Base):
    __tablename__ = 'rst_po_list'

    PO_ID = Column(BIGINT(20), primary_key=True)
    PO_REF = Column(String(55))
    SUPPLIER_ID = Column(String(55))
    PO_STATUS = Column(String(55))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    APPROVED_BY = Column(BIGINT(20))
    APPROVED_DT = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))


class RstPoMrItem(Base):
    __tablename__ = 'rst_po_mr_items'

    PO_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    MR_NUMBER = Column(String(55))
    REQ_PART_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    PO_REQUESTED_QTY = Column(BIGINT(20))
    PO_APPROVED_QTY = Column(BIGINT(20))
    RECEIVED_QTY = Column(BIGINT(20))
    PART_PRICE = Column(DECIMAL(11, 2))
    COMPANY_ID = Column(BIGINT(20))
    CURRENCY_CODE = Column(String(20))


class RstPosReceipt(Base):
    __tablename__ = 'rst_pos_receipt'

    RECEIPT_ID = Column(Float(asdecimal=True), primary_key=True)
    RECEIPT_DATE = Column(DateTime, nullable=False)
    HANDLED_BY = Column(Float(asdecimal=True), nullable=False)
    CONSUMER_NAME = Column(String(255))
    CONSUMER_ID = Column(Float(asdecimal=True))
    AMOUNT_CHARGED = Column(Float(asdecimal=True), nullable=False)
    AMOUNT_PAID = Column(Float(asdecimal=True))
    BALANCE_RETURNED = Column(Float(asdecimal=True))
    CURRENCY_CODE = Column(String(5), nullable=False)
    MODE_OF_PAYMENT = Column(String(20), nullable=False, server_default=text("'CASH'"))
    PAYMENT_ID = Column(Float(asdecimal=True))
    STATUS = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    ACTIVE_STATUS = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    AMOUNT_ROUNDED = Column(Float(asdecimal=True))
    ITEM_ID = Column(Float(asdecimal=True), nullable=False)
    RECEIPT_NO = Column(String(55), nullable=False)


class RstPostcode(Base):
    __tablename__ = 'rst_postcode'

    ID = Column(DECIMAL(19, 0), primary_key=True)
    POSTAL_CODE = Column(BIGINT(20))
    CITY = Column(String(100))
    STATE = Column(String(100))
    TALUK = Column(String(100))


t_rst_prod_type_category_mapping = Table(
    'rst_prod_type_category_mapping', metadata,
    Column('ID', Float(asdecimal=True), nullable=False),
    Column('PROD_TYPE', String(100), nullable=False),
    Column('CAT_DESC', String(100), nullable=False),
    Column('IMAGE', LONGBLOB)
)


class RstProductMaster(Base):
    __tablename__ = 'rst_product_master'

    PRODUCT_ID = Column(BIGINT(20), primary_key=True)
    PART_NO = Column(String(55))
    MODEL_ID_OLD = Column(String(255))
    SUB_CATEGORY = Column(String(55), server_default=text("'PRODUCT'"))
    SPECIFICATION = Column(String(255))
    DESCRIPTION = Column(String(255))
    REORDER_LVL = Column(BIGINT(20))
    MAX_ORDER = Column(BIGINT(20))
    MIN_ORDER = Column(BIGINT(20))
    SET_OF_UNIT = Column(BIGINT(20))
    LEAD_TIME = Column(BIGINT(20))
    UNIT_PRICE = Column(DECIMAL(11, 2))
    SELLING_PRICE = Column(DECIMAL(11, 2))
    CURRENCY_CODE = Column(String(20))
    DISTRIBUTOR_PRICE = Column(DECIMAL(11, 2))
    SHIPPING_PRICE = Column(DECIMAL(11, 2))
    DUMMY_PROD = Column(TINYINT(4), server_default=text("0"))
    DISCONTINUED = Column(TINYINT(4), server_default=text("0"))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    WARRANTY_MONTHS = Column(SMALLINT(6))
    SUPPLIER = Column(String(55))
    REPAIRABLE_PRICE = Column(DECIMAL(11, 2))
    REPAIR_WARRANTY = Column(BIGINT(20))
    REMARKS = Column(String(255))
    IMAGE = Column(LONGBLOB)
    PROD_SPEC = Column(LONGBLOB)
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    PART_NO_UP = Column(String(55))
    MODEL_ID = Column(BIGINT(20), nullable=False)
    RECYCLE_WORKING_PRICE = Column(DECIMAL(11, 2))
    RECYCLE_NON_WORKING_PRICE = Column(DECIMAL(11, 2))
    CAPACITY = Column(String(20))
    PRODUCT_NUMBER = Column(String(20))


class RstProductMasterBk(Base):
    __tablename__ = 'rst_product_master_bk'

    PRODUCT_ID = Column(BIGINT(20), primary_key=True)
    PART_NO = Column(String(55))
    MODEL_ID_OLD = Column(String(255))
    SUB_CATEGORY = Column(String(55), server_default=text("'PRODUCT'"))
    SPECIFICATION = Column(String(255))
    DESCRIPTION = Column(String(255))
    REORDER_LVL = Column(BIGINT(20))
    MAX_ORDER = Column(BIGINT(20))
    MIN_ORDER = Column(BIGINT(20))
    SET_OF_UNIT = Column(BIGINT(20))
    LEAD_TIME = Column(BIGINT(20))
    UNIT_PRICE = Column(DECIMAL(11, 2))
    SELLING_PRICE = Column(DECIMAL(11, 2))
    CURRENCY_CODE = Column(String(20))
    DISTRIBUTOR_PRICE = Column(DECIMAL(11, 2))
    SHIPPING_PRICE = Column(DECIMAL(11, 2))
    DUMMY_PROD = Column(TINYINT(4), server_default=text("0"))
    DISCONTINUED = Column(TINYINT(4), server_default=text("0"))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    WARRANTY_MONTHS = Column(SMALLINT(6))
    SUPPLIER = Column(String(55))
    REPAIRABLE_PRICE = Column(DECIMAL(11, 2))
    REPAIR_WARRANTY = Column(BIGINT(20))
    REMARKS = Column(String(255))
    IMAGE = Column(LONGBLOB)
    PROD_SPEC = Column(LONGBLOB)
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    PART_NO_UP = Column(String(55))
    MODEL_ID = Column(BIGINT(20), nullable=False)
    RETAINED_PRODUCT_ID = Column(BIGINT(20))


class RstProductPlanMapping(Base):
    __tablename__ = 'rst_product_plan_mapping'

    ID = Column(Float(asdecimal=True), primary_key=True)
    PLAN_ID = Column(BIGINT(20), nullable=False)
    PRODUCT_TYPE = Column(String(255), nullable=False)
    PLAN_PRODUCT_DESCRIPTION = Column(String(255))


class RstProductcategoryMaster(Base):
    __tablename__ = 'rst_productcategory_master'

    NAME = Column(String(50), nullable=False)
    CODE = Column(BIGINT(20), primary_key=True)
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))


class RstProductvalidityMaster(Base):
    __tablename__ = 'rst_productvalidity_master'

    NAME = Column(String(50), nullable=False)
    CODE = Column(BIGINT(20), primary_key=True)
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))


t_rst_push_notify = Table(
    'rst_push_notify', metadata,
    Column('USER_ID', Float(asdecimal=True), nullable=False),
    Column('DEVICE_TYPE', String(20)),
    Column('GCM_API_KEY', String(256)),
    Column('GCM_DEVICE_ID', String(256)),
    Column('IOS_API_KEY', String(256)),
    Column('IOS_DEVICE_ID', String(256)),
    Column('FCM_APP_KEY', String(256)),
    Column('UPDATED_DT', DATETIME(fsp=6))
)


class RstQcMaster(Base):
    __tablename__ = 'rst_qc_master'

    QC_ID = Column(Float(asdecimal=True), primary_key=True)
    NAME = Column(String(50))


t_rst_quot_parts = Table(
    'rst_quot_parts', metadata,
    Column('QUOTATION_ID', BIGINT(20)),
    Column('JOB_PART_ID', BIGINT(20)),
    Column('COMPANY_ID', BIGINT(20))
)


class RstQuotation(Base):
    __tablename__ = 'rst_quotation'

    QUOTATION_ID = Column(BIGINT(20), primary_key=True)
    SERVICE_COST = Column(DECIMAL(12, 2))
    REMARKS = Column(String(255))
    STATUS = Column(BIGINT(20), server_default=text("-1"))
    QUOTE_REF = Column(String(255))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_BY = Column(BIGINT(20))
    TOTAL_PART_COST = Column(DECIMAL(11, 2))
    TOTAL_COST = Column(DECIMAL(11, 2))
    COMPANY_ID = Column(BIGINT(20))
    CURRENCY_CODE = Column(String(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_DT = Column(DATETIME(fsp=2))
    IS_CONSUMER_APPROVED = Column(TINYINT(4), server_default=text("0"))
    SR_ID = Column(Float(asdecimal=True))
    ACTIVE_APPROVAL_ID = Column(String(55))
    FINAL_APPROVAL_ID = Column(String(55))
    TAX_COMPANY_ID = Column(Float(asdecimal=True))
    MOVED_TO_NEW_QUOT_MODULE = Column(Float(asdecimal=True))
    STATUS_REVERT_REQUESTED_BY = Column(String(255))
    STATUS_REVERT_REQUESTED_ON = Column(DateTime)
    EXT_PROVIDER_REMARKS = Column(String(500))


class RstQuotationApproval(Base):
    __tablename__ = 'rst_quotation_approval'

    APPROVAL_ID = Column(Float(asdecimal=True), primary_key=True)
    APPROVER_ID = Column(Float(asdecimal=True), nullable=False)
    QUOTATION_ID = Column(Float(asdecimal=True))
    APPROVED_AMT = Column(DECIMAL(11, 2))
    AMT_CHARGABLE = Column(DECIMAL(11, 2))
    STATUS = Column(TINYINT(4), server_default=text("-1"))
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_DATE = Column(DATETIME(fsp=6))
    CREATED_DATE = Column(DATETIME(fsp=6))
    TOTAL_PARTS_COST = Column(DECIMAL(11, 2))
    SERVICE_COST = Column(DECIMAL(11, 2))
    DELIVERY_CHARGE = Column(DECIMAL(11, 2))
    TOTAL_COST = Column(DECIMAL(11, 2))
    ONSITE_COLLECTION_CHARGE = Column(DECIMAL(11, 2))
    OTHER_CHARGES = Column(DECIMAL(11, 2))
    FORWARDED_BY = Column(Float(asdecimal=True))
    SERVICE_COST_MARKUP = Column(DECIMAL(6, 2), server_default=text("1.00"))
    PARTS_COST_MARKUP = Column(DECIMAL(6, 2), server_default=text("1.00"))
    ONSITE_COST_MARKUP = Column(DECIMAL(6, 2), server_default=text("1.00"))
    LOGISTIC_COST_MARKUP = Column(DECIMAL(6, 2), server_default=text("1.00"))
    OTHER_CHARGES_DESCRIPTION = Column(String(255))
    IS_ACTIVE = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    APPROVAL_NO = Column(String(55))
    CREATED_BY = Column(Float(asdecimal=True))
    ACK_PDF = Column(LONGBLOB)
    STATUS_REVERT_REQUESTED_BY = Column(String(255))
    STATUS_REVERT_REQUESTED_ON = Column(DateTime)


t_rst_quotation_costs = Table(
    'rst_quotation_costs', metadata,
    Column('COST_ID', Float(asdecimal=True), nullable=False),
    Column('COST_NAME', String(20), nullable=False),
    Column('COST', Float(asdecimal=True), nullable=False),
    Column('CHARGED_BY', Float(asdecimal=True), nullable=False),
    Column('CHARGED_ON', DateTime, nullable=False),
    Column('QUOTATION_ID', Float(asdecimal=True), nullable=False),
    Column('SRP_RATE', Float(asdecimal=True), nullable=False, server_default=text("1")),
    Column('MARKED_UP_COST', Float(asdecimal=True)),
    Column('MARKED_UP_BY', Float(asdecimal=True)),
    Column('MARKED_UP_ON', DateTime),
    Column('IS_CLAIMABLE', Float(asdecimal=True), nullable=False, server_default=text("1"))
)


t_rst_recycle_model_price = Table(
    'rst_recycle_model_price', metadata,
    Column('MODEL_ID', Float(asdecimal=True)),
    Column('WORKING_PRICE', Float(asdecimal=True)),
    Column('COMPANY_ID', String(20)),
    Column('NON_WORKING_PRICE', Float(asdecimal=True))
)


class RstRecycleQuestion(Base):
    __tablename__ = 'rst_recycle_questions'

    SEQ = Column(DECIMAL(38, 0), primary_key=True)
    QUESTION = Column(String(1000))
    AMOUNT_DEPRECIATION = Column(DECIMAL(38, 0))
    DESCRIPTION = Column(String(1000))
    COMPANY_ID = Column(String(20))


class RstRecycleQuotation(Base):
    __tablename__ = 'rst_recycle_quotation'

    QUOTATION_ID = Column(BIGINT(20), primary_key=True)
    REQ_ID = Column(BIGINT(20))
    COMPANY_ID = Column(BIGINT(20))
    RECYCLE_PRICE = Column(DECIMAL(11, 2))
    REMARKS = Column(String(255))
    STATUS = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    CURRENCY_CODE = Column(String(20))
    REJECT_STATUS = Column(CHAR(1), server_default=text("'N'"))
    ACTIVE_STATUS = Column(CHAR(1), server_default=text("'Y'"))
    ACCEPTED_STATUS = Column(CHAR(1), server_default=text("'N'"))
    IS_APPROVED = Column(CHAR(1), server_default=text("'N'"))
    STATUS_BK = Column(BIGINT(20))


class RstRecycleRequest(Base):
    __tablename__ = 'rst_recycle_request'

    REQ_ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20))
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    EQ_STOCK_ID = Column(BIGINT(20))
    COUNTRY_CODE = Column(String(55))
    CITY = Column(String(55))
    ACCEPTED_COMPANY_ID = Column(BIGINT(20))
    ACTIVE_STATUS = Column(CHAR(1), server_default=text("'Y'"))
    APPROVED_QUOTATION_ID = Column(BIGINT(20))


t_rst_recycle_sign_up = Table(
    'rst_recycle_sign_up', metadata,
    Column('EMAIL_ADDRESS', String(255)),
    Column('MOBILE_NUMBER', DECIMAL(20, 0)),
    Column('USER_TYPE', String(10))
)


class RstReportConfig(Base):
    __tablename__ = 'rst_report_config'

    CONFIG_ID = Column(Float(asdecimal=True), primary_key=True)
    CONFIG_NAME = Column(String(55), nullable=False)
    DESCRIPTION = Column(String(255), nullable=False)
    MAIN_VIEW_NAME = Column(String(55), nullable=False)
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))


class RstReqPart(Base):
    __tablename__ = 'rst_req_parts'

    PRODUCT_ID = Column(BIGINT(20))
    REQUEST_QTY = Column(INTEGER(11))
    APPROVED_QTY = Column(INTEGER(11))
    SUPPLIER_ID = Column(BIGINT(20))
    DESCRIPTION = Column(String(255))
    MR_ID = Column(String(55), primary_key=True, nullable=False)
    PART_PRICE = Column(DECIMAL(11, 2))
    COMPANY_ID = Column(BIGINT(20))
    REQ_PART_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    CURRENCY_CODE = Column(String(20))


class RstRequisition(Base):
    __tablename__ = 'rst_requisition'

    MR_ID = Column(String(55), primary_key=True)
    REQ_DT = Column(DATETIME(fsp=2))
    STATUS = Column(String(55))
    CHARGE_DEPT = Column(String(55))
    REMARKS = Column(String(255))
    REQ_BY = Column(String(55))
    VOID_REJECTED_REASON = Column(String(255))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    APPROVED_BY = Column(BIGINT(20))
    APPROVED_DT = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))


class RstReview(Base):
    __tablename__ = 'rst_reviews'
    __table_args__ = (
        Index('RST_REVIEWS_UK1', 'EQ_STOCK_ID', 'USER_ID', unique=True),
    )

    EQ_STOCK_ID = Column(Float(asdecimal=True), nullable=False)
    USER_ID = Column(Float(asdecimal=True), nullable=False)
    REVIEW_ID = Column(Float(asdecimal=True), primary_key=True)
    RATING = Column(Float(asdecimal=True))
    REVIEW = Column(String(4000))


class RstRma(Base):
    __tablename__ = 'rst_rma'

    RMA_ID = Column(BIGINT(20), nullable=False)
    RMA_NO = Column(String(55), primary_key=True)
    BATCH_ID = Column(String(55))
    COMMENTS = Column(String(255))
    TOT_QTY_RTN = Column(SMALLINT(6))
    RECEIVED_DT = Column(DATETIME(fsp=2))
    RECEIVED_BY = Column(String(55))
    RMA_STATUS = Column(String(55))
    USER_ID = Column(BIGINT(20))
    CUSTOMER_TYPE = Column(CHAR(1))
    CUST_REJECTED_REASON = Column(String(55))
    CUST_REJECTED_COMMENTS = Column(String(255))
    REJECTED_REASON = Column(String(55))
    REJECTED_COMMENTS = Column(String(255))
    TOTAL_REPAIR_ESTIMATE = Column(DECIMAL(11, 2))
    ACTUAL_INVOICE_NO = Column(String(55))
    STATUS_UPDATED_BY = Column(BIGINT(20))
    STATUS_UPDATED_DT = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))


class RstRmaPart(Base):
    __tablename__ = 'rst_rma_parts'

    RMA_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    STOCK_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    PRODUCT_ID = Column(BIGINT(20))
    SERIAL_NO = Column(String(55))
    INVOICE_NO = Column(String(55))
    QTY = Column(BIGINT(20))
    QTY_RECEIVED = Column(BIGINT(20))
    IN_WARRANTY = Column(BIGINT(20))
    PROPBLEM_DESC = Column(String(1500))
    REMARKS = Column(String(1500))
    VOID_REASON = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))
    EQ_STOCK_ID = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    JOB_ID = Column(String(55))


class RstRoleFunctionMap(Base):
    __tablename__ = 'rst_role_function_map'

    ROLE_FUNCTION_MAP_ID = Column(Float(asdecimal=True), primary_key=True)
    ROLE_NAME = Column(String(55))
    FUNCTION_CODE = Column(String(55))
    IS_ACTIVE = Column(TINYINT(4), server_default=text("1"))
    IS_PAYABLE = Column(Float(asdecimal=True), server_default=text("0"))
    PAYMENT_DONE = Column(Float(asdecimal=True), server_default=text("0"))
    IS_EDITABLE = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    IS_PRIMARY_ROLE = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    SYSTEM_CREATED = Column(BIGINT(20), server_default=text("0"))
    COMPANY_ID = Column(BIGINT(20))


class RstRole(Base):
    __tablename__ = 'rst_roles'

    ROLE_ID = Column(BIGINT(20), primary_key=True)
    ROLE_NAME = Column(String(55), nullable=False, unique=True)
    ROLE_DESCRIPTION = Column(String(255))
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    IS_PARENT = Column(TINYINT(4), server_default=text("0"))
    DISPLAY_NAME = Column(String(55))
    IS_ADMIN_ROLE = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    COMPANY_ID = Column(Float(asdecimal=True))


t_rst_roles_child = Table(
    'rst_roles_child', metadata,
    Column('PARENT_ROLE_ID', String(55), nullable=False),
    Column('CHILD_ROLE_ID', String(55), nullable=False),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Index('RST_ROLES_CHILD_UNIQUE1', 'PARENT_ROLE_ID', 'CHILD_ROLE_ID', unique=True)
)


class RstRpCriterion(Base):
    __tablename__ = 'rst_rp_criteria'

    CRITERIA_ID = Column(Float(asdecimal=True), primary_key=True)
    FIELD_NAME = Column(String(55))
    FIELD_TYPE = Column(String(55))
    CRITERIA = Column(String(20))
    RANGE_FROM = Column(String(55))
    RANGE_TO = Column(String(55))
    CRT_NAME = Column(String(55), unique=True)
    VALUE = Column(String(20))


t_rst_rp_points_redemption = Table(
    'rst_rp_points_redemption', metadata,
    Column('POINTS_ID', Float(asdecimal=True)),
    Column('POINTS_REDEEMED', Float(asdecimal=True)),
    Column('REDEMPTION_ID', Float(asdecimal=True))
)


t_rst_rp_redemption_catalogue = Table(
    'rst_rp_redemption_catalogue', metadata,
    Column('ITEM_ID', BIGINT(20), nullable=False),
    Column('POINTS', BIGINT(20)),
    Column('DESCRIPTION', String(512)),
    Column('CATEGORY', String(255)),
    Column('COUNTRY_CODE', String(5)),
    Column('REDEMPTION_ADDRESS', String(2024)),
    Column('COMPANY_ID', BIGINT(20)),
    Column('CREATED_DATE', DATETIME(fsp=6)),
    Column('UPDATED_DATE', DATETIME(fsp=6)),
    Column('START_DATE', DateTime),
    Column('END_DATE', DateTime),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1")),
    Column('REDEMPTION_VALIDITY_DAYS', Float(asdecimal=True)),
    Column('IS_LAUNCHED', Float(asdecimal=True), server_default=text("0")),
    Column('CAPPED_TYPE', String(20), server_default=text("'PERCENTAGE'")),
    Column('CAPPED_VALUE', BIGINT(20)),
    Column('LENGTH', DECIMAL(5, 2)),
    Column('WIDTH', DECIMAL(5, 2)),
    Column('HEIGHT', DECIMAL(5, 2)),
    Column('WEIGHT', DECIMAL(5, 2)),
    Column('LINKED_ITEM_ID', BIGINT(20))
)


t_rst_rp_redemption_history = Table(
    'rst_rp_redemption_history', metadata,
    Column('REDEMPTION_ID', BIGINT(20), nullable=False),
    Column('USER_ID', BIGINT(20)),
    Column('ITEM_ID', BIGINT(20)),
    Column('REDEEMED_DATE', DATETIME(fsp=6)),
    Column('REDEMPTION_EXPIRY_DATE', DateTime),
    Column('COLLECTED_DATE', DateTime),
    Column('FIRST_NAME', String(55)),
    Column('LAST_NAME', String(55)),
    Column('CONTACT_NUMBER', String(20)),
    Column('EMAIL_ID', String(55)),
    Column('IC_NUMBER', String(20)),
    Column('DISCOUNT_TAKEN', TINYINT(4), server_default=text("0")),
    Column('PAYMENT_INVOICE_NUMBER', String(55))
)


t_rst_rp_redemption_location = Table(
    'rst_rp_redemption_location', metadata,
    Column('ITEM_ID', BIGINT(20)),
    Column('ADDRESS_ID', BIGINT(20))
)


class RstRpRewardPoint(Base):
    __tablename__ = 'rst_rp_reward_points'

    POINTS_ID = Column(Float(asdecimal=True), primary_key=True)
    USER_ID = Column(Float(asdecimal=True))
    POINTS_ISSUED = Column(Float(asdecimal=True))
    APPLIED_RULE_NAME = Column(String(55))
    ISSUED_DATE = Column(DateTime)
    EXPIRY_DATE = Column(String(20))
    POINTS_USED = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))


class RstRpRuleCriterion(Base):
    __tablename__ = 'rst_rp_rule_criteria'

    RULE_NAME = Column(String(55), primary_key=True, nullable=False)
    CRT_NAME = Column(String(55), primary_key=True, nullable=False)
    ORDER1 = Column(Float(asdecimal=True))


class RstRpRule(Base):
    __tablename__ = 'rst_rp_rules'

    RULE_ID = Column(Float(asdecimal=True), primary_key=True)
    RULE_NAME = Column(String(20), nullable=False)
    RULE_DESC = Column(String(2000))
    POINTS = Column(Float(asdecimal=True), nullable=False)
    POINTS_VALID_FOR_DAYS = Column(Float(asdecimal=True), nullable=False)
    COMPANY_ID = Column(Float(asdecimal=True))


t_rst_sales_parts = Table(
    'rst_sales_parts', metadata,
    Column('PART_NO', String(55), nullable=False),
    Column('DESCRIPTION', String(55)),
    Column('HSN_CODE', String(20)),
    Column('BASE_PRICE', DECIMAL(11, 2)),
    Column('CUSTOMER_PRICE', BIGINT(20)),
    Column('STOCK_AVAILABILITY', String(20)),
    Column('ETD', DateTime),
    Column('CGST', DECIMAL(11, 2)),
    Column('SGST', DECIMAL(11, 2)),
    Column('PRODUCT', String(50)),
    Column('MODELNO', String(50)),
    Column('COLOR', String(25)),
    Column('QTY', Float(asdecimal=True)),
    Column('YEAR', DECIMAL(11, 2)),
    Column('TYPE', String(10))
)


t_rst_sales_parts_used = Table(
    'rst_sales_parts_used', metadata,
    Column('SALES_PARTS_ID', BIGINT(20), nullable=False),
    Column('QTY', BIGINT(20)),
    Column('REMARKS', String(2000)),
    Column('PCB_LOCATION', String(55)),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('PART_SERIAL_NO', String(100)),
    Column('PART_NO', String(55)),
    Column('USER_ID', BIGINT(20)),
    Column('EW_START_DT', DateTime),
    Column('EW_END_DT', DateTime)
)


class RstSaleschannelMaster(Base):
    __tablename__ = 'rst_saleschannel_master'

    NAME = Column(String(50), nullable=False)
    CODE = Column(BIGINT(20), primary_key=True)
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))
    SALES_DT = Column(DateTime)


t_rst_salesinvoice = Table(
    'rst_salesinvoice', metadata,
    Column('ISALES_ID', BIGINT(20), nullable=False),
    Column('IINVOICE_NO', String(55)),
    Column('USER_ID', BIGINT(20)),
    Column('CUSTOMER_TYPE', CHAR(1)),
    Column('DELIVERY_CHRGS', DECIMAL(11, 2)),
    Column('TOTAL_AMT', DECIMAL(11, 2)),
    Column('PAYMENT_MODE', String(55)),
    Column('SHIPPING_MTHD', String(255)),
    Column('SHIPPING_ADDR1', String(255)),
    Column('SHIPPING_ADDR2', String(255)),
    Column('SALES_BY', BIGINT(20)),
    Column('REMARKS', String(4000)),
    Column('GST_AMT', DECIMAL(11, 2)),
    Column('SUB_TOTAL', DECIMAL(11, 2)),
    Column('RECEIPT_NO', String(55)),
    Column('COMPANY_ID', BIGINT(20)),
    Column('PAYMENT_MODE2', String(55)),
    Column('MODE1_AMOUNT', DECIMAL(10, 2)),
    Column('MODE2_AMOUNT', DECIMAL(10, 2)),
    Column('STATUS_CODE', String(20)),
    Column('TRANS_REF', String(55)),
    Column('CURRENCY_CODE', String(20)),
    Column('DISCOUNT', DECIMAL(11, 2)),
    Column('PARTS_COST', DECIMAL(11, 2)),
    Column('SERVICE_COST', DECIMAL(11, 2)),
    Column('OTHER_COST', DECIMAL(11, 2)),
    Column('CGST', DECIMAL(11, 2)),
    Column('SGST', DECIMAL(11, 2)),
    Column('CGST_AMT', DECIMAL(11, 2)),
    Column('SGST_AMT', String(11)),
    Column('TCRNO', String(100)),
    Column('TCRDATE', DateTime),
    Column('DISCOUNT_ID', Float(asdecimal=True)),
    Column('TRANSPORT_COST', DECIMAL(11, 2)),
    Column('ASC_LABR_DISCNT', DECIMAL(11, 2)),
    Column('ASC_TRANPDISCNT', DECIMAL(11, 2)),
    Column('ASC_OTHERDISCNT', DECIMAL(11, 2)),
    Column('APPLE_LABRDISCNT', DECIMAL(11, 2)),
    Column('APPLE_TRANSDISCNT', DECIMAL(11, 2)),
    Column('APPLE_OTHERDISCNT', DECIMAL(11, 2)),
    Column('ASC_PARTDISCNT', DECIMAL(11, 2)),
    Column('APPLE_PARTSDISCNT', DECIMAL(11, 2)),
    Column('ADV_AMT', DECIMAL(11, 2)),
    Column('GSTIN', String(50)),
    Column('PAN', String(50)),
    Column('WARRNTY_ID', DECIMAL(11, 2)),
    Column('TCRAMT', DECIMAL(10, 2)),
    Column('SALES_DT', DateTime)
)


class RstSalesorder(Base):
    __tablename__ = 'rst_salesorder'

    SALES_ID = Column(BIGINT(20), primary_key=True)
    INVOICE_NO = Column(String(55))
    USER_ID = Column(BIGINT(20))
    CUSTOMER_TYPE = Column(CHAR(1), server_default=text("'W'"))
    DELIVERY_CHRGS = Column(DECIMAL(11, 2))
    TOTAL_AMT = Column(DECIMAL(11, 2))
    PAYMENT_MODE = Column(String(55))
    SHIPPING_MTHD = Column(String(255))
    SHIPPING_ADDR1 = Column(String(255))
    SHIPPING_ADDR2 = Column(String(255))
    SALES_BY = Column(BIGINT(20))
    SALES_DT = Column(DATETIME(fsp=2))
    REMARKS = Column(String(4000))
    GST_AMT = Column(DECIMAL(11, 2))
    SUB_TOTAL = Column(DECIMAL(11, 2))
    RECEIPT_NO = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))
    PAYMENT_MODE2 = Column(String(55))
    MODE1_AMOUNT = Column(DECIMAL(10, 2))
    MODE2_AMOUNT = Column(DECIMAL(10, 2))
    JOB_ID = Column(String(55))
    STATUS_CODE = Column(String(20))
    TRANS_REF = Column(String(55))
    CURRENCY_CODE = Column(String(20))
    DISCOUNT = Column(DECIMAL(11, 2))
    PARTS_COST = Column(DECIMAL(11, 2))
    SERVICE_COST = Column(DECIMAL(11, 2))
    OTHER_COST = Column(DECIMAL(11, 2))
    CGST = Column(DECIMAL(11, 2))
    SGST = Column(DECIMAL(11, 2))
    CGST_AMT = Column(DECIMAL(11, 2))
    SGST_AMT = Column(String(11))
    TCRNO = Column(String(100))
    TCRDATE = Column(DateTime)
    DISCOUNT_ID = Column(Float(asdecimal=True))
    TRANSPORT_COST = Column(DECIMAL(11, 2))
    ASC_LABR_DISCNT = Column(DECIMAL(11, 2))
    ASC_TRANPDISCNT = Column(DECIMAL(11, 2))
    ASC_OTHERDISCNT = Column(DECIMAL(11, 2))
    APPLE_LABRDISCNT = Column(DECIMAL(11, 2))
    APPLE_TRANSDISCNT = Column(DECIMAL(11, 2))
    APPLE_OTHERDISCNT = Column(DECIMAL(11, 2))
    ASC_PARTDISCNT = Column(DECIMAL(11, 2))
    APPLE_PARTSDISCNT = Column(DECIMAL(11, 2))
    ADV_AMT = Column(DECIMAL(11, 2))
    GSTIN = Column(String(50))
    PAN = Column(String(50))


t_rst_serial_no_update_track = Table(
    'rst_serial_no_update_track', metadata,
    Column('OLD_SERIAL_NO', String(255)),
    Column('EQ_STOCK_ID', Float(asdecimal=True)),
    Column('EQ_STOCK_ID_ATEND', Float(asdecimal=True)),
    Column('OLD_BRAND_NAME', String(255)),
    Column('OLD_MODEL_NAME', String(255)),
    Column('OLD_PRODUCT_TYPE', String(255)),
    Column('NEW_SERIAL_NO', String(255)),
    Column('NEW_BRAND_NAME', String(255)),
    Column('NEW_MODEL_NAME', String(255)),
    Column('NEW_PRODUCT_TYPE', String(255)),
    Column('OLD_PRODUCT_ID', Float(asdecimal=True)),
    Column('NEW_PRODUCT_ID', Float(asdecimal=True)),
    Column('RESULT', String(55)),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('USER_ID', Float(asdecimal=True)),
    Column('REQ_DATE', DateTime),
    Column('TRACK_ID', String(55)),
    Column('CONSUMER_ID', String(20))
)


class RstSery(Base):
    __tablename__ = 'rst_series'

    SERIES_ID = Column(DECIMAL(30, 0), primary_key=True)
    SERIES_NAME = Column(String(40))
    BRAND_ID = Column(DECIMAL(30, 0))
    PRODUCT_TYPE = Column(String(55))
    PRODUCT_TYPE_UP = Column(String(55))


class RstSeries1(Base):
    __tablename__ = 'rst_series1'

    SERIES_ID = Column(DECIMAL(30, 0), primary_key=True)
    SERIES_NAME = Column(String(40))
    BRAND_ID = Column(DECIMAL(30, 0))


t_rst_service_center_issue = Table(
    'rst_service_center_issue', metadata,
    Column('FIX_ID', Float(asdecimal=True)),
    Column('ISSUE_ID', Float(asdecimal=True)),
    Column('SERVICE_CENTER_ID', Float(asdecimal=True)),
    Column('CURRENCY', String(20)),
    Column('ONSITE_COST', Float(asdecimal=True)),
    Column('PICKUP_COST', Float(asdecimal=True)),
    Column('FIX_PRICE', Float(asdecimal=True)),
    Column('BRAND_ID', Float(asdecimal=True))
)


t_rst_service_center_issue_new = Table(
    'rst_service_center_issue_new', metadata,
    Column('FIX_ID', Float(asdecimal=True)),
    Column('ISSUE_ID', Float(asdecimal=True)),
    Column('SERVICE_CENTER_ID', Float(asdecimal=True)),
    Column('CURRENCY', String(20)),
    Column('ONSITE_COST', Float(asdecimal=True)),
    Column('PICKUP_COST', Float(asdecimal=True)),
    Column('FIX_PRICE', Float(asdecimal=True)),
    Column('BRAND_ID', Float(asdecimal=True))
)


class RstServiceCtrIssueRating(Base):
    __tablename__ = 'rst_service_ctr_issue_rating'

    USER_ID = Column(Float(asdecimal=True), primary_key=True)
    RATING = Column(String(20))
    DESCRIPTION = Column(String(20))
    SERVICE_CENTER_ID = Column(Float(asdecimal=True))


t_rst_service_ctr_issue_ratingn = Table(
    'rst_service_ctr_issue_ratingn', metadata,
    Column('USER_ID', Float(asdecimal=True), nullable=False),
    Column('RATING', String(20)),
    Column('DESCRIPTION', String(20)),
    Column('SERVICE_CENTER_ID', Float(asdecimal=True))
)


t_rst_service_request = Table(
    'rst_service_request', metadata,
    Column('CUSTOMER_TYPE', String(55)),
    Column('DATE_IN', DATETIME(fsp=2)),
    Column('CLOSE_STATUS', TINYINT(4), server_default=text("0")),
    Column('BATCH_ID', String(55)),
    Column('USER_ID', BIGINT(20)),
    Column('PRODUCT_ID', BIGINT(20)),
    Column('PRODUCT_DESC', String(255)),
    Column('FAILURE_DESC', String(255)),
    Column('COMPANY_ID', BIGINT(20)),
    Column('EQ_STOCK_ID', BIGINT(20)),
    Column('REMARKS', String(4000)),
    Column('STATUS', String(55)),
    Column('JOB_ID', String(55)),
    Column('ASSIGNED_TO', Float(asdecimal=True)),
    Column('ASSIGNED_BY', Float(asdecimal=True)),
    Column('APPOINTMENT_DT', DATETIME(fsp=2)),
    Column('SR_NUMBER', String(55), nullable=False, unique=True),
    Column('CREATED_BY', BIGINT(20), nullable=False),
    Column('CREATED_DT', DATETIME(fsp=2), nullable=False),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2)),
    Column('CONTACT_NO', String(55)),
    Column('USER_NAME', String(255)),
    Column('FAILURE_DESC_OTHERS', String(4000)),
    Column('PHONE_NO', String(55)),
    Column('ADDRESS_LINE1', String(255)),
    Column('ADDRESS_LINE2', String(55)),
    Column('CITY', String(55)),
    Column('STATE', String(100)),
    Column('POSTAL_CODE', String(20)),
    Column('COUNTRY_CODE', String(55)),
    Column('PRODUCT_STATUS', Float(asdecimal=True), nullable=False, server_default=text("0")),
    Column('ACTIVE_STATUS', TINYINT(4), nullable=False, server_default=text("1")),
    Column('COLLECTED_BY', String(50)),
    Column('COLLECTED_DT', DATETIME(fsp=2)),
    Column('SR_ID', Float(asdecimal=True)),
    Column('MIGRATED_SR_NO', Float(asdecimal=True)),
    Column('STATUS_REVERT_REQUESTED_BY', String(255)),
    Column('STATUS_REVERT_REQUESTED_ON', DateTime),
    Column('FAILURE_DESC_BK', String(255)),
    Column('PHONE_NO_COUNTRY_CODE', String(5)),
    Column('SENT_TO_WAREHOUSE', String(20), server_default=text("'N'")),
    Column('SR_TYPE', String(20)),
    Column('RECEIVED_DT', DATETIME(fsp=6)),
    Column('INWARD_TYPE', String(20)),
    Column('CURRENCY_CODE', String(20)),
    Column('TOKEN_NO', String(100))
)


class RstServicecategoryMaster(Base):
    __tablename__ = 'rst_servicecategory_master'

    NAME = Column(String(50), nullable=False)
    CODE = Column(BIGINT(20), primary_key=True)
    TYPE = Column(String(50), nullable=False)
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("0"))


class RstShipment(Base):
    __tablename__ = 'rst_shipment'

    SHIP_ID = Column(BIGINT(20), primary_key=True)
    SHIP_DATE = Column(DATETIME(fsp=2))
    DEALER_CD = Column(String(55))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    SHIPMENT_REF = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))


class RstShipmentItem(Base):
    __tablename__ = 'rst_shipment_items'

    SHIP_ITEMS_ID = Column(BIGINT(20), primary_key=True)
    SHIP_ID = Column(BIGINT(20))
    JOB_ID = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))


t_rst_shipment_products = Table(
    'rst_shipment_products', metadata,
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('CREATED_BY', Float(asdecimal=True)),
    Column('LOGISTICS_ID', Float(asdecimal=True), nullable=False),
    Column('EQ_STOCK_ID', Float(asdecimal=True), nullable=False),
    Column('CREATED_DATE', DateTime)
)


class RstSmsAudit(Base):
    __tablename__ = 'rst_sms_audit'

    SMS_ID = Column(String(20), primary_key=True)
    COMPANY_ID = Column(Float(asdecimal=True))
    MESSAGE = Column(String(4000))
    SENT_DATE = Column(DATETIME(fsp=6))
    SMS_CREDIT_USED = Column(Float(asdecimal=True))
    DIRECTION = Column(String(5), nullable=False, server_default=text("'OUT'"))
    SENT_STATUS = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    SMS_TYPE = Column(String(55))
    SMS_TO = Column(String(20), nullable=False)


class RstStockAdjustInfo(Base):
    __tablename__ = 'rst_stock_adjust_info'

    STOCK_ADJUST_INFO_ID = Column(BIGINT(20), primary_key=True)
    PRODUCT_ID = Column(BIGINT(20))
    PHY_BALANCE = Column(BIGINT(20))
    SYS_BALANCE = Column(BIGINT(20))
    ADJUSTMENT_VALUE = Column(BIGINT(20))
    STATUS = Column(BIGINT(20))
    ADJUSTMENT_DT = Column(DATETIME(fsp=2))
    ADJUSTMENT_BY = Column(String(45))
    ADJUSTMENT_FILE_NAME = Column(String(45))
    COMPANY_ID = Column(BIGINT(20))
    INVENTORY_ID = Column(BIGINT(20))


t_rst_tax_configuration = Table(
    'rst_tax_configuration', metadata,
    Column('TAX_CONFIGURATION_ID', BIGINT(20), nullable=False),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('TAX_NAME', String(55)),
    Column('VALUE', String(55)),
    Column('DESCRIPTION', String(255)),
    Column('TAX_PERCENTAGE', String(10)),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1")),
    Column('CREATED_BY', BIGINT(20)),
    Column('CREATED_DT', DATETIME(fsp=2)),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2))
)


t_rst_tax_form_companytype_cfg = Table(
    'rst_tax_form_companytype_cfg', metadata,
    Column('COMPANY_TYPE', String(55)),
    Column('FORM_TYPE', String(55)),
    Column('FORM_TYPE_DESCRIPTION', String(55)),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1"))
)


t_rst_tax_mappings = Table(
    'rst_tax_mappings', metadata,
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('FORM_TYPE', String(55)),
    Column('TAX_CONFIGURATION_ID', BIGINT(20))
)


class RstUploadHistory(Base):
    __tablename__ = 'rst_upload_history'

    UPLOAD_ID = Column(BIGINT(20), primary_key=True)
    UPLOAD_FILE_NAME = Column(String(255))
    UPLOAD_TYPE = Column(String(55))
    UPLOAD_DATETIME = Column(DATETIME(fsp=2))
    UPLOAD_STATUS = Column(TINYINT(4), server_default=text("0"))
    UPLOAD_FINISHED_TIME = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))
    UPLOADED_BY = Column(BIGINT(20))
    TOTAL_RECORDS = Column(BIGINT(20))
    SUCCESS_COUNT = Column(BIGINT(20))
    SKIPPED_COUNT = Column(BIGINT(20))
    FAILED_COUNT = Column(BIGINT(20))
    CURRENT_ROW_PROCESSED = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    HEADER_MAPPINGS = Column(String(500))


class RstUploadMetadatum(Base):
    __tablename__ = 'rst_upload_metadata'

    METADATA_ID = Column(BIGINT(20), primary_key=True)
    UPLOAD_TYPE_ID = Column(BIGINT(20), nullable=False)
    FIELD_NAME = Column(String(55))
    TABLE_NAME = Column(String(55))
    COLUMN_NAME = Column(String(55))
    REF_TABLE_NAME = Column(String(55))
    REF_COLUMN_NAME = Column(String(55))
    ORDER_BY = Column(String(55))


class RstUploadType(Base):
    __tablename__ = 'rst_upload_type'

    UPLOAD_TYPE_ID = Column(BIGINT(20), primary_key=True)
    UPLOAD_TYPE = Column(String(55))
    ACTIVE_STATUS = Column(BIGINT(20))


t_rst_upload_xls_template = Table(
    'rst_upload_xls_template', metadata,
    Column('UPLOAD_TYPE', String(20)),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('TEMPLATE', LONGTEXT),
    Column('ACTIVE_STATUS', TINYINT(4), server_default=text("1"))
)


class RstUserRoleMap(Base):
    __tablename__ = 'rst_user_role_map'

    USER_ROLE_MAP_ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20))
    ROLE_NAME = Column(String(50))
    COMPANY_ID = Column(BIGINT(20))


class RstUsersMobileinfo(Base):
    __tablename__ = 'rst_users_mobileinfo'

    FB_AUTH_TOKEN = Column(String(255))
    FB_ID = Column(String(255))
    DEVICE_TOKEN = Column(String(255))
    DEVICE_TYPE = Column(String(1))
    GOOGLE_TOKEN = Column(String(255))
    MOBILEINFO_ID = Column(Float(asdecimal=True), primary_key=True)
    SESSION_TOKEN = Column(String(255))
    GOOGLE_ID_TOKEN = Column(String(512))
    GOOGLE_TOKEN_TYPE = Column(String(255))
    USER_IMAGE = Column(LONGBLOB)
    IP = Column(String(30))
    UPDATED_DT = Column(DATETIME(fsp=6))
    LOCATION = Column(String(100))


class RstWarrantyBk(Base):
    __tablename__ = 'rst_warranty_bk'

    WARRNTY_ID = Column(BIGINT(20), primary_key=True)
    WARRNTY_REF = Column(String(55))
    EQ_STOCK_ID = Column(BIGINT(20), nullable=False)
    PURCHASE_DT = Column(DateTime)
    PROD_DATE_CODE = Column(String(255))
    USER_ID = Column(BIGINT(20))
    IN_WARRANTY = Column(BIGINT(20))
    REMARKS = Column(String(4000))
    VOID_REASON = Column(String(4000))
    REGISTERED_BY = Column(BIGINT(20))
    REGISTERED_BY_TYPE = Column(String(55))
    WARRENTY_EXP_DT = Column(DateTime)
    PURCHASE_FROM = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))
    COUNTRY_CODE = Column(String(55))
    WARRANTY_NO = Column(String(55))
    REGISTERED_DT = Column(DATETIME(fsp=6))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    FILE_UPLOAD_1 = Column(LONGBLOB)
    FILE_UPLOAD_2 = Column(LONGBLOB)
    FILE_UPLOAD_3 = Column(LONGBLOB)
    FILE_UPLOAD_1_NAME = Column(String(55))
    FILE_UPLOAD_2_NAME = Column(String(55))
    FILE_UPLOAD_3_NAME = Column(String(55))
    WARRANTY_MONTHS = Column(BIGINT(20))
    UPDATED_BY = Column(Float(asdecimal=True))
    EMAIL_SENT = Column(TINYINT(4), server_default=text("0"))
    CURRENCY_CODE = Column(String(20))
    PRODUCT_COST = Column(String(20))
    WARRANTY_TYPE = Column(String(3), nullable=False, server_default=text("'MW'"))
    EW_TYPE = Column(Float(asdecimal=True))
    EW_CATEGORY = Column(Float(asdecimal=True))
    WARRANTY_STATUS = Column(String(55))
    INVOICE_NUMBER = Column(String(55))
    ADDITIONAL_INFO = Column(String(55))
    CREATED_BY = Column(BIGINT(20))
    OLD_USER_ID = Column(BIGINT(20))
    IS_UPDATED = Column(TINYINT(4))
    EW_CATEGORY_DESC = Column(String(200))
    ORIG_PRODUCT_COST = Column(Float(asdecimal=True))
    WARRANTY_START_DATE = Column(DateTime)
    OLD_PURCHASE_DT = Column(DateTime)
    OLD_REGD_DT = Column(DateTime)
    UPDATED_DT = Column(DateTime)
    OLD_WARRENTY_EXP_DATE = Column(DateTime)
    OH_HOLD_MIGRATION = Column(String(20))
    MIGRATED_WARRANTY_NO = Column(Float(asdecimal=True))
    PARENT_WARRANTY_ID = Column(Float(asdecimal=True))
    EW_TYPE_BK = Column(Float(asdecimal=True))
    EW_CATEGORY_BK = Column(Float(asdecimal=True))
    REACTIVATED_ON = Column(DateTime)


t_rst_warranty_claim_balance = Table(
    'rst_warranty_claim_balance', metadata,
    Column('USER_ID', BIGINT(20), nullable=False, unique=True),
    Column('WARRANTY_ID', INTEGER(11)),
    Column('EXT_WARRANTY_PROVIDER_ID', INTEGER(11)),
    Column('EQ_STOCK_ID', INTEGER(11)),
    Column('WARRANTY_NO', INTEGER(11)),
    Column('WARRANTY_MONTHS', INTEGER(11)),
    Column('EW_PURCHASED_DATE', Date),
    Column('EW_START_DATE', Date),
    Column('EW_EXPIRY_DATE', Date),
    Column('CONSUMER_NAME', Text),
    Column('EMAIL_ID', Text),
    Column('EXT_WARRANTY_PROVIDER_NAME', Text),
    Column('BRAND_NAME', Text),
    Column('MODEL_NAME', Text),
    Column('PRODUCT_TYPE', Text),
    Column('SERIAL_NO', INTEGER(11)),
    Column('TOTAL_CLAIMED_AMT', INTEGER(11)),
    Column('MAX_CLAIMABLE_AMT', INTEGER(11)),
    Column('CLAIMABLIE_BALANCE', INTEGER(11))
)


class RstWarrantyOnHold(Base):
    __tablename__ = 'rst_warranty_on_hold'

    WARRNTY_HOLD_ID = Column(BIGINT(20), primary_key=True)
    WARRNTY_REF = Column(String(55))
    PURCHASE_DT = Column(DateTime)
    PROD_DATE_CODE = Column(String(255))
    USER_ID = Column(BIGINT(20))
    IN_WARRANTY = Column(BIGINT(20))
    REMARKS = Column(String(4000))
    VOID_REASON = Column(String(4000))
    REGISTERED_BY = Column(BIGINT(20))
    REGISTERED_BY_TYPE = Column(String(55))
    WARRENTY_EXP_DT = Column(DateTime)
    PURCHASE_FROM = Column(String(55))
    COMPANY_ID = Column(BIGINT(20))
    COUNTRY_CODE = Column(String(55))
    WARRANTY_NO = Column(String(55))
    REGISTERED_DT = Column(DATETIME(fsp=6))
    WARRANTY_MONTHS = Column(BIGINT(20))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    FILE_UPLOAD_1 = Column(LONGBLOB)
    FILE_UPLOAD_2 = Column(LONGBLOB)
    FILE_UPLOAD_3 = Column(LONGBLOB)
    FILE_UPLOAD_1_NAME = Column(String(55))
    FILE_UPLOAD_2_NAME = Column(String(55))
    FILE_UPLOAD_3_NAME = Column(String(55))
    WARRANTY_PERIOD_UNIT = Column(String(20), nullable=False, server_default=text("'MONTHS'"))
    UPDATED_BY = Column(Float(asdecimal=True))
    EMAIL_SENT = Column(TINYINT(4), server_default=text("0"))
    REVIEW_ID = Column(Float(asdecimal=True))
    CURRENCY_CODE = Column(String(20))
    PRODUCT_COST = Column(String(20))
    WARRANTY_TYPE = Column(String(2), nullable=False, server_default=text("'MW'"))
    EW_TYPE = Column(String(80))
    EW_CATEGORY = Column(String(80))
    MANU_WARRANTY_ID = Column(Float(asdecimal=True))
    BRAND = Column(String(55))
    MODEL = Column(String(55))
    PRODUCT_TYPE = Column(String(55))
    CREATED_BY = Column(Float(asdecimal=True))
    NULL_BRAND_PATCHED = Column(String(20))


t_rst_yarraa_services = Table(
    'rst_yarraa_services', metadata,
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('ACCEPT_ONLINE_SR', TINYINT(4), nullable=False, server_default=text("0")),
    Column('ACCEPT_ONLINE_EW_PURCHASE', TINYINT(4), nullable=False, server_default=text("0"))
)


t_ssew_batch_data_status = Table(
    'ssew_batch_data_status', metadata,
    Column('WARRANTY_NO', String(55)),
    Column('EQ_STOCK_ID', String(55)),
    Column('W_DUMMY', String(255)),
    Column('WARRNTY_REF', String(55)),
    Column('PURCHASE_DT', DateTime),
    Column('WARRANTY_PERIOD', Float(asdecimal=True)),
    Column('EXD_WARRANTY_PERIOD', Float(asdecimal=True)),
    Column('RST_CODE_DESCRIPTION', String(50)),
    Column('COMPANY_NAME', String(255)),
    Column('IC_NO_DOC_NO', String(55)),
    Column('FIRST_NAME', String(55)),
    Column('EMAIL_ID', String(255)),
    Column('ADDRESSLINE_1', String(255)),
    Column('ADDRESSLINE_2', String(255)),
    Column('ADDRESSLINE_3', String(255)),
    Column('POSTCODE', String(20)),
    Column('COUNTRY', String(50)),
    Column('PHONE_NO', String(55)),
    Column('MOBILE', String(55)),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('CODE_ID', Float(asdecimal=True)),
    Column('VALUE', String(100)),
    Column('USER_ID', Float(asdecimal=True)),
    Column('STATUS', String(20)),
    Column('REMARKS', String(2000)),
    Column('LAST_UPDATE_DATE', DateTime),
    Column('ITERATION_COUNT', Float(asdecimal=True))
)


class SsewDatum(Base):
    __tablename__ = 'ssew_data'

    SSEW_DATA_ID = Column(BIGINT(20), primary_key=True)
    ACTIVITY_CALL_DATE = Column(String(100))
    RESULT_CODE = Column(String(100))
    FORM_ID = Column(String(200))
    WAR_STATUS = Column(String(20))
    NAME_IC = Column(String(200))
    SURNAME = Column(String(200))
    SALUTATION = Column(String(20))
    NRIC = Column(String(200))
    RESIDENTIAL_ADDRESS = Column(String(200))
    POSTAL_CODE = Column(String(200))
    CONTACT_NO_HOME = Column(String(200))
    CONTACT_NO_MOBILE = Column(String(200))
    CONTACT_NO_OFFICE = Column(String(200))
    EMAIL = Column(String(200))
    PRODUCT_TYPE = Column(String(200))
    BRAND = Column(String(200))
    BRAND_REPORT = Column(String(200))
    MODEL = Column(String(200))
    MODEL_NUMBER = Column(String(200))
    SERIAL_NUMBER = Column(String(200))
    PRICE_PRODUCT = Column(String(200))
    WARRANTY_SERIAL_NUMBER = Column(String(200))
    CHALLENGER_TAX_INVOICE_NUMBER = Column(String(200))
    PLACE_PURCHASE = Column(String(200))
    CLT_MATRIX = Column(String(200))
    LENGTH_MANUFACTURER_WARRANTY = Column(String(20))
    LENGTH_EXTENDED_WARRANTY = Column(String(20))
    PROMO_NON_PROMO = Column(String(20))
    EXTENDED_WARRANTY_PRICE = Column(String(200))
    EXTENDED_WARRANTY_PRICE_NO_GST = Column(String(200))
    EXTENDED_WARRANTY_COST = Column(String(200))
    SSEW_START_DATE = Column(String(100))
    SSEW_REG_MONTH = Column(String(20))
    SSEW_REG_YEAR = Column(String(20))
    SSEW_LENGTH_MONTHS = Column(String(20))
    SSEW_MONTHLY_REG_AMOUNT = Column(String(20))
    SSEW_LENGTH = Column(String(20))
    EXT_WARN_TOTAL_COST_REPAIR = Column(String(20))
    EXT_WARN_CLAIM_BAL = Column(String(20))
    SRP_BALANCE = Column(String(20))
    PRODUCT_PURCHASE_DAY = Column(String(20))
    PRODUCT_PURCHASE_MONTH = Column(String(20))
    PRODUCT_PURCHASE_YEAR = Column(String(20))
    EXT_WARRANTY_START_DAY = Column(String(20))
    EXT_WARRANTY_START_MONTH = Column(String(20))
    EXT_WARRANTY_START_YEAR = Column(String(20))
    EXT_WARRANTY_END_DAY = Column(String(20))
    EXT_WARRANTY_END_MONTH = Column(String(20))
    EXT_WARRANTY_END_YEAR = Column(String(20))
    SSEW_PURCHASE_DAY = Column(String(20))
    SSEW_PURCHASE_MONTH = Column(String(20))
    SSEW_PURCHASE_YEAR = Column(String(20))
    WARRANTY_COMMENTS = Column(String(200))
    CASE_ID = Column(String(200))
    UNIQUE_WARRANTY = Column(String(20))
    UPC_DESCRIPTION = Column(String(200))
    SEW_PURCHASE_DATE = Column(String(200))
    NEW_EMAIL_ID = Column(String(200))


t_ssew_data_user = Table(
    'ssew_data_user', metadata,
    Column('EMAIL_ID', String(255)),
    Column('TITLE', String(55))
)


t_ssew_missing_data_status = Table(
    'ssew_missing_data_status', metadata,
    Column('WARRANTY_NO', Float(asdecimal=True)),
    Column('EQ_STOCK_ID', String(55)),
    Column('W_DUMMY', Float(asdecimal=True)),
    Column('WARRNTY_REF', String(55)),
    Column('PURCHASE_DT', DateTime),
    Column('WARRANTY_PERIOD', Float(asdecimal=True)),
    Column('EXD_WARRANTY_PERIOD', Float(asdecimal=True)),
    Column('RST_CODE_DESCRIPTION', String(50)),
    Column('COMPANY_NAME', String(255)),
    Column('IC_NO_DOC_NO', String(55)),
    Column('FIRST_NAME', String(55)),
    Column('EMAIL_ID', String(255)),
    Column('ADDRESSLINE_1', String(255)),
    Column('ADDRESSLINE_2', String(255)),
    Column('ADDRESSLINE_3', String(255)),
    Column('POSTCODE', String(20)),
    Column('COUNTRY', String(50)),
    Column('PHONE_NO', String(55)),
    Column('MOBILE', String(55)),
    Column('COMPANY_ID', Float(asdecimal=True)),
    Column('CODE_ID', Float(asdecimal=True)),
    Column('VALUE', String(100)),
    Column('USER_ID', Float(asdecimal=True)),
    Column('STATUS', String(20)),
    Column('REMARKS', String(2000)),
    Column('LAST_UPDATE_DATE', DateTime),
    Column('SERIAL_NO', String(55)),
    Column('MODLE_NAME', String(55)),
    Column('BRAND_NAME', String(55)),
    Column('PRODUCT_TYPE', String(55))
)


t_ssew_upc_codes = Table(
    'ssew_upc_codes', metadata,
    Column('UPC_CODE', String(255)),
    Column('COST', String(255))
)


t_students = Table(
    'students', metadata,
    Column('NAME', String(70)),
    Column('ENROLLDATE', DateTime),
    Column('PROGRESS', Float(asdecimal=True))
)


class TblPartTransaction(Base):
    __tablename__ = 'tbl_part_transaction'

    part_transaction_id = Column(BIGINT(20), primary_key=True)
    part_no = Column(String(25))
    user_to_branch = Column(TINYINT(4))
    user_to_user = Column(TINYINT(4))
    branch_to_branch = Column(TINYINT(4))
    branch_to_user = Column(TINYINT(4))
    transfered_from = Column(BIGINT(20))
    transfered_to = Column(BIGINT(20))
    quantity = Column(BIGINT(20))
    transfered_date = Column(DATETIME(fsp=2))
    CREATED_DT = Column(DATETIME(fsp=6))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))


t_temp_rejected_emails = Table(
    'temp_rejected_emails', metadata,
    Column('ORG_EMAIL', String(55)),
    Column('ALT_EMAIL', String(55)),
    Column('FLYERS', String(55)),
    Column('REF_NO', String(20)),
    Column('HP_NO', String(20))
)


class TempWarranty(Base):
    __tablename__ = 'temp_warranty'

    WARRANTY_NO = Column(String(55), primary_key=True)
    SNO = Column(String(55))


class User(Base):
    __tablename__ = 'user'

    user_id = Column(INTEGER(11), primary_key=True)
    first_name = Column(String(512))
    last_name = Column(String(512))
    email_id = Column(String(255))
    created_dt = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"))
    password = Column(String(255))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(INTEGER(11), primary_key=True)
    first_name = Column(String(512))
    last_name = Column(String(512))
    email_id = Column(String(255))
    created_dt = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"))
    password = Column(String(255))


class YarraaI18nModule(Base):
    __tablename__ = 'yarraa_i18n_modules'

    ID = Column(Float(asdecimal=True), primary_key=True)
    TAB_NAME = Column(String(55))
    PORTLET_TITLE = Column(String(55))
    MODEL_NAME = Column(String(255), nullable=False, server_default=text("'1'"))
    TAB_DISPLAY_NAME = Column(String(55))
    IS_DISPLAYABLE = Column(TINYINT(4), nullable=False, server_default=text("1"))


class RstBatch(Base):
    __tablename__ = 'rst_batch'

    ID = Column(DECIMAL(19, 0), primary_key=True)
    ACTIVE_STATUS = Column(BIGINT(20))
    COMPANY_ID = Column(DECIMAL(19, 0))
    NAME = Column(String(255), nullable=False)
    UNITS = Column(BIGINT(20))
    PLAN_ID = Column(ForeignKey('rst_plan.ID'), index=True)
    CREATED_DATE = Column(DATETIME(fsp=6))

    rst_plan = relationship('RstPlan')


class RstBrandsNew(Base):
    __tablename__ = 'rst_brands_new'

    BRAND_ID = Column(BIGINT(20), primary_key=True)
    BRAND_NAME = Column(String(55), nullable=False)
    BRAND_IMAGE = Column(LONGBLOB)
    SYSTEM_CREATED = Column(TINYINT(4), server_default=text("0"))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    IMAGE_NAME = Column(String(255))
    BRAND_NAME_UP = Column(String(55), nullable=False)
    UPDATED_BY = Column(Float(asdecimal=True))
    UPDATED_DT = Column(DateTime)
    SERIES_ID = Column(ForeignKey('rst_series1.SERIES_ID'), nullable=False, index=True)

    rst_series1 = relationship('RstSeries1')


class RstCallLog(Base):
    __tablename__ = 'rst_call_log'

    LOG_ID = Column(Float(asdecimal=True), primary_key=True)
    CASE_ID = Column(ForeignKey('rst_call_log_cases.CASE_ID', ondelete='CASCADE'), nullable=False, index=True)
    LOG_DESC = Column(String(4000))
    LOGGED_BY = Column(Float(asdecimal=True))
    LOGGED_ON = Column(DATETIME(fsp=6))
    SR_ID = Column(Float(asdecimal=True))

    rst_call_log_case = relationship('RstCallLogCase')


class RstCode(Base):
    __tablename__ = 'rst_code'

    CODE_ID = Column(BIGINT(20), primary_key=True)
    SYSTEM_CREATED = Column(TINYINT(4), server_default=text("1"))
    TYPE = Column(ForeignKey('rst_code_type.CODE_TYPE'), index=True)
    VALUE = Column(String(255))
    DESCRIPTION = Column(String(4000))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    ORDER_BY = Column(SMALLINT(6))
    CREATED_DT = Column(DATETIME(fsp=2))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))
    CODE_TYPE_ID = Column(BIGINT(20))
    I18N_ID = Column(String(255))
    I18N_PREFIX = Column(String(255))
    ISSUE_ID = Column(String(20))

    rst_code_type = relationship('RstCodeType')


class RstCodeBk(Base):
    __tablename__ = 'rst_code_bk'

    CODE_ID = Column(BIGINT(20), primary_key=True)
    SYSTEM_CREATED = Column(TINYINT(4), server_default=text("1"))
    TYPE = Column(ForeignKey('rst_code_type.CODE_TYPE'), index=True)
    VALUE = Column(String(255))
    DESCRIPTION = Column(String(255))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    ORDER_BY = Column(SMALLINT(6))
    CREATED_DT = Column(DATETIME(fsp=2))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    COMPANY_ID = Column(BIGINT(20))
    CODE_TYPE_ID = Column(BIGINT(20))
    I18N_ID = Column(String(255))
    I18N_PREFIX = Column(String(255))

    rst_code_type = relationship('RstCodeType')


t_rst_ew_plan_appl_countries = Table(
    'rst_ew_plan_appl_countries', metadata,
    Column('PLAN_ID', ForeignKey('rst_ew_plan_list.PLAN_ID', ondelete='CASCADE'), nullable=False, index=True),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('COUNTRY_CODE', String(2), nullable=False, server_default=text("'SG'"))
)


t_rst_ew_plan_appl_features = Table(
    'rst_ew_plan_appl_features', metadata,
    Column('PLAN_ID', ForeignKey('rst_ew_plan_list.PLAN_ID', ondelete='CASCADE'), nullable=False, index=True),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('FEATURE_ID', Float(asdecimal=True), nullable=False)
)


t_rst_ew_plan_appl_products = Table(
    'rst_ew_plan_appl_products', metadata,
    Column('PLAN_ID', ForeignKey('rst_ew_plan_list.PLAN_ID', ondelete='CASCADE'), nullable=False, index=True),
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('PRODUCT_ID', BIGINT(20), nullable=False)
)


t_rst_inventory_transfer_parts = Table(
    'rst_inventory_transfer_parts', metadata,
    Column('COMPANY_ID', BIGINT(20), nullable=False),
    Column('INVENTORY_ID', ForeignKey('rst_inventory_transfer.INVENTORY_ID', ondelete='CASCADE'), nullable=False, index=True),
    Column('LOCATION', String(55)),
    Column('PRODUCT_ID', BIGINT(20), nullable=False),
    Column('EQ_STOCK_ID', BIGINT(20)),
    Column('QTY', BIGINT(20), nullable=False),
    Column('CREATED_BY', BIGINT(20), nullable=False),
    Column('CREATED_DT', DATETIME(fsp=2), nullable=False),
    Column('UPDATED_BY', BIGINT(20)),
    Column('UPDATED_DT', DATETIME(fsp=2)),
    Column('SR_NUMBER', String(55)),
    Column('SR_STATUS', String(55)),
    Column('PART_ID', BIGINT(20)),
    Column('MERGED_TO', Float(asdecimal=True)),
    Column('MERGED_FROM', Float(asdecimal=True))
)


class RstModelReference(Base):
    __tablename__ = 'rst_model_references'

    REFERENCE_ID = Column(Float(asdecimal=True), primary_key=True)
    MODEL_ID = Column(ForeignKey('rst_models_org.MODEL_ID'), index=True)
    RESOURCE_URL = Column(String(255))
    RESOURCE_TYPE = Column(String(20))
    CREATED_BY = Column(Float(asdecimal=True))
    UPDATED_BY = Column(Float(asdecimal=True))
    CREATED_DT = Column(DateTime)
    UPDATED_DT = Column(DateTime)
    RESOURCE_IMG_URL = Column(String(255))
    ACTIVE_STATUS = Column(TINYINT(4))

    rst_models_org = relationship('RstModelsOrg')


class RstReportConfigColumn(Base):
    __tablename__ = 'rst_report_config_columns'
    __table_args__ = (
        Index('RST_REPORT_CONFIG_COLUMNS_UK1', 'COLUMN_IDENTIFIER', 'CONFIG_ID', unique=True),
    )

    COLUMN_ID = Column(Float(asdecimal=True), primary_key=True)
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    CONFIG_ID = Column(ForeignKey('rst_report_config.CONFIG_ID'), nullable=False, index=True)
    VIEW_NAME = Column(String(55), nullable=False)
    COLUMN_NAME = Column(String(55), nullable=False)
    DISPLAY_NAME = Column(String(55), nullable=False)
    DATA_TYPE = Column(String(20), nullable=False)
    FORMAT = Column(String(10))
    COLUMN_IDENTIFIER = Column(String(55), nullable=False)
    ORDER_BY_COLUMN = Column(String(55))
    QRY_STRING = Column(String(4000))
    IS_DISPLAYABLE_COLUMN = Column(TINYINT(4), nullable=False, server_default=text("1"))

    rst_report_config = relationship('RstReportConfig')


class RstReport(Base):
    __tablename__ = 'rst_reports'

    REPORT_ID = Column(Float(asdecimal=True), primary_key=True)
    COMPANY_ID = Column(Float(asdecimal=True))
    REPORT_TITLE = Column(String(255), nullable=False)
    CREATED_BY = Column(Float(asdecimal=True))
    CREATED_ON = Column(DATETIME(fsp=6))
    REPORT_TYPE = Column(String(20), nullable=False)
    ACTIVE_STATUS = Column(TINYINT(4), nullable=False, server_default=text("1"))
    CONFIG_ID = Column(ForeignKey('rst_report_config.CONFIG_ID'), nullable=False, index=True)
    SHOW_DETAILS = Column(Float(asdecimal=True), nullable=False, server_default=text("-1"))

    rst_report_config = relationship('RstReportConfig')


class RstStockInfo(Base):
    __tablename__ = 'rst_stock_info'
    __table_args__ = (
        Index('RST_STOCK_INFO_UK1', 'PRODUCT_ID', 'COMPANY_ID', unique=True),
    )



    STOCK_ID = Column(BIGINT(20), primary_key=True)
    PRODUCT_ID = Column(ForeignKey('rst_product_master.PRODUCT_ID'), nullable=False)
    COMPANY_ID = Column(ForeignKey('rst_company_new.COMPANY_ID'), nullable=False, index=True)
    LOCATION = Column(String(55))
    IN_QTY = Column(BIGINT(20))
    OUT_QTY = Column(BIGINT(20), nullable=False, server_default=text("0"))
    BALANCE_QTY = Column(BIGINT(20))
    CREATED_BY = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    QTY_BELOW_AVE_ALERT = Column(BIGINT(20))
    ALERT_ENABLED = Column(TINYINT(4))

    rst_company_new = relationship('RstCompanyNew')
    rst_product_master = relationship('RstProductMaster')


class RstUser(Base):
    __tablename__ = 'rst_users'

    USER_ID = Column(BIGINT(20), primary_key=True)
    TITLE = Column(String(10))
    FIRST_NAME = Column(String(55), nullable=False)
    MIDDLE_NAME = Column(String(55))
    LAST_NAME = Column(String(55))
    DOC_NUMBER = Column(String(55))
    DOB = Column(DateTime)
    EMAIL_ID = Column(String(255), nullable=False)
    USER_NAME = Column(String(55))
    PASSWORD = Column(String(1000))
    PASSWORD_HINT = Column(String(255))
    SECRET_QUESTION = Column(String(255))
    SECRET_QUESTION_ANS = Column(String(255))
    PHONE_NO = Column(String(50))
    DEPARTMENT = Column(String(50), server_default=text("'CONSUMER'"))
    ADDRESS_LINE1 = Column(String(255))
    ADDRESS_LINE2 = Column(String(255))
    CITY = Column(String(55))
    STATE = Column(String(100))
    POSTAL_CODE = Column(String(20))
    COUNTRY_CODE = Column(String(55), nullable=False, server_default=text("'IN'"))
    COMPANY_ID = Column(ForeignKey('rst_company_new.COMPANY_ID'), index=True)
    USER_TYPE = Column(String(55), server_default=text("'Consumers'"))
    LICENSE_ID = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=6))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    PREFERED_LANG = Column(String(10))
    IS_TECHNICAN = Column(TINYINT(4), server_default=text("0"))
    VERSION = Column(BIGINT(20), server_default=text("0"))
    ACTIVE_STATUS = Column(CHAR(1), server_default=text("'A'"))
    ACCOUNT_EXPIRED = Column(CHAR(1), server_default=text("'N'"))
    ACCOUNT_LOCKED = Column(CHAR(1), server_default=text("'N'"))
    CREDENTIALS_EXPIRED = Column(CHAR(1), server_default=text("'N'"))
    TC_AGREED = Column(CHAR(1), server_default=text("'Y'"))
    HAS_REGISTERED = Column(CHAR(1), server_default=text("'Y'"))
    MOBILE = Column(String(55))

    ACCESS_GROUP = Column(String(55))
    LOGIN_COUNT = Column(BIGINT(20), server_default=text("0"))
    LAST_LOGIN_TIME = Column(DATETIME(fsp=6))
    REG_COMPLETED = Column(String(1), nullable=False, server_default=text("'Y'"))
    NEW_PASSWORD = Column(String(1000))
    IC_NO = Column(String(55))
    MOBILE_COUNTRY_CODE = Column(String(5))
    REFERED_BY = Column(Float(asdecimal=True))
    OFFICE_PHONE = Column(String(20))
    ALTERNATE_EMAIL = Column(String(55))
    ADDITIONAL_INFO = Column(String(55))
    IS_FIRST_TIME_LOGIN = Column(TINYINT(4), nullable=False, server_default=text("1"))
    SSEW_DATA_NEW_ID = Column(BIGINT(20))
    ADDRESS_LINE3 = Column(String(255))
    TIMEZONE = Column(String(55), nullable=False, server_default=text("'Asia/India'"))
    TALUK_VALUE = Column(String(100))
    MOBILEINFO_ID = Column(ForeignKey('rst_users_mobileinfo.MOBILEINFO_ID'), index=True)
    GMAIL_FB = Column(Float(asdecimal=True))
    GENDER = Column(String(20))
    GSTIN = Column(String(50))
    PANNO = Column(String(20))
    SIGNATURE = Column(LONGBLOB)




    rst_company_new = relationship('RstCompanyNew')
    rst_users_mobileinfo = relationship('RstUsersMobileinfo')


class YarraaI18n(Base):
    __tablename__ = 'yarraa_i18n'

    ID = Column(Float(asdecimal=True), primary_key=True)
    PORTLET_ID = Column(ForeignKey('yarraa_i18n_modules.ID'), index=True)
    TEXT_EN_US = Column(String(255), nullable=False)
    TEXT_ZH_CN = Column(String(255), nullable=False)
    TEXT_DE_DE = Column(String(255), nullable=False)

    yarraa_i18n_module = relationship('YarraaI18nModule')


class RstBatchUnit(Base):
    __tablename__ = 'rst_batch_units'

    ID = Column(DECIMAL(19, 0), primary_key=True)
    CREATED_DATE = Column(DateTime)
    PIN = Column(String(255))
    SNO = Column(String(255))
    BATCH_ID = Column(ForeignKey('rst_batch.ID'), index=True)
    IS_SOLD = Column(TINYINT(4), nullable=False, server_default=text("0"))

    rst_batch = relationship('RstBatch')


class RstJob(Base):
    __tablename__ = 'rst_job'

    JOB_ID = Column(BIGINT(20), primary_key=True)
    BATCH_ID = Column(String(55))
    JOB_NO = Column(String(255))
    JOB_TYPE = Column(String(55))
    ATTENTED_BY = Column(String(55))
    EQ_STOCK_ID = Column(ForeignKey('rst_equipmt_stock.EQ_STOCK_ID'), nullable=False, index=True)
    SW_VERSION = Column(String(255))
    PRODUCTION_DT = Column(DateTime)
    LOAN_EQUIPMENT_ID = Column(BIGINT(20))
    LOAN_EQUIPMENT_REF = Column(String(255))
    LOAN_COMES_WITH = Column(String(255))
    SWAP_SERIAL = Column(String(55))
    IN_WARRANTY_OLD = Column(BIGINT(20))
    IRIS_SYMPTOM = Column(String(255))
    IRIS_CONDITION = Column(String(55))
    SECOND_RTN = Column(String(55))
    NETWORK_OPTR = Column(String(55))
    CASING_CLR = Column(String(55))
    TECHNICIAN_ID = Column(ForeignKey('rst_users.USER_ID'), index=True)
    JOB_STATUS = Column(BIGINT(20))
    IRIS_DEFECT = Column(BIGINT(20))
    IRIS_REPAIR = Column(BIGINT(20))
    REPAIR_LEVEL = Column(BIGINT(20))
    MAXIMUM = Column(String(55))
    HANDLED_BY = Column(String(255))
    RECEIVED_BY = Column(String(255))
    REGISTER_IN = Column(SMALLINT(6))
    PARAM_SYS_TEST = Column(SMALLINT(6))
    CUST_LBL_UPGRD = Column(SMALLINT(6))
    PRE_TEST_HW_UPGRD = Column(SMALLINT(6))
    SW_UPGRADE = Column(SMALLINT(6))
    REGISTER_OUT = Column(SMALLINT(6))
    FINAL_OUT = Column(SMALLINT(6))
    BOM_CHECK = Column(SMALLINT(6))
    COMES_WITH = Column(String(255))
    LABOUR_COST = Column(String(55))
    FAILURE_DESC = Column(String(255))
    REPAIR_NOTES = Column(String(2000))
    SHIP_STATUS = Column(BIGINT(20), server_default=text("0"))
    SR_NUMBER = Column(String(55))
    SW_VERSION_UPDATED = Column(String(55))
    PAID = Column(TINYINT(4))
    BILLING_STATUS = Column(BIGINT(20))
    BILLING_ID = Column(BIGINT(20))
    SMS_SEND_STATUS = Column(String(45))
    NO_OF_TIMES_SMS_SEND = Column(BIGINT(20))
    SMS_SEND_DT = Column(DATETIME(fsp=2))
    SMS_SEND_BY = Column(String(100))
    COMPANY_ID = Column(ForeignKey('rst_company_new.COMPANY_ID'), nullable=False, index=True)
    QUOTATION_ID = Column(ForeignKey('rst_quotation.QUOTATION_ID'), index=True)
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))
    COLLECTED_BY = Column(String(55))
    COLLECTED_DT = Column(DATETIME(fsp=2))
    JOB_STATUS_UPD_DT = Column(DATETIME(fsp=2))
    CREATED_DT = Column(DATETIME(fsp=2))
    CREATED_BY = Column(BIGINT(20))
    CLOSE_STATUS = Column(TINYINT(4), server_default=text("0"))
    CLOSED_DATE = Column(DATETIME(fsp=6))
    SWAP_EQ_STOCK_ID = Column(BIGINT(20))
    IN_WARRANTY = Column(String(5))
    ACTIVE_STATUS = Column(Float(asdecimal=True), nullable=False, server_default=text("1"))
    IRIS_SYMPTOM_BK = Column(String(255))
    IRIS_CONDITION_BK = Column(String(255))
    JOB_STATUS_BK = Column(BIGINT(20))
    IRIS_REPAIR_BK = Column(BIGINT(20))
    IRIS_DEFECT_BK = Column(BIGINT(20))
    REPAIR_LEVEL_BK = Column(BIGINT(20))
    IN_WARRANTY_BK = Column(String(20))
    PANEL_STATUS = Column(String(50))
    CONSUMER_LATITUDE = Column(DECIMAL(20, 6))
    CONSUMER_LONGITUDE = Column(DECIMAL(20, 6))
    SCRATCHES_IN_PANEL = Column(Float(asdecimal=True))
    PANEL_PEELOFF = Column(Float(asdecimal=True))
    COLOUR_FADED = Column(Float(asdecimal=True))
    TECHNICIAN_LATITUDE = Column(DECIMAL(20, 6))
    TECHNICIAN_LONGITUDE = Column(DECIMAL(20, 6))
    FCM_KEY = Column(String(200))
    SERVICE_TYPE = Column(String(30))
    FILE_UPLOAD = Column(LONGBLOB)
    FILE_UPLOAD_NAME = Column(String(50))

    rst_company_new = relationship('RstCompanyNew')
    rst_equipmt_stock = relationship('RstEquipmtStock')
    rst_quotation = relationship('RstQuotation')
    rst_user = relationship('RstUser')


class RstPrdDefect(Base):
    __tablename__ = 'rst_prd_defects'

    DEFECT_ID = Column(BIGINT(20), primary_key=True)
    PROD_ID = Column(ForeignKey('rst_product_master.PRODUCT_ID'), nullable=False, index=True)
    DEFECT_DESCRIPTION = Column(BIGINT(20), nullable=False)
    PRICE = Column(DECIMAL(20, 10))
    CREATED_BY = Column(ForeignKey('rst_users.USER_ID'), index=True)
    CREATED_ON = Column(DATETIME(fsp=6))

    rst_user = relationship('RstUser')
    rst_product_master = relationship('RstProductMaster')


class RstReportColumn(Base):
    __tablename__ = 'rst_report_columns'

    COLUMN_ID = Column(Float(asdecimal=True), primary_key=True)
    REPORT_ID = Column(ForeignKey('rst_reports.REPORT_ID'), nullable=False, index=True)
    REPORT_COLUMN = Column(String(55), nullable=False)
    VIEW_ORDER = Column(Float(asdecimal=True))

    rst_report = relationship('RstReport')


class RstReportCriterion(Base):
    __tablename__ = 'rst_report_criteria'

    CRITERIA_ID = Column(String(20), primary_key=True)
    CRITERIA_COLUMN = Column(String(55), nullable=False)
    CRITERIA_TYPE = Column(String(20), nullable=False)
    DEFAULT_CRITERIA_VALUE = Column(String(55))
    DEFAULT_RANGE_FROM = Column(String(20))
    DEFAULT_RANGE_TO = Column(String(20))
    CRITERIA_ORDER = Column(Float(asdecimal=True))
    REPORT_ID = Column(ForeignKey('rst_reports.REPORT_ID'), nullable=False, index=True)
    JOIN_VIEW = Column(String(4000))

    rst_report = relationship('RstReport')


class RstReportSortColumn(Base):
    __tablename__ = 'rst_report_sort_columns'

    SORT_COLUMN_ID = Column(Float(asdecimal=True), primary_key=True)
    REPORT_ID = Column(ForeignKey('rst_reports.REPORT_ID'), nullable=False, index=True)
    SORT_COLUMN = Column(String(55), nullable=False)
    SORT_ORDER = Column(Float(asdecimal=True))
    IS_GROUP_BY_COLUMN = Column(TINYINT(4), nullable=False, server_default=text("0"))
    MATRIX_ROW_OR_COLUMN = Column(String(20))
    ASC_OR_DESC = Column(String(5), nullable=False, server_default=text("'ASC'"))

    rst_report = relationship('RstReport')


class RstReportSummary(Base):
    __tablename__ = 'rst_report_summary'

    SUMMARY_ID = Column(Float(asdecimal=True), primary_key=True)
    REPORT_ID = Column(ForeignKey('rst_reports.REPORT_ID'), nullable=False, index=True)
    SUMMARY_COLUMN = Column(String(55), nullable=False)
    SUMMARY_TYPE = Column(String(20), nullable=False)
    DISPLAY_NAME = Column(String(255))

    rst_report = relationship('RstReport')


class RstStockTransaction(Base):
    __tablename__ = 'rst_stock_transactions'

    STOCK_TRANSACTION_ID = Column(BIGINT(20), primary_key=True)
    STOCK_TRANSACTION_DATE = Column(DATETIME(fsp=2))
    IN_QTY = Column(BIGINT(20))
    OUT_QTY = Column(BIGINT(20))
    TRANSACTION_TYPE = Column(String(55))
    TRANSACTION_REF = Column(String(55))
    COMPANY_REF_ID = Column(BIGINT(20))
    COMPANY_ID = Column(ForeignKey('rst_company_new.COMPANY_ID'), index=True)
    STOCK_ID = Column(ForeignKey('rst_stock_info.STOCK_ID'), index=True)
    PRODUCT_ID = Column(ForeignKey('rst_product_master.PRODUCT_ID'), index=True)

    rst_company_new = relationship('RstCompanyNew')
    rst_product_master = relationship('RstProductMaster')
    rst_stock_info = relationship('RstStockInfo')


class RstUserRequestPart(Base):
    __tablename__ = 'rst_user_request_parts'

    user_request_part_id = Column(BIGINT(20), primary_key=True)
    part_id = Column(ForeignKey('rst_parts.PART_ID'), index=True)
    part_no = Column(String(25))
    user_id = Column(ForeignKey('rst_users.USER_ID'), index=True)
    quantity = Column(BIGINT(20))
    branch_id = Column(ForeignKey('rst_branch.branch_id'), index=True)
    request_status = Column(String(30))
    CREATED_DT = Column(DATETIME(fsp=6))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))

    branch = relationship('RstBranch')
    part = relationship('RstPart')
    user = relationship('RstUser')


class RstWarranty(Base):
    __tablename__ = 'rst_warranty'

    WARRNTY_ID = Column(BIGINT(20), primary_key=True)
    WARRNTY_REF = Column(String(55))
    EQ_STOCK_ID = Column(ForeignKey('rst_equipmt_stock.EQ_STOCK_ID'), nullable=False, index=True)
    PURCHASE_DT = Column(DateTime)
    PROD_DATE_CODE = Column(String(255))
    USER_ID = Column(ForeignKey('rst_users.USER_ID'), index=True)
    IN_WARRANTY = Column(BIGINT(20))
    REMARKS = Column(String(4000))
    VOID_REASON = Column(String(4000))
    REGISTERED_BY = Column(BIGINT(20))
    REGISTERED_BY_TYPE = Column(String(55))
    WARRENTY_EXP_DT = Column(DateTime)
    PURCHASE_FROM = Column(String(200))
    COMPANY_ID = Column(BIGINT(20))
    COUNTRY_CODE = Column(String(55))
    WARRANTY_NO = Column(String(55))
    REGISTERED_DT = Column(DATETIME(fsp=6))
    ACTIVE_STATUS = Column(TINYINT(4), server_default=text("1"))
    FILE_UPLOAD_1 = Column(LONGBLOB)
    FILE_UPLOAD_2 = Column(LONGBLOB)
    FILE_UPLOAD_3 = Column(LONGBLOB)
    FILE_UPLOAD_1_NAME = Column(String(55))
    FILE_UPLOAD_2_NAME = Column(String(55))
    FILE_UPLOAD_3_NAME = Column(String(55))
    WARRANTY_MONTHS = Column(BIGINT(20))
    UPDATED_BY = Column(Float(asdecimal=True))
    EMAIL_SENT = Column(TINYINT(4), server_default=text("0"))
    CURRENCY_CODE = Column(String(20))
    PRODUCT_COST = Column(String(20))
    WARRANTY_TYPE = Column(String(8), nullable=False, server_default=text("'MW'"))
    EW_TYPE = Column(Float(asdecimal=True))
    EW_CATEGORY = Column(Float(asdecimal=True))
    WARRANTY_STATUS = Column(String(55))
    INVOICE_NUMBER = Column(String(55))
    ADDITIONAL_INFO = Column(String(55))
    CREATED_BY = Column(BIGINT(20))
    OLD_USER_ID = Column(BIGINT(20))
    IS_UPDATED = Column(TINYINT(4))
    EW_CATEGORY_DESC = Column(String(200))
    ORIG_PRODUCT_COST = Column(Float(asdecimal=True))
    WARRANTY_START_DATE = Column(DateTime)
    OLD_PURCHASE_DT = Column(DateTime)
    OLD_REGD_DT = Column(DateTime)
    UPDATED_DT = Column(DateTime)
    OLD_WARRENTY_EXP_DATE = Column(DateTime)
    OH_HOLD_MIGRATION = Column(String(20))
    MIGRATED_WARRANTY_NO = Column(Float(asdecimal=True))
    PARENT_WARRANTY_ID = Column(Float(asdecimal=True))
    EW_TYPE_BK = Column(Float(asdecimal=True))
    EW_CATEGORY_BK = Column(Float(asdecimal=True))
    REACTIVATED_ON = Column(DateTime)
    DATE_PATCHED = Column(Float(asdecimal=True))
    ORIG_COST_PATCHED = Column(Float(asdecimal=True))
    ORIG_COST_BK = Column(Float(asdecimal=True))
    VOIDED_BY = Column(Float(asdecimal=True))
    VOIDED_ON = Column(DateTime)
    ORDER_REF_NUMBER = Column(String(255))
    REDEMPTION_ID = Column(Float(asdecimal=True))
    CONSUMER_SUBSCRIBED = Column(TINYINT(4), nullable=False, server_default=text("0"))
    WORKING_CONDITION = Column(TINYINT(4), server_default=text("1"))
    WARRANTY_STATE = Column(String(55), server_default=text("'ACTIVE'"))
    SALES_TYPE = Column(String(1))
    SALES_BY = Column(BIGINT(20))
    PLAN_ID = Column(BIGINT(20))
    EW_START_DT = Column(DateTime)
    EW_END_DT = Column(DateTime)

    rst_equipmt_stock = relationship('RstEquipmtStock')
    rst_user = relationship('RstUser')


t_rst_prd_fixes = Table(
    'rst_prd_fixes', metadata,
    Column('EQ_STOCK_ID', BIGINT(20), nullable=False),
    Column('DEFECT_ID', ForeignKey('rst_prd_defects.DEFECT_ID'), nullable=False, index=True),
    Column('ACCEPTED_BY', ForeignKey('rst_users.USER_ID'), nullable=False, index=True),
    Column('REMARKS', String(4000)),
    Column('CREATED_BY', ForeignKey('rst_users.USER_ID'), index=True),
    Column('CREATED_ON', DATETIME(fsp=6))
)


class RstUserPartsStock(Base):
    __tablename__ = 'rst_user_parts_stock'

    user_parts_stock_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(ForeignKey('rst_users.USER_ID'), index=True)
    branch_id = Column(ForeignKey('rst_branch.branch_id'), index=True)
    user_request_part_id = Column(ForeignKey('rst_user_request_parts.user_request_part_id'), index=True)
    current_qty = Column(BIGINT(20))
    CREATED_DT = Column(DATETIME(fsp=6))
    CREATED_BY = Column(BIGINT(20))
    UPDATED_DT = Column(DATETIME(fsp=2))
    UPDATED_BY = Column(BIGINT(20))

    branch = relationship('RstBranch')
    user = relationship('RstUser')
    user_request_part = relationship('RstUserRequestPart')
