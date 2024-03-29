# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Salesrep(models.Model):
    idsalesrep = models.AutoField(db_column='idSalesRep', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    method = models.SmallIntegerField(db_column='Method', blank=True, null=True)  # Field name made lowercase.
    target1 = models.FloatField(db_column='Target1', blank=True, null=True)  # Field name made lowercase.
    commission1 = models.FloatField(db_column='Commission1', blank=True, null=True)  # Field name made lowercase.
    target2 = models.FloatField(db_column='Target2', blank=True, null=True)  # Field name made lowercase.
    commission2 = models.FloatField(db_column='Commission2', blank=True, null=True)  # Field name made lowercase.
    target3 = models.FloatField(db_column='Target3', blank=True, null=True)  # Field name made lowercase.
    commission3 = models.FloatField(db_column='Commission3', blank=True, null=True)  # Field name made lowercase.
    target4 = models.FloatField(db_column='Target4', blank=True, null=True)  # Field name made lowercase.
    commission4 = models.FloatField(db_column='Commission4', blank=True, null=True)  # Field name made lowercase.
    target5 = models.FloatField(db_column='Target5', blank=True, null=True)  # Field name made lowercase.
    commission5 = models.FloatField(db_column='Commission5', blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    entity = models.CharField(db_column='Entity', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rep_on_hold = models.CharField(db_column='Rep_On_Hold', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bank_account = models.CharField(db_column='Bank_Account', max_length=40, blank=True, null=True)  # Field name made lowercase.
    comment1 = models.CharField(db_column='Comment1', max_length=80, blank=True, null=True)  # Field name made lowercase.
    comment2 = models.CharField(db_column='Comment2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    salesrep_ibranchid = models.IntegerField(db_column='SalesRep_iBranchID', blank=True, null=True)  # Field name made lowercase.
    salesrep_dcreateddate = models.DateTimeField(db_column='SalesRep_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    salesrep_dmodifieddate = models.DateTimeField(db_column='SalesRep_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    salesrep_icreatedbranchid = models.IntegerField(db_column='SalesRep_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    salesrep_imodifiedbranchid = models.IntegerField(db_column='SalesRep_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    salesrep_icreatedagentid = models.IntegerField(db_column='SalesRep_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    salesrep_imodifiedagentid = models.IntegerField(db_column='SalesRep_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    salesrep_ichangesetid = models.IntegerField(db_column='SalesRep_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    salesrep_checksum = models.TextField(db_column='SalesRep_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SalesRep'

class Stkitem(models.Model):
    stocklink = models.AutoField(db_column='StockLink', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=400, blank=True, null=True)  # Field name made lowercase.
    description_1 = models.CharField(db_column='Description_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description_2 = models.CharField(db_column='Description_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description_3 = models.CharField(db_column='Description_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serviceitem = models.BooleanField(db_column='ServiceItem')  # Field name made lowercase.
    itemactive = models.BooleanField(db_column='ItemActive')  # Field name made lowercase.
    whseitem = models.BooleanField(db_column='WhseItem')  # Field name made lowercase.
    serialitem = models.BooleanField(db_column='SerialItem')  # Field name made lowercase.
    duplicatesn = models.BooleanField(db_column='DuplicateSN')  # Field name made lowercase.
    strictsn = models.BooleanField(db_column='StrictSN')  # Field name made lowercase.
    bomcode = models.CharField(db_column='BomCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smtrxcol = models.IntegerField(db_column='SMtrxCol', blank=True, null=True)  # Field name made lowercase.
    pmtrxcol = models.IntegerField(db_column='PMtrxCol', blank=True, null=True)  # Field name made lowercase.
    cmodel = models.CharField(db_column='cModel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crevision = models.CharField(db_column='cRevision', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccomponent = models.CharField(db_column='cComponent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddatereleased = models.DateTimeField(db_column='dDateReleased', blank=True, null=True)  # Field name made lowercase.
    dstkitemtimestamp = models.DateTimeField(db_column='dStkitemTimeStamp', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue1id = models.IntegerField(db_column='iInvSegValue1ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue2id = models.IntegerField(db_column='iInvSegValue2ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue3id = models.IntegerField(db_column='iInvSegValue3ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue4id = models.IntegerField(db_column='iInvSegValue4ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue5id = models.IntegerField(db_column='iInvSegValue5ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue6id = models.IntegerField(db_column='iInvSegValue6ID', blank=True, null=True)  # Field name made lowercase.
    iinvsegvalue7id = models.IntegerField(db_column='iInvSegValue7ID', blank=True, null=True)  # Field name made lowercase.
    cextdescription = models.CharField(db_column='cExtDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    csimplecode = models.CharField(db_column='cSimpleCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bcommissionitem = models.BooleanField(db_column='bCommissionItem')  # Field name made lowercase.
    blotitem = models.BooleanField(db_column='bLotItem')  # Field name made lowercase.
    ilotstatus = models.IntegerField(db_column='iLotStatus', blank=True, null=True)  # Field name made lowercase.
    blotmustexpire = models.BooleanField(db_column='bLotMustExpire')  # Field name made lowercase.
    iitemcostingmethod = models.IntegerField(db_column='iItemCostingMethod')  # Field name made lowercase.
    ieucommodityid = models.IntegerField(db_column='iEUCommodityID')  # Field name made lowercase.
    ieusupplementaryunitid = models.IntegerField(db_column='iEUSupplementaryUnitID')  # Field name made lowercase.
    fnetmass = models.FloatField(db_column='fNetMass')  # Field name made lowercase.
    iuomstockingunitid = models.IntegerField(db_column='iUOMStockingUnitID', blank=True, null=True)  # Field name made lowercase.
    iuomdefpurchaseunitid = models.IntegerField(db_column='iUOMDefPurchaseUnitID', blank=True, null=True)  # Field name made lowercase.
    iuomdefsellunitid = models.IntegerField(db_column='iUOMDefSellUnitID', blank=True, null=True)  # Field name made lowercase.
    fstockgppercent = models.FloatField(db_column='fStockGPPercent', blank=True, null=True)  # Field name made lowercase.
    ceachdescription = models.CharField(db_column='cEachDescription', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cmeasurement = models.CharField(db_column='cMeasurement', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fbuylength = models.FloatField(db_column='fBuyLength', blank=True, null=True)  # Field name made lowercase.
    fbuywidth = models.FloatField(db_column='fBuyWidth', blank=True, null=True)  # Field name made lowercase.
    fbuyheight = models.FloatField(db_column='fBuyHeight', blank=True, null=True)  # Field name made lowercase.
    fbuyarea = models.FloatField(db_column='fBuyArea', blank=True, null=True)  # Field name made lowercase.
    fbuyvolume = models.FloatField(db_column='fBuyVolume', blank=True, null=True)  # Field name made lowercase.
    cbuyweight = models.FloatField(db_column='cBuyWeight', blank=True, null=True)  # Field name made lowercase.
    cbuyunit = models.CharField(db_column='cBuyUnit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fselllength = models.FloatField(db_column='fSellLength', blank=True, null=True)  # Field name made lowercase.
    fsellwidth = models.FloatField(db_column='fSellWidth', blank=True, null=True)  # Field name made lowercase.
    fsellheight = models.FloatField(db_column='fSellHeight', blank=True, null=True)  # Field name made lowercase.
    fsellarea = models.FloatField(db_column='fSellArea', blank=True, null=True)  # Field name made lowercase.
    fsellvolume = models.FloatField(db_column='fSellVolume', blank=True, null=True)  # Field name made lowercase.
    csellweight = models.FloatField(db_column='cSellWeight', blank=True, null=True)  # Field name made lowercase.
    csellunit = models.CharField(db_column='cSellUnit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    boverridesell = models.BooleanField(db_column='bOverrideSell', blank=True, null=True)  # Field name made lowercase.
    buomitem = models.BooleanField(db_column='bUOMItem')  # Field name made lowercase.
    bdimensionitem = models.BooleanField(db_column='bDimensionItem')  # Field name made lowercase.
    bvasitem = models.BooleanField(db_column='bVASItem')  # Field name made lowercase.
    bairtimeitem = models.BooleanField(db_column='bAirtimeItem')  # Field name made lowercase.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stkitem_ibranchid = models.IntegerField(db_column='StkItem_iBranchID', blank=True, null=True)  # Field name made lowercase.
    stkitem_dcreateddate = models.DateTimeField(db_column='StkItem_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    stkitem_dmodifieddate = models.DateTimeField(db_column='StkItem_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    stkitem_icreatedbranchid = models.IntegerField(db_column='StkItem_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    stkitem_imodifiedbranchid = models.IntegerField(db_column='StkItem_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    stkitem_icreatedagentid = models.IntegerField(db_column='StkItem_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    stkitem_imodifiedagentid = models.IntegerField(db_column='StkItem_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    stkitem_ichangesetid = models.IntegerField(db_column='StkItem_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    stkitem_checksum = models.TextField(db_column='StkItem_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bsynctosot = models.BooleanField(db_column='bSyncToSOT')  # Field name made lowercase.
    imajorindustrycodeid = models.IntegerField(db_column='iMajorIndustryCodeID', blank=True, null=True)  # Field name made lowercase.
    bimportedservices = models.BooleanField(db_column='bImportedServices')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StkItem'

class Tills(models.Model):
    idtills = models.AutoField(db_column='IdTills', primary_key=True)  # Field name made lowercase.
    tillno = models.CharField(db_column='TillNo', max_length=4)  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    ideviceiddisplay = models.IntegerField(db_column='iDeviceIDDisplay', blank=True, null=True)  # Field name made lowercase.
    ideviceiddrawer = models.IntegerField(db_column='iDeviceIDDrawer', blank=True, null=True)  # Field name made lowercase.
    ideviceidprinter = models.IntegerField(db_column='iDeviceIDPrinter', blank=True, null=True)  # Field name made lowercase.
    ideviceidfiscalprinter = models.IntegerField(db_column='iDeviceIDFiscalPrinter', blank=True, null=True)  # Field name made lowercase.
    ideviceidpinpad = models.IntegerField(db_column='iDeviceIDPinPad', blank=True, null=True)  # Field name made lowercase.
    cterminalid = models.CharField(db_column='cTerminalID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tills_ibranchid = models.IntegerField(db_column='Tills_iBranchID', blank=True, null=True)  # Field name made lowercase.
    tills_dcreateddate = models.DateTimeField(db_column='Tills_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    tills_dmodifieddate = models.DateTimeField(db_column='Tills_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    tills_icreatedbranchid = models.IntegerField(db_column='Tills_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    tills_imodifiedbranchid = models.IntegerField(db_column='Tills_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    tills_icreatedagentid = models.IntegerField(db_column='Tills_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    tills_imodifiedagentid = models.IntegerField(db_column='Tills_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    tills_ichangesetid = models.IntegerField(db_column='Tills_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    tills_checksum = models.TextField(db_column='Tills_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Tills'


class Trcodes(models.Model):
    idtrcodes = models.AutoField(db_column='idTrCodes', primary_key=True)  # Field name made lowercase.
    imodule = models.IntegerField(db_column='iModule')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    linkid = models.IntegerField(db_column='LinkID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    debittrans = models.BooleanField(db_column='DebitTrans')  # Field name made lowercase.
    tax = models.BooleanField(db_column='Tax')  # Field name made lowercase.
    rep = models.BooleanField(db_column='Rep')  # Field name made lowercase.
    account1link = models.IntegerField(db_column='Account1Link', blank=True, null=True)  # Field name made lowercase.
    account2link = models.IntegerField(db_column='Account2Link', blank=True, null=True)  # Field name made lowercase.
    taxaccountlink = models.IntegerField(db_column='TaxAccountLink', blank=True, null=True)  # Field name made lowercase.
    glprompt = models.BooleanField(db_column='GLPrompt')  # Field name made lowercase.
    taxtypeid = models.IntegerField(db_column='TaxTypeID', blank=True, null=True)  # Field name made lowercase.
    splittr = models.BooleanField(db_column='SplitTr')  # Field name made lowercase.
    bsalesfilter = models.BooleanField(db_column='bSalesFilter')  # Field name made lowercase.
    ballowsubacctrans = models.BooleanField(db_column='bAllowSubAccTrans')  # Field name made lowercase.
    bsettlementdisc = models.BooleanField(db_column='bSettlementDisc')  # Field name made lowercase.
    idttaxgroupid = models.IntegerField(db_column='iDtTaxGroupID', blank=True, null=True)  # Field name made lowercase.
    icttaxgroupid = models.IntegerField(db_column='iCtTaxGroupID', blank=True, null=True)  # Field name made lowercase.
    itaxgroupid = models.IntegerField(db_column='iTaxGroupID', blank=True, null=True)  # Field name made lowercase.
    imbserviceid = models.IntegerField(db_column='iMBServiceID')  # Field name made lowercase.
    trcodes_ibranchid = models.IntegerField(db_column='TrCodes_iBranchID', blank=True, null=True)  # Field name made lowercase.
    trcodes_dcreateddate = models.DateTimeField(db_column='TrCodes_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    trcodes_dmodifieddate = models.DateTimeField(db_column='TrCodes_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    trcodes_icreatedbranchid = models.IntegerField(db_column='TrCodes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    trcodes_imodifiedbranchid = models.IntegerField(db_column='TrCodes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    trcodes_icreatedagentid = models.IntegerField(db_column='TrCodes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    trcodes_imodifiedagentid = models.IntegerField(db_column='TrCodes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    trcodes_ichangesetid = models.IntegerField(db_column='TrCodes_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    trcodes_checksum = models.TextField(db_column='TrCodes_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bprepayment = models.BooleanField(db_column='bPrepayment')  # Field name made lowercase.
    bpurchasesfilter = models.BooleanField(db_column='bPurchasesFilter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrCodes'


class WhtBatch(models.Model):
    idbatch = models.AutoField(db_column='idBatch', primary_key=True)  # Field name made lowercase.
    batchnumber = models.CharField(db_column='batchNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    batchstate = models.CharField(db_column='batchState', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fwhtpercentage = models.FloatField(db_column='fWHTPercentage', blank=True, null=True)  # Field name made lowercase.
    fwhtamount = models.FloatField(db_column='fWHTAmount', blank=True, null=True)  # Field name made lowercase.
    idinvnum = models.BigIntegerField(db_column='idInvNum', blank=True, null=True)  # Field name made lowercase.
    idinvoicelines = models.BigIntegerField(db_column='idInvoiceLines', blank=True, null=True)  # Field name made lowercase.
    grvnumber = models.CharField(db_column='GrvNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.CharField(db_column='OrderNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caccountname = models.CharField(db_column='cAccountName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fqtyprocessed = models.FloatField(db_column='fQtyProcessed', blank=True, null=True)  # Field name made lowercase.
    funitpriceexcl = models.FloatField(db_column='fUnitPriceExcl', blank=True, null=True)  # Field name made lowercase.
    funitpriceincl = models.FloatField(db_column='fUnitPriceIncl', blank=True, null=True)  # Field name made lowercase.
    ftaxrate = models.FloatField(db_column='fTaxRate', blank=True, null=True)  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeId', blank=True, null=True)  # Field name made lowercase.
    foreigncurrencyid = models.IntegerField(db_column='ForeignCurrencyID', blank=True, null=True)  # Field name made lowercase.
    funitpriceexclforeign = models.FloatField(db_column='fUnitPriceExclForeign', blank=True, null=True)  # Field name made lowercase.
    funitpriceinclforeign = models.FloatField(db_column='fUnitPriceInclForeign', blank=True, null=True)  # Field name made lowercase.
    wht_batch_ibranchid = models.IntegerField(db_column='WHT_Batch_iBranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WHT_Batch'


class WhtBatchstatus(models.Model):
    idbatchnumber = models.AutoField(db_column='idBatchNumber', primary_key=True)  # Field name made lowercase.
    batchnumber = models.CharField(db_column='batchNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    batchstatus = models.BooleanField(db_column='batchStatus', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    processingdate = models.DateTimeField(db_column='processingDate', blank=True, null=True)  # Field name made lowercase.
    wht_batchstatus_ibranchid = models.IntegerField(db_column='WHT_BatchStatus_iBranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WHT_BatchStatus'


class WhtState(models.Model):
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WHT_State'


class Whsemst(models.Model):
    whselink = models.AutoField(db_column='WhseLink', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    knownas = models.CharField(db_column='KnownAs', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=30, blank=True, null=True)  # Field name made lowercase.
    banklink = models.IntegerField(db_column='BankLink', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankaccnum = models.CharField(db_column='BankAccNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankacctype = models.CharField(db_column='BankAccType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modemtel = models.CharField(db_column='ModemTel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    defaultwhse = models.BooleanField(db_column='DefaultWhse')  # Field name made lowercase.
    addnewstock = models.BooleanField(db_column='AddNewStock')  # Field name made lowercase.
    dwarehousetimestamp = models.DateTimeField(db_column='dWarehouseTimeStamp', blank=True, null=True)  # Field name made lowercase.
    iwhsetypeid = models.IntegerField(db_column='iWhseTypeID')  # Field name made lowercase.
    ballowtobuyinto = models.BooleanField(db_column='bAllowToBuyInto')  # Field name made lowercase.
    ballowtosellfrom = models.BooleanField(db_column='bAllowToSellFrom')  # Field name made lowercase.
    ballownegstock = models.BooleanField(db_column='bAllowNegStock')  # Field name made lowercase.
    idefaultitemgroupid = models.IntegerField(db_column='iDefaultItemGroupID', blank=True, null=True)  # Field name made lowercase.
    ballowmultibinlocations = models.BooleanField(db_column='bAllowMultiBinLocations')  # Field name made lowercase.
    whsemst_ibranchid = models.IntegerField(db_column='WhseMst_iBranchID', blank=True, null=True)  # Field name made lowercase.
    whsemst_dcreateddate = models.DateTimeField(db_column='WhseMst_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    whsemst_dmodifieddate = models.DateTimeField(db_column='WhseMst_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    whsemst_icreatedbranchid = models.IntegerField(db_column='WhseMst_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    whsemst_imodifiedbranchid = models.IntegerField(db_column='WhseMst_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    whsemst_icreatedagentid = models.IntegerField(db_column='WhseMst_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    whsemst_imodifiedagentid = models.IntegerField(db_column='WhseMst_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    whsemst_ichangesetid = models.IntegerField(db_column='WhseMst_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    whsemst_checksum = models.TextField(db_column='WhseMst_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    busedefaultbinlevels = models.BooleanField(db_column='bUseDefaultBinLevels')  # Field name made lowercase.
    idefaultwhsesalesbinid = models.IntegerField(db_column='iDefaultWhseSalesBinID', blank=True, null=True)  # Field name made lowercase.
    idefaultwhsepurchasebinid = models.IntegerField(db_column='iDefaultWhsePurchaseBinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhseMst'


class Whsestk(models.Model):
    idwhsestk = models.BigAutoField(db_column='IdWhseStk', primary_key=True)  # Field name made lowercase.
    whwhseid = models.IntegerField(db_column='WHWhseID', blank=True, null=True)  # Field name made lowercase.
    whstocklink = models.IntegerField(db_column='WHStockLink')  # Field name made lowercase.
    whstockgroup = models.CharField(db_column='WHStockGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    whqtyonhand = models.FloatField(db_column='WHQtyOnHand')  # Field name made lowercase.
    whqtyonso = models.FloatField(db_column='WHQtyOnSO')  # Field name made lowercase.
    whqtyonpo = models.FloatField(db_column='WHQtyOnPO')  # Field name made lowercase.
    whqtyreserved = models.FloatField(db_column='WHQtyReserved')  # Field name made lowercase.
    whttinv = models.CharField(db_column='WHTTInv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    whttcrn = models.CharField(db_column='WHTTCrn', max_length=10, blank=True, null=True)  # Field name made lowercase.
    whttgrv = models.CharField(db_column='WHTTGrv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    whttrts = models.CharField(db_column='WHTTRts', max_length=10, blank=True, null=True)  # Field name made lowercase.
    whbarcode = models.CharField(db_column='WHBarCode', max_length=400, blank=True, null=True)  # Field name made lowercase.
    whre_ord_lvl = models.FloatField(db_column='WHRe_Ord_Lvl', blank=True, null=True)  # Field name made lowercase.
    whre_ord_qty = models.FloatField(db_column='WHRe_Ord_Qty', blank=True, null=True)  # Field name made lowercase.
    whmin_lvl = models.FloatField(db_column='WHMin_Lvl', blank=True, null=True)  # Field name made lowercase.
    whmax_lvl = models.FloatField(db_column='WHMax_Lvl', blank=True, null=True)  # Field name made lowercase.
    whusepricedefs = models.BooleanField(db_column='WHUsePriceDefs')  # Field name made lowercase.
    whuseinfodefs = models.BooleanField(db_column='WHUseInfoDefs')  # Field name made lowercase.
    whuseorderdefs = models.BooleanField(db_column='WHUseOrderDefs')  # Field name made lowercase.
    whusedefaultdefs = models.BooleanField(db_column='WHUseDefaultDefs')  # Field name made lowercase.
    whpackcode = models.CharField(db_column='WHPackCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    whjobqty = models.FloatField(db_column='WHJobQty')  # Field name made lowercase.
    ibinlocationid = models.IntegerField(db_column='iBinLocationID', blank=True, null=True)  # Field name made lowercase.
    flgrvcount = models.FloatField(db_column='fLGRVCount', blank=True, null=True)  # Field name made lowercase.
    whmfpqty = models.FloatField(db_column='WHMFPQty')  # Field name made lowercase.
    whusesupplierdefs = models.BooleanField(db_column='WHUseSupplierDefs')  # Field name made lowercase.
    faveragecost = models.FloatField(db_column='fAverageCost')  # Field name made lowercase.
    flatestcost = models.FloatField(db_column='fLatestCost')  # Field name made lowercase.
    flowestcost = models.FloatField(db_column='fLowestCost')  # Field name made lowercase.
    fhighestcost = models.FloatField(db_column='fHighestCost')  # Field name made lowercase.
    fmanualcost = models.FloatField(db_column='fManualCost')  # Field name made lowercase.
    fwhselastgrvcost = models.FloatField(db_column='fWhseLastGRVCost')  # Field name made lowercase.
    bwhallownegstock = models.BooleanField(db_column='bWHAllowNegStock')  # Field name made lowercase.
    fwhqtytodeliver = models.FloatField(db_column='fWHQtyToDeliver', blank=True, null=True)  # Field name made lowercase.
    whsestk_fleaddays = models.FloatField(db_column='WhseStk_fLeadDays', blank=True, null=True)  # Field name made lowercase.
    whbuyingagentid = models.IntegerField(db_column='WHBuyingAgentID', blank=True, null=True)  # Field name made lowercase.
    fibtqtytoissue = models.FloatField(db_column='fIBTQtyToIssue')  # Field name made lowercase.
    fibtqtytoreceive = models.FloatField(db_column='fIBTQtyToReceive')  # Field name made lowercase.
    whsestk_ibranchid = models.IntegerField(db_column='WhseStk_iBranchID', blank=True, null=True)  # Field name made lowercase.
    whsestk_dcreateddate = models.DateTimeField(db_column='WhseStk_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    whsestk_dmodifieddate = models.DateTimeField(db_column='WhseStk_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    whsestk_icreatedbranchid = models.IntegerField(db_column='WhseStk_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    whsestk_imodifiedbranchid = models.IntegerField(db_column='WhseStk_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    whsestk_icreatedagentid = models.IntegerField(db_column='WhseStk_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    whsestk_imodifiedagentid = models.IntegerField(db_column='WhseStk_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    whsestk_ichangesetid = models.IntegerField(db_column='WhseStk_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    whsestk_checksum = models.TextField(db_column='WhseStk_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'WhseStk'

class Dtbldeliverymethod(models.Model):
    iddeliverymethod = models.AutoField(db_column='IdDeliveryMethod', primary_key=True)  # Field name made lowercase.
    idelmethodid = models.IntegerField(db_column='iDelMethodID', blank=True, null=True)  # Field name made lowercase.
    cmethod = models.CharField(db_column='cMethod', max_length=35, blank=True, null=True)  # Field name made lowercase.
    ccomment = models.CharField(db_column='cComment', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bselect = models.BooleanField(db_column='bSelect', blank=True, null=True)  # Field name made lowercase.
    deffectivedate = models.DateTimeField(db_column='dEffectiveDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_dtblDeliveryMethod'


class Dtbldeliverynote(models.Model):
    iddeliverynote = models.AutoField(db_column='IdDeliveryNote', primary_key=True)  # Field name made lowercase.
    iaccountid = models.BigIntegerField(db_column='iAccountID', blank=True, null=True)  # Field name made lowercase.
    iinvoiceid = models.BigIntegerField(db_column='iInvoiceID', blank=True, null=True)  # Field name made lowercase.
    iinventoryid = models.BigIntegerField(db_column='iInventoryID', blank=True, null=True)  # Field name made lowercase.
    ibtblinvoicelineid = models.BigIntegerField(db_column='ibtblInvoiceLineID', blank=True, null=True)  # Field name made lowercase.
    iwarehouseid = models.BigIntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    cinvoicenumber = models.CharField(db_column='cInvoiceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdelnotenum = models.CharField(db_column='cDelNoteNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ftotalqty = models.FloatField(db_column='fTotalQty', blank=True, null=True)  # Field name made lowercase.
    fqtydelivered = models.FloatField(db_column='fQtyDelivered', blank=True, null=True)  # Field name made lowercase.
    fconfirmdeliveryqty = models.FloatField(db_column='fConfirmDeliveryQty', blank=True, null=True)  # Field name made lowercase.
    ddeliverydate = models.DateTimeField(db_column='dDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus', blank=True, null=True)  # Field name made lowercase.
    bisprinted = models.BooleanField(db_column='bIsPrinted', blank=True, null=True)  # Field name made lowercase.
    cordernum = models.CharField(db_column='cOrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bperinvoice = models.BooleanField(db_column='bPerInvoice', blank=True, null=True)  # Field name made lowercase.
    bislotitem = models.BooleanField(db_column='bIsLotItem', blank=True, null=True)  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID', blank=True, null=True)  # Field name made lowercase.
    clotnumber = models.CharField(db_column='cLotNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem', blank=True, null=True)  # Field name made lowercase.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID', blank=True, null=True)  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_dtbldeliverynote_ibranchid = models.IntegerField(db_column='_dtblDeliveryNote_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_dcreateddate = models.DateTimeField(db_column='_dtblDeliveryNote_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_dmodifieddate = models.DateTimeField(db_column='_dtblDeliveryNote_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_icreatedbranchid = models.IntegerField(db_column='_dtblDeliveryNote_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_imodifiedbranchid = models.IntegerField(db_column='_dtblDeliveryNote_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_icreatedagentid = models.IntegerField(db_column='_dtblDeliveryNote_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_imodifiedagentid = models.IntegerField(db_column='_dtblDeliveryNote_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_ichangesetid = models.IntegerField(db_column='_dtblDeliveryNote_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliverynote_checksum = models.TextField(db_column='_dtblDeliveryNote_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    istockbinlocationid = models.IntegerField(db_column='iStockBinLocationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_dtblDeliveryNote'


class Dtbldeliveryserials(models.Model):
    iddeliveryserials = models.AutoField(db_column='IdDeliverySerials', primary_key=True)  # Field name made lowercase.
    iinvoiceid = models.IntegerField(db_column='iInvoiceID', blank=True, null=True)  # Field name made lowercase.
    iinvoicelineid = models.BigIntegerField(db_column='iInvoiceLineID', blank=True, null=True)  # Field name made lowercase.
    iinvoicelinesn = models.IntegerField(db_column='iInvoiceLineSN', blank=True, null=True)  # Field name made lowercase.
    ideliverynoteid = models.IntegerField(db_column='iDeliveryNoteID', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus', blank=True, null=True)  # Field name made lowercase.
    cserialnumber = models.CharField(db_column='cSerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_dtbldeliveryserials_ibranchid = models.IntegerField(db_column='_dtblDeliverySerials_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_dcreateddate = models.DateTimeField(db_column='_dtblDeliverySerials_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_dmodifieddate = models.DateTimeField(db_column='_dtblDeliverySerials_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_icreatedbranchid = models.IntegerField(db_column='_dtblDeliverySerials_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_imodifiedbranchid = models.IntegerField(db_column='_dtblDeliverySerials_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_icreatedagentid = models.IntegerField(db_column='_dtblDeliverySerials_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_imodifiedagentid = models.IntegerField(db_column='_dtblDeliverySerials_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_ichangesetid = models.IntegerField(db_column='_dtblDeliverySerials_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dtbldeliveryserials_checksum = models.TextField(db_column='_dtblDeliverySerials_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_dtblDeliverySerials'


class Etbldeleted(models.Model):
    iddeleted = models.AutoField(db_column='idDeleted', primary_key=True)  # Field name made lowercase.
    ctablename = models.CharField(db_column='cTableName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cpkfields = models.CharField(db_column='cPKFields', max_length=512, blank=True, null=True)  # Field name made lowercase.
    cpkvalues = models.CharField(db_column='cPKValues', max_length=128, blank=True, null=True)  # Field name made lowercase.
    irowbranchid = models.IntegerField(db_column='iRowBranchID', blank=True, null=True)  # Field name made lowercase.
    ideletedatbranchid = models.IntegerField(db_column='iDeletedAtBranchID', blank=True, null=True)  # Field name made lowercase.
    field_auditdate = models.DateTimeField(db_column='_auditDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_audithostname = models.CharField(db_column='_auditHostName', max_length=64, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_auditsystemuser = models.CharField(db_column='_auditSystemUser', max_length=64, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_auditusername = models.CharField(db_column='_auditUserName', max_length=64, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_auditappname = models.CharField(db_column='_auditAppName', max_length=128, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    ichangesetid = models.IntegerField(db_column='iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    field_keyfields_checksum = models.TextField(db_column='_KeyFields_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblDeleted'


class Etbldoccat(models.Model):
    iddoccat = models.AutoField(db_column='idDocCat', primary_key=True)  # Field name made lowercase.
    cdoccatcode = models.CharField(db_column='cDocCatCode', max_length=30)  # Field name made lowercase.
    cdoccatdescription = models.CharField(db_column='cDocCatDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cdoccatlocation = models.CharField(db_column='cDocCatLocation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    idoccatgroupid = models.IntegerField(db_column='iDocCatGroupID', blank=True, null=True)  # Field name made lowercase.
    field_etbldoccat_ibranchid = models.IntegerField(db_column='_etblDocCat_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_dcreateddate = models.DateTimeField(db_column='_etblDocCat_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_dmodifieddate = models.DateTimeField(db_column='_etblDocCat_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_icreatedbranchid = models.IntegerField(db_column='_etblDocCat_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_imodifiedbranchid = models.IntegerField(db_column='_etblDocCat_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_icreatedagentid = models.IntegerField(db_column='_etblDocCat_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_imodifiedagentid = models.IntegerField(db_column='_etblDocCat_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_ichangesetid = models.IntegerField(db_column='_etblDocCat_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccat_checksum = models.TextField(db_column='_etblDocCat_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblDocCat'


class Etbldoccatgroup(models.Model):
    iddoccatgroup = models.AutoField(db_column='idDocCatGroup', primary_key=True)  # Field name made lowercase.
    cdoccatgroupcode = models.CharField(db_column='cDocCatGroupCode', max_length=30)  # Field name made lowercase.
    cdoccatgroupdescription = models.CharField(db_column='cDocCatGroupDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cdoccatgrouplocation = models.CharField(db_column='cDocCatGroupLocation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    field_etbldoccatgroup_ibranchid = models.IntegerField(db_column='_etblDocCatGroup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_dcreateddate = models.DateTimeField(db_column='_etblDocCatGroup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_dmodifieddate = models.DateTimeField(db_column='_etblDocCatGroup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_icreatedbranchid = models.IntegerField(db_column='_etblDocCatGroup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_imodifiedbranchid = models.IntegerField(db_column='_etblDocCatGroup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_icreatedagentid = models.IntegerField(db_column='_etblDocCatGroup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_imodifiedagentid = models.IntegerField(db_column='_etblDocCatGroup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_ichangesetid = models.IntegerField(db_column='_etblDocCatGroup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldoccatgroup_checksum = models.TextField(db_column='_etblDocCatGroup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblDocCatGroup'


class Etbldocprofiles(models.Model):
    iddocprofiles = models.AutoField(db_column='idDocProfiles', primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=20)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=120, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    idoctype = models.IntegerField(db_column='iDocType')  # Field name made lowercase.
    idocsubtype = models.IntegerField(db_column='iDocSubType')  # Field name made lowercase.
    busedefaults = models.BooleanField(db_column='bUseDefaults')  # Field name made lowercase.
    bautonum = models.BooleanField(db_column='bAutoNum')  # Field name made lowercase.
    inextautonum = models.IntegerField(db_column='iNextAutoNum', blank=True, null=True)  # Field name made lowercase.
    iautonumpadlength = models.IntegerField(db_column='iAutoNumPadLength', blank=True, null=True)  # Field name made lowercase.
    cautonumprefix = models.CharField(db_column='cAutoNumPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    buniquenum = models.BooleanField(db_column='bUniqueNum', blank=True, null=True)  # Field name made lowercase.
    idoctrcodeid = models.IntegerField(db_column='iDocTrCodeID', blank=True, null=True)  # Field name made lowercase.
    idochomelayoutid = models.IntegerField(db_column='iDocHomeLayoutID', blank=True, null=True)  # Field name made lowercase.
    bdochomelayoutprompt = models.BooleanField(db_column='bDocHomeLayoutPrompt')  # Field name made lowercase.
    idocforeignlayoutid = models.IntegerField(db_column='iDocForeignLayoutID', blank=True, null=True)  # Field name made lowercase.
    bdocforeignlayoutprompt = models.BooleanField(db_column='bDocForeignLayoutPrompt')  # Field name made lowercase.
    iexclusivedoc = models.IntegerField(db_column='iExclusiveDoc', blank=True, null=True)  # Field name made lowercase.
    itaxperdoc = models.IntegerField(db_column='iTaxPerDoc', blank=True, null=True)  # Field name made lowercase.
    bhasbeenused = models.BooleanField(db_column='bHasBeenUsed')  # Field name made lowercase.
    bisuserlayout = models.BooleanField(db_column='bIsUserLayout')  # Field name made lowercase.
    bisuserforeignlayout = models.BooleanField(db_column='bIsUserForeignLayout')  # Field name made lowercase.
    idochomeemaillayoutid = models.IntegerField(db_column='iDocHomeEmailLayoutID', blank=True, null=True)  # Field name made lowercase.
    bdochomeemaillayoutprompt = models.BooleanField(db_column='bDocHomeEmailLayoutPrompt')  # Field name made lowercase.
    bisuseremaillayout = models.BooleanField(db_column='bIsUserEmailLayout')  # Field name made lowercase.
    idocforeignemaillayoutid = models.IntegerField(db_column='iDocForeignEmailLayoutID', blank=True, null=True)  # Field name made lowercase.
    bdocforeignemaillayoutprompt = models.BooleanField(db_column='bDocForeignEmailLayoutPrompt')  # Field name made lowercase.
    bisuserforeignemaillayout = models.BooleanField(db_column='bIsUserForeignEmailLayout')  # Field name made lowercase.
    field_etbldocprofiles_ibranchid = models.IntegerField(db_column='_etblDocProfiles_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_dcreateddate = models.DateTimeField(db_column='_etblDocProfiles_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_dmodifieddate = models.DateTimeField(db_column='_etblDocProfiles_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_icreatedbranchid = models.IntegerField(db_column='_etblDocProfiles_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_imodifiedbranchid = models.IntegerField(db_column='_etblDocProfiles_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_icreatedagentid = models.IntegerField(db_column='_etblDocProfiles_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_imodifiedagentid = models.IntegerField(db_column='_etblDocProfiles_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_ichangesetid = models.IntegerField(db_column='_etblDocProfiles_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbldocprofiles_checksum = models.TextField(db_column='_etblDocProfiles_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblDocProfiles'


class Etblduration(models.Model):
    iduration = models.AutoField(db_column='iDuration', primary_key=True)  # Field name made lowercase.
    itype = models.CharField(db_column='iType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iduetype = models.CharField(db_column='iDueType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ddatedue = models.DateTimeField(db_column='dDateDue', blank=True, null=True)  # Field name made lowercase.
    itimetaken = models.IntegerField(db_column='iTimeTaken', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblDuration'


class Etbleftgatewaytype(models.Model):
    gatewayid = models.AutoField(db_column='GatewayID', primary_key=True)  # Field name made lowercase.
    ccode = models.SmallIntegerField(db_column='cCode', blank=True, null=True)  # Field name made lowercase.
    cgatewayname = models.CharField(db_column='cGatewayName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    field_etbleftgatewaytype_ibranchid = models.IntegerField(db_column='_etblEFTGatewayType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_dcreateddate = models.DateTimeField(db_column='_etblEFTGatewayType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_dmodifieddate = models.DateTimeField(db_column='_etblEFTGatewayType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_icreatedbranchid = models.IntegerField(db_column='_etblEFTGatewayType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_imodifiedbranchid = models.IntegerField(db_column='_etblEFTGatewayType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_icreatedagentid = models.IntegerField(db_column='_etblEFTGatewayType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_imodifiedagentid = models.IntegerField(db_column='_etblEFTGatewayType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_ichangesetid = models.IntegerField(db_column='_etblEFTGatewayType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftgatewaytype_checksum = models.TextField(db_column='_etblEFTGatewayType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEFTGatewayType'


class Etbleftreference(models.Model):
    idnumber = models.AutoField(db_column='idNumber', primary_key=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    field_etbleftreference_ibranchid = models.IntegerField(db_column='_etblEFTReference_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_dcreateddate = models.DateTimeField(db_column='_etblEFTReference_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_dmodifieddate = models.DateTimeField(db_column='_etblEFTReference_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_icreatedbranchid = models.IntegerField(db_column='_etblEFTReference_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_imodifiedbranchid = models.IntegerField(db_column='_etblEFTReference_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_icreatedagentid = models.IntegerField(db_column='_etblEFTReference_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_imodifiedagentid = models.IntegerField(db_column='_etblEFTReference_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_ichangesetid = models.IntegerField(db_column='_etblEFTReference_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftreference_checksum = models.TextField(db_column='_etblEFTReference_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEFTReference'


class Etbleftsfilelayout(models.Model):
    ideftslayout = models.AutoField(db_column='idEFTSLayout', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=200)  # Field name made lowercase.
    bsystemlayout = models.BooleanField(db_column='bSystemLayout')  # Field name made lowercase.
    cnameoutfile = models.CharField(db_column='cNameOutFile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctypeoutfile = models.CharField(db_column='cTypeOutFile', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idelimiteroutfile = models.IntegerField(db_column='iDelimiterOutFile', blank=True, null=True)  # Field name made lowercase.
    ieolcharoutfile = models.IntegerField(db_column='iEOLCharOutFile', blank=True, null=True)  # Field name made lowercase.
    icountrycode = models.IntegerField(db_column='iCountryCode')  # Field name made lowercase.
    inoofheaders = models.IntegerField(db_column='iNoOfHeaders', blank=True, null=True)  # Field name made lowercase.
    inooftransactions = models.IntegerField(db_column='iNoOFTransactions', blank=True, null=True)  # Field name made lowercase.
    inooffooters = models.IntegerField(db_column='iNoOfFooters', blank=True, null=True)  # Field name made lowercase.
    imaxnoofrecords = models.IntegerField(db_column='iMaxNoOfRecords', blank=True, null=True)  # Field name made lowercase.
    ihashtotalcalc = models.IntegerField(db_column='iHashTotalCalc')  # Field name made lowercase.
    cseednumber = models.CharField(db_column='cSeedNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ballowtestrun = models.BooleanField(db_column='bAllowTestRun')  # Field name made lowercase.
    baskbatchno = models.BooleanField(db_column='bAskBatchNo')  # Field name made lowercase.
    idaydifference = models.IntegerField(db_column='iDayDifference')  # Field name made lowercase.
    iacbservicetype = models.IntegerField(db_column='iACBServiceType')  # Field name made lowercase.
    bincrementfilename = models.BooleanField(db_column='bIncrementFileName')  # Field name made lowercase.
    cusername = models.CharField(db_column='cUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpassword = models.CharField(db_column='cPassword', max_length=160, blank=True, null=True)  # Field name made lowercase.
    cpin = models.CharField(db_column='cPin', max_length=160, blank=True, null=True)  # Field name made lowercase.
    ieftsorderletterid = models.IntegerField(db_column='iEFTSOrderLetterID')  # Field name made lowercase.
    isourcelayoutid = models.IntegerField(db_column='iSourceLayoutID', blank=True, null=True)  # Field name made lowercase.
    cxslt = models.TextField(db_column='cXSLT', blank=True, null=True)  # Field name made lowercase.
    field_etbleftsfilelayout_ibranchid = models.IntegerField(db_column='_etblEFTSFileLayout_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_dcreateddate = models.DateTimeField(db_column='_etblEFTSFileLayout_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_dmodifieddate = models.DateTimeField(db_column='_etblEFTSFileLayout_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_icreatedbranchid = models.IntegerField(db_column='_etblEFTSFileLayout_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_imodifiedbranchid = models.IntegerField(db_column='_etblEFTSFileLayout_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_icreatedagentid = models.IntegerField(db_column='_etblEFTSFileLayout_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_imodifiedagentid = models.IntegerField(db_column='_etblEFTSFileLayout_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_ichangesetid = models.IntegerField(db_column='_etblEFTSFileLayout_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayout_checksum = models.TextField(db_column='_etblEFTSFileLayout_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEFTSFileLayout'


class Etbleftsfilelayoutdetails(models.Model):
    ideftslayoutdetails = models.AutoField(db_column='idEFTSLayoutDetails', primary_key=True)  # Field name made lowercase.
    ieftslayoutid = models.IntegerField(db_column='iEFTSLayoutID')  # Field name made lowercase.
    crecordtype = models.CharField(db_column='cRecordType', max_length=50)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=30)  # Field name made lowercase.
    ifieldlength = models.IntegerField(db_column='iFieldLength')  # Field name made lowercase.
    idecimalplaces = models.IntegerField(db_column='iDecimalPlaces', blank=True, null=True)  # Field name made lowercase.
    cfieldformat = models.CharField(db_column='cFieldFormat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ifiller = models.IntegerField(db_column='iFiller', blank=True, null=True)  # Field name made lowercase.
    bfieldinuse = models.BooleanField(db_column='bFieldInUse')  # Field name made lowercase.
    cvaluetype = models.CharField(db_column='cValueType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cdefaultvalue = models.CharField(db_column='cDefaultValue', max_length=120, blank=True, null=True)  # Field name made lowercase.
    field_etbleftsfilelayoutdetails_ibranchid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_dcreateddate = models.DateTimeField(db_column='_etblEFTSFileLayoutDetails_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_dmodifieddate = models.DateTimeField(db_column='_etblEFTSFileLayoutDetails_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_icreatedbranchid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_imodifiedbranchid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_icreatedagentid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_imodifiedagentid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_ichangesetid = models.IntegerField(db_column='_etblEFTSFileLayoutDetails_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleftsfilelayoutdetails_checksum = models.TextField(db_column='_etblEFTSFileLayoutDetails_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEFTSFileLayoutDetails'


class Etbleucommodity(models.Model):
    ideucommodity = models.AutoField(db_column='IDEUCommodity', primary_key=True)  # Field name made lowercase.
    ceucommoditycode = models.CharField(db_column='cEUCommodityCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ceucommoditydescription = models.CharField(db_column='cEUCommodityDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field_etbleucommodity_ibranchid = models.IntegerField(db_column='_etblEUCommodity_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_dcreateddate = models.DateTimeField(db_column='_etblEUCommodity_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_dmodifieddate = models.DateTimeField(db_column='_etblEUCommodity_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_icreatedbranchid = models.IntegerField(db_column='_etblEUCommodity_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_imodifiedbranchid = models.IntegerField(db_column='_etblEUCommodity_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_icreatedagentid = models.IntegerField(db_column='_etblEUCommodity_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_imodifiedagentid = models.IntegerField(db_column='_etblEUCommodity_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_ichangesetid = models.IntegerField(db_column='_etblEUCommodity_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucommodity_checksum = models.TextField(db_column='_etblEUCommodity_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEUCommodity'


class Etbleucountry(models.Model):
    ideucountry = models.AutoField(db_column='IDEUCountry', primary_key=True)  # Field name made lowercase.
    ceucountrycode = models.CharField(db_column='cEUCountryCode', max_length=2)  # Field name made lowercase.
    ceucountryname = models.CharField(db_column='cEUCountryName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    field_etbleucountry_ibranchid = models.IntegerField(db_column='_etblEUCountry_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_dcreateddate = models.DateTimeField(db_column='_etblEUCountry_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_dmodifieddate = models.DateTimeField(db_column='_etblEUCountry_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_icreatedbranchid = models.IntegerField(db_column='_etblEUCountry_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_imodifiedbranchid = models.IntegerField(db_column='_etblEUCountry_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_icreatedagentid = models.IntegerField(db_column='_etblEUCountry_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_imodifiedagentid = models.IntegerField(db_column='_etblEUCountry_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_ichangesetid = models.IntegerField(db_column='_etblEUCountry_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleucountry_checksum = models.TextField(db_column='_etblEUCountry_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEUCountry'


class Etbleunotc(models.Model):
    ideunotc = models.AutoField(db_column='IDEUNoTC', primary_key=True)  # Field name made lowercase.
    ceunotccode = models.CharField(db_column='cEUNoTCCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ceunotcdescription = models.CharField(db_column='cEUNoTCDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    field_etbleunotc_ibranchid = models.IntegerField(db_column='_etblEUNoTC_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_dcreateddate = models.DateTimeField(db_column='_etblEUNoTC_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_dmodifieddate = models.DateTimeField(db_column='_etblEUNoTC_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_icreatedbranchid = models.IntegerField(db_column='_etblEUNoTC_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_imodifiedbranchid = models.IntegerField(db_column='_etblEUNoTC_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_icreatedagentid = models.IntegerField(db_column='_etblEUNoTC_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_imodifiedagentid = models.IntegerField(db_column='_etblEUNoTC_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_ichangesetid = models.IntegerField(db_column='_etblEUNoTC_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleunotc_checksum = models.TextField(db_column='_etblEUNoTC_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEUNoTC'


class Etbleusupplementaryunit(models.Model):
    ideusupplementaryunit = models.AutoField(db_column='IDEUSupplementaryUnit', primary_key=True)  # Field name made lowercase.
    ceusupplementaryunitcode = models.CharField(db_column='cEUSupplementaryUnitCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ceusupplementaryunitdescription = models.CharField(db_column='cEUSupplementaryUnitDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etbleusupplementaryunit_ibranchid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_dcreateddate = models.DateTimeField(db_column='_etblEUSupplementaryUnit_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_dmodifieddate = models.DateTimeField(db_column='_etblEUSupplementaryUnit_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_icreatedbranchid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_imodifiedbranchid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_icreatedagentid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_imodifiedagentid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_ichangesetid = models.IntegerField(db_column='_etblEUSupplementaryUnit_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbleusupplementaryunit_checksum = models.TextField(db_column='_etblEUSupplementaryUnit_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblEUSupplementaryUnit'


class Etblfiscaldata(models.Model):
    idfiscaldata = models.AutoField(db_column='idFiscalData', primary_key=True)  # Field name made lowercase.
    cdevicetpin = models.CharField(db_column='cDeviceTPIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itaxaid = models.IntegerField(db_column='iTaxAID', blank=True, null=True)  # Field name made lowercase.
    ftaxarate = models.FloatField(db_column='fTaxARate', blank=True, null=True)  # Field name made lowercase.
    itaxbid = models.IntegerField(db_column='iTaxBID', blank=True, null=True)  # Field name made lowercase.
    ftaxbrate = models.FloatField(db_column='fTaxBRate', blank=True, null=True)  # Field name made lowercase.
    itaxcid = models.IntegerField(db_column='iTaxCID', blank=True, null=True)  # Field name made lowercase.
    ftaxcrate = models.FloatField(db_column='fTaxCRate', blank=True, null=True)  # Field name made lowercase.
    itaxdid = models.IntegerField(db_column='iTaxDID', blank=True, null=True)  # Field name made lowercase.
    ftaxdrate = models.FloatField(db_column='fTaxDRate', blank=True, null=True)  # Field name made lowercase.
    itaxeid = models.IntegerField(db_column='iTaxEID', blank=True, null=True)  # Field name made lowercase.
    ftaxerate = models.FloatField(db_column='fTaxERate', blank=True, null=True)  # Field name made lowercase.
    itaxfid = models.IntegerField(db_column='iTaxFID', blank=True, null=True)  # Field name made lowercase.
    ftaxfrate = models.FloatField(db_column='fTaxFRate', blank=True, null=True)  # Field name made lowercase.
    itaxgid = models.IntegerField(db_column='iTaxGID', blank=True, null=True)  # Field name made lowercase.
    ftaxgrate = models.FloatField(db_column='fTaxGRate', blank=True, null=True)  # Field name made lowercase.
    itaxhid = models.IntegerField(db_column='iTaxHID', blank=True, null=True)  # Field name made lowercase.
    ftaxhrate = models.FloatField(db_column='fTaxHRate', blank=True, null=True)  # Field name made lowercase.
    ctaxjson = models.CharField(db_column='cTaxJSON', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ctaxpayername = models.CharField(db_column='cTaxpayerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ctaxpayeraddress = models.CharField(db_column='cTaxpayerAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cesdserialnumber = models.CharField(db_column='cESDSerialNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cserialnumber = models.CharField(db_column='cSerialNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bislocked = models.BooleanField(db_column='bIsLocked', blank=True, null=True)  # Field name made lowercase.
    field_etblfiscaldata_ibranchid = models.IntegerField(db_column='_etblFiscalData_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_dcreateddate = models.DateTimeField(db_column='_etblFiscalData_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_dmodifieddate = models.DateTimeField(db_column='_etblFiscalData_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_icreatedbranchid = models.IntegerField(db_column='_etblFiscalData_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_imodifiedbranchid = models.IntegerField(db_column='_etblFiscalData_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_icreatedagentid = models.IntegerField(db_column='_etblFiscalData_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_imodifiedagentid = models.IntegerField(db_column='_etblFiscalData_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_ichangesetid = models.IntegerField(db_column='_etblFiscalData_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscaldata_checksum = models.TextField(db_column='_etblFiscalData_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblFiscalData'


class Etblfiscalprintermodels(models.Model):
    ifiscalprintermodelsid = models.AutoField(db_column='iFiscalPrinterModelsId', primary_key=True)  # Field name made lowercase.
    cprintermodelname = models.CharField(db_column='cPrinterModelName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cprintermodelmanufacture = models.CharField(db_column='cPrinterModelManufacture', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cfiscaldrivername = models.CharField(db_column='cFiscalDriverName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ballowalphanumdoc = models.BooleanField(db_column='bAllowAlphaNumDoc')  # Field name made lowercase.
    bisprinter = models.BooleanField(db_column='bIsPrinter')  # Field name made lowercase.
    field_etblfiscalprintermodels_ibranchid = models.IntegerField(db_column='_etblFiscalPrinterModels_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_dcreateddate = models.DateTimeField(db_column='_etblFiscalPrinterModels_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_dmodifieddate = models.DateTimeField(db_column='_etblFiscalPrinterModels_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_icreatedbranchid = models.IntegerField(db_column='_etblFiscalPrinterModels_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_imodifiedbranchid = models.IntegerField(db_column='_etblFiscalPrinterModels_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_icreatedagentid = models.IntegerField(db_column='_etblFiscalPrinterModels_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_imodifiedagentid = models.IntegerField(db_column='_etblFiscalPrinterModels_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_ichangesetid = models.IntegerField(db_column='_etblFiscalPrinterModels_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprintermodels_checksum = models.TextField(db_column='_etblFiscalPrinterModels_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblFiscalPrinterModels'


class Etblfiscalprinters(models.Model):
    ifiscalprinterid = models.AutoField(db_column='iFiscalPrinterId', primary_key=True)  # Field name made lowercase.
    iposdeviceid = models.IntegerField(db_column='iPOSDeviceId', blank=True, null=True)  # Field name made lowercase.
    cipaddress = models.CharField(db_column='cIPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cportnumber = models.CharField(db_column='cPortNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    csubnetmask = models.CharField(db_column='cSubnetMask', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cdefaultgateway = models.CharField(db_column='cDefaultGateway', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cmacaddress = models.CharField(db_column='cMACAddress', max_length=17, blank=True, null=True)  # Field name made lowercase.
    itaxtypea = models.IntegerField(db_column='iTaxTypeA', blank=True, null=True)  # Field name made lowercase.
    itaxtypeb = models.IntegerField(db_column='iTaxTypeB', blank=True, null=True)  # Field name made lowercase.
    itaxtypec = models.IntegerField(db_column='iTaxTypeC', blank=True, null=True)  # Field name made lowercase.
    itaxtyped = models.IntegerField(db_column='iTaxTypeD', blank=True, null=True)  # Field name made lowercase.
    itaxtypee = models.IntegerField(db_column='iTaxTypeE', blank=True, null=True)  # Field name made lowercase.
    itaxtypef = models.IntegerField(db_column='iTaxTypeF', blank=True, null=True)  # Field name made lowercase.
    bdeviceconfigured = models.BooleanField(db_column='bDeviceConfigured', blank=True, null=True)  # Field name made lowercase.
    cregistrationkey = models.CharField(db_column='cRegistrationKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctinnumber = models.CharField(db_column='cTINNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmrcnumber = models.CharField(db_column='cMRCNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblfiscalprinters_ibranchid = models.IntegerField(db_column='_etblFiscalPrinters_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_dcreateddate = models.DateTimeField(db_column='_etblFiscalPrinters_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_dmodifieddate = models.DateTimeField(db_column='_etblFiscalPrinters_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_icreatedbranchid = models.IntegerField(db_column='_etblFiscalPrinters_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_imodifiedbranchid = models.IntegerField(db_column='_etblFiscalPrinters_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_icreatedagentid = models.IntegerField(db_column='_etblFiscalPrinters_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_imodifiedagentid = models.IntegerField(db_column='_etblFiscalPrinters_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_ichangesetid = models.IntegerField(db_column='_etblFiscalPrinters_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblfiscalprinters_checksum = models.TextField(db_column='_etblFiscalPrinters_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    itaxtypeg = models.IntegerField(db_column='iTaxTypeG', blank=True, null=True)  # Field name made lowercase.
    itaxtypeh = models.IntegerField(db_column='iTaxTypeH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblFiscalPrinters'


class Etblglaccounttypes(models.Model):
    idglaccounttype = models.IntegerField(db_column='idGLAccountType', primary_key=True)  # Field name made lowercase.
    caccounttypedescription = models.CharField(db_column='cAccountTypeDescription', max_length=100)  # Field name made lowercase.
    bisbalancesheet = models.BooleanField(db_column='bIsBalanceSheet')  # Field name made lowercase.
    bisdebit = models.BooleanField(db_column='bIsDebit')  # Field name made lowercase.
    ireportinggroup = models.IntegerField(db_column='iReportingGroup')  # Field name made lowercase.
    ireportinggroupsort = models.IntegerField(db_column='iReportingGroupSort')  # Field name made lowercase.
    bdualprinting = models.BooleanField(db_column='bDualPrinting')  # Field name made lowercase.
    field_etblglaccounttypes_ibranchid = models.IntegerField(db_column='_etblGLAccountTypes_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_dcreateddate = models.DateTimeField(db_column='_etblGLAccountTypes_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_dmodifieddate = models.DateTimeField(db_column='_etblGLAccountTypes_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_icreatedbranchid = models.IntegerField(db_column='_etblGLAccountTypes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_imodifiedbranchid = models.IntegerField(db_column='_etblGLAccountTypes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_icreatedagentid = models.IntegerField(db_column='_etblGLAccountTypes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_imodifiedagentid = models.IntegerField(db_column='_etblGLAccountTypes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_ichangesetid = models.IntegerField(db_column='_etblGLAccountTypes_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglaccounttypes_checksum = models.TextField(db_column='_etblGLAccountTypes_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLAccountTypes'


class Etblglloanaccountlinks(models.Model):
    idglloanaccountlinks = models.AutoField(db_column='idGLLoanAccountLinks', primary_key=True)  # Field name made lowercase.
    iabloanaccountid = models.IntegerField(db_column='iABLoanAccountID', blank=True, null=True)  # Field name made lowercase.
    ibranchloanaccountid = models.IntegerField(db_column='iBranchLoanAccountID', blank=True, null=True)  # Field name made lowercase.
    field_etblglloanaccountlinks_ibranchid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_dcreateddate = models.DateTimeField(db_column='_etblGLLoanAccountLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_dmodifieddate = models.DateTimeField(db_column='_etblGLLoanAccountLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_icreatedbranchid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_imodifiedbranchid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_icreatedagentid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_imodifiedagentid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_ichangesetid = models.IntegerField(db_column='_etblGLLoanAccountLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglloanaccountlinks_checksum = models.TextField(db_column='_etblGLLoanAccountLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLLoanAccountLinks'


class Etblglreportcategory(models.Model):
    idreportcategory = models.AutoField(db_column='idReportCategory', primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=40)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblglreportcategory_ibranchid = models.IntegerField(db_column='_etblGLReportCategory_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_dcreateddate = models.DateTimeField(db_column='_etblGLReportCategory_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_dmodifieddate = models.DateTimeField(db_column='_etblGLReportCategory_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_icreatedbranchid = models.IntegerField(db_column='_etblGLReportCategory_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_imodifiedbranchid = models.IntegerField(db_column='_etblGLReportCategory_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_icreatedagentid = models.IntegerField(db_column='_etblGLReportCategory_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_imodifiedagentid = models.IntegerField(db_column='_etblGLReportCategory_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_ichangesetid = models.IntegerField(db_column='_etblGLReportCategory_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglreportcategory_checksum = models.TextField(db_column='_etblGLReportCategory_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLReportCategory'


class Etblglrevisebudget(models.Model):
    idglrevisebudget = models.AutoField(db_column='idGLReviseBudget', primary_key=True)  # Field name made lowercase.
    iglaccountid = models.IntegerField(db_column='iGLAccountID')  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    iperiod = models.IntegerField(db_column='iPeriod')  # Field name made lowercase.
    fnewbudget = models.FloatField(db_column='fNewBudget')  # Field name made lowercase.
    foldbudget = models.FloatField(db_column='fOldBudget')  # Field name made lowercase.
    creason = models.CharField(db_column='cReason', max_length=50)  # Field name made lowercase.
    ddate = models.DateTimeField(db_column='dDate')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    itxbranchrevisedbudgetid = models.IntegerField(db_column='iTxBranchRevisedBudgetID')  # Field name made lowercase.
    fnewbudgetforeign = models.FloatField(db_column='fNewBudgetForeign')  # Field name made lowercase.
    foldbudgetforeign = models.FloatField(db_column='fOldBudgetForeign')  # Field name made lowercase.
    field_etblglrevisebudget_ibranchid = models.IntegerField(db_column='_etblGLReviseBudget_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_dcreateddate = models.DateTimeField(db_column='_etblGLReviseBudget_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_dmodifieddate = models.DateTimeField(db_column='_etblGLReviseBudget_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_icreatedbranchid = models.IntegerField(db_column='_etblGLReviseBudget_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_imodifiedbranchid = models.IntegerField(db_column='_etblGLReviseBudget_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_icreatedagentid = models.IntegerField(db_column='_etblGLReviseBudget_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_imodifiedagentid = models.IntegerField(db_column='_etblGLReviseBudget_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_ichangesetid = models.IntegerField(db_column='_etblGLReviseBudget_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudget_checksum = models.TextField(db_column='_etblGLReviseBudget_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLReviseBudget'


class Etblglrevisebudgetprev(models.Model):
    idglrevisebudgetprev = models.AutoField(db_column='idGLReviseBudgetPrev', primary_key=True)  # Field name made lowercase.
    iglaccountprevid = models.IntegerField(db_column='iGLAccountPrevID')  # Field name made lowercase.
    iprojectprevid = models.IntegerField(db_column='iProjectPrevID')  # Field name made lowercase.
    iperiodprevid = models.IntegerField(db_column='iPeriodPrevID')  # Field name made lowercase.
    fnewbudgetprev = models.FloatField(db_column='fNewBudgetPrev', blank=True, null=True)  # Field name made lowercase.
    foldbudgetprev = models.FloatField(db_column='fOldBudgetPrev', blank=True, null=True)  # Field name made lowercase.
    creasonprev = models.CharField(db_column='cReasonPrev', max_length=50)  # Field name made lowercase.
    ddateprev = models.DateTimeField(db_column='dDatePrev', blank=True, null=True)  # Field name made lowercase.
    iagentidprev = models.IntegerField(db_column='iAgentIDPrev', blank=True, null=True)  # Field name made lowercase.
    fnewbudgetprevforeign = models.FloatField(db_column='fNewBudgetPrevForeign')  # Field name made lowercase.
    foldbudgetprevforeign = models.FloatField(db_column='fOldBudgetPrevForeign')  # Field name made lowercase.
    field_etblglrevisebudgetprev_ibranchid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_dcreateddate = models.DateTimeField(db_column='_etblGLReviseBudgetPrev_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_dmodifieddate = models.DateTimeField(db_column='_etblGLReviseBudgetPrev_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_icreatedbranchid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_imodifiedbranchid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_icreatedagentid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_imodifiedagentid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_ichangesetid = models.IntegerField(db_column='_etblGLReviseBudgetPrev_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglrevisebudgetprev_checksum = models.TextField(db_column='_etblGLReviseBudgetPrev_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLReviseBudgetPrev'


class Etblglsegment(models.Model):
    idsegment = models.AutoField(db_column='idSegment', primary_key=True)  # Field name made lowercase.
    isegmentno = models.IntegerField(db_column='iSegmentNo')  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=40)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isegmentbranchid = models.IntegerField(db_column='iSegmentBranchID', blank=True, null=True)  # Field name made lowercase.
    field_etblglsegment_ibranchid = models.IntegerField(db_column='_etblGLSegment_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_dcreateddate = models.DateTimeField(db_column='_etblGLSegment_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_dmodifieddate = models.DateTimeField(db_column='_etblGLSegment_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_icreatedbranchid = models.IntegerField(db_column='_etblGLSegment_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_imodifiedbranchid = models.IntegerField(db_column='_etblGLSegment_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_icreatedagentid = models.IntegerField(db_column='_etblGLSegment_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_imodifiedagentid = models.IntegerField(db_column='_etblGLSegment_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_ichangesetid = models.IntegerField(db_column='_etblGLSegment_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegment_checksum = models.TextField(db_column='_etblGLSegment_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    imscoaaccountid = models.IntegerField(db_column='imSCOAAccountID', blank=True, null=True)  # Field name made lowercase.
    mscoaid = models.CharField(db_column='mSCOAId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblGLSegment'


class Etblglsegmentsetup(models.Model):
    idsegmentno = models.IntegerField(db_column='idSegmentNo', primary_key=True)  # Field name made lowercase.
    bforcevalue = models.BooleanField(db_column='bForceValue')  # Field name made lowercase.
    bsegmentused = models.BooleanField(db_column='bSegmentUsed')  # Field name made lowercase.
    csegmentlabel = models.CharField(db_column='cSegmentLabel', max_length=35)  # Field name made lowercase.
    csegmentmask = models.CharField(db_column='cSegmentMask', max_length=40, blank=True, null=True)  # Field name made lowercase.
    binuse = models.BooleanField(db_column='bInUse')  # Field name made lowercase.
    bisbranchsegment = models.BooleanField(db_column='bIsBranchSegment')  # Field name made lowercase.
    field_etblglsegmentsetup_ibranchid = models.IntegerField(db_column='_etblGLSegmentSetup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_dcreateddate = models.DateTimeField(db_column='_etblGLSegmentSetup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_dmodifieddate = models.DateTimeField(db_column='_etblGLSegmentSetup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_icreatedbranchid = models.IntegerField(db_column='_etblGLSegmentSetup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_imodifiedbranchid = models.IntegerField(db_column='_etblGLSegmentSetup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_icreatedagentid = models.IntegerField(db_column='_etblGLSegmentSetup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_imodifiedagentid = models.IntegerField(db_column='_etblGLSegmentSetup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_ichangesetid = models.IntegerField(db_column='_etblGLSegmentSetup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglsegmentsetup_checksum = models.TextField(db_column='_etblGLSegmentSetup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLSegmentSetup'


class Etblglmscoaaccounts(models.Model):
    idglmscoaaccount = models.AutoField(db_column='idGLmSCOAAccount', primary_key=True)  # Field name made lowercase.
    scoaid = models.CharField(db_column='SCOAId', max_length=50)  # Field name made lowercase.
    parentscoaid = models.CharField(db_column='ParentSCOAId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    definitiondescription = models.TextField(db_column='DefinitionDescription', blank=True, null=True)  # Field name made lowercase.
    scoafile = models.CharField(db_column='SCOAFile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scoaaccount = models.CharField(db_column='SCOAAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scoalevel = models.IntegerField(db_column='SCOALevel', blank=True, null=True)  # Field name made lowercase.
    excelrownumber = models.IntegerField(db_column='ExcelRowNumber', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='ShortDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vatstatus = models.CharField(db_column='VATStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    breakdownallowed = models.CharField(db_column='BreakDownAllowed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    principle = models.CharField(db_column='Principle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    applicableto = models.CharField(db_column='ApplicableTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bpostinglevel = models.BooleanField(db_column='bPostingLevel', blank=True, null=True)  # Field name made lowercase.
    postingleveldescription = models.CharField(db_column='PostingLevelDescription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountnumberprefix = models.CharField(db_column='AccountNumberPrefix', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountnumber1 = models.IntegerField(db_column='AccountNumber1', blank=True, null=True)  # Field name made lowercase.
    accountnumber2 = models.IntegerField(db_column='AccountNumber2', blank=True, null=True)  # Field name made lowercase.
    accountnumber3 = models.IntegerField(db_column='AccountNumber3', blank=True, null=True)  # Field name made lowercase.
    accountnumber4 = models.IntegerField(db_column='AccountNumber4', blank=True, null=True)  # Field name made lowercase.
    accountnumber5 = models.IntegerField(db_column='AccountNumber5', blank=True, null=True)  # Field name made lowercase.
    accountnumber6 = models.IntegerField(db_column='AccountNumber6', blank=True, null=True)  # Field name made lowercase.
    accountnumber7 = models.IntegerField(db_column='AccountNumber7', blank=True, null=True)  # Field name made lowercase.
    accountnumber8 = models.IntegerField(db_column='AccountNumber8', blank=True, null=True)  # Field name made lowercase.
    accountnumber9 = models.IntegerField(db_column='AccountNumber9', blank=True, null=True)  # Field name made lowercase.
    accountnumber10 = models.IntegerField(db_column='AccountNumber10', blank=True, null=True)  # Field name made lowercase.
    accountnumber11 = models.IntegerField(db_column='AccountNumber11', blank=True, null=True)  # Field name made lowercase.
    accountnumber12 = models.IntegerField(db_column='AccountNumber12', blank=True, null=True)  # Field name made lowercase.
    gfscode = models.CharField(db_column='GFSCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mscoacheck = models.TextField(db_column='MSCOACheck', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nextsubaccountnumber = models.IntegerField(db_column='NextSubAccountNumber', blank=True, null=True)  # Field name made lowercase.
    field_etblglmscoaaccounts_ibranchid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_dcreateddate = models.DateTimeField(db_column='_etblGLmSCOAAccounts_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_dmodifieddate = models.DateTimeField(db_column='_etblGLmSCOAAccounts_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_icreatedbranchid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_imodifiedbranchid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_icreatedagentid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_imodifiedagentid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_ichangesetid = models.IntegerField(db_column='_etblGLmSCOAAccounts_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaaccounts_checksum = models.TextField(db_column='_etblGLmSCOAAccounts_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    imscoaverid = models.IntegerField(db_column='imSCOAVerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblGLmSCOAAccounts'


class Etblglmscoaglaccverlinks(models.Model):
    idglaccverlink = models.AutoField(db_column='idGLAccVerLink', primary_key=True)  # Field name made lowercase.
    iglaccountid = models.IntegerField(db_column='iGLAccountID')  # Field name made lowercase.
    imscoaversionid = models.IntegerField(db_column='imSCOAVersionID')  # Field name made lowercase.
    field_etblglmscoaglaccverlinks_ibranchid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_dcreateddate = models.DateTimeField(db_column='_etblGLmSCOAGLAccVerLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_dmodifieddate = models.DateTimeField(db_column='_etblGLmSCOAGLAccVerLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_icreatedbranchid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_imodifiedbranchid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_icreatedagentid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_imodifiedagentid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_ichangesetid = models.IntegerField(db_column='_etblGLmSCOAGLAccVerLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaglaccverlinks_checksum = models.TextField(db_column='_etblGLmSCOAGLAccVerLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLmSCOAGLAccVerLinks'


class Etblglmscoaversions(models.Model):
    idmscoaversion = models.AutoField(db_column='idmSCOAVersion', primary_key=True)  # Field name made lowercase.
    cversiondescription = models.CharField(db_column='cVersionDescription', max_length=50)  # Field name made lowercase.
    btransactingversion = models.BooleanField(db_column='bTransactingVersion')  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_etblglmscoaversions_ibranchid = models.IntegerField(db_column='_etblGLmSCOAVersions_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_dcreateddate = models.DateTimeField(db_column='_etblGLmSCOAVersions_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_dmodifieddate = models.DateTimeField(db_column='_etblGLmSCOAVersions_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_icreatedbranchid = models.IntegerField(db_column='_etblGLmSCOAVersions_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_imodifiedbranchid = models.IntegerField(db_column='_etblGLmSCOAVersions_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_icreatedagentid = models.IntegerField(db_column='_etblGLmSCOAVersions_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_imodifiedagentid = models.IntegerField(db_column='_etblGLmSCOAVersions_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_ichangesetid = models.IntegerField(db_column='_etblGLmSCOAVersions_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblglmscoaversions_checksum = models.TextField(db_column='_etblGLmSCOAVersions_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblGLmSCOAVersions'


class Etblgstprepayments(models.Model):
    idgstprepayments = models.AutoField(db_column='idGSTPrepayments', primary_key=True)  # Field name made lowercase.
    ipostarprepayid = models.IntegerField(db_column='iPostARPrepayID', blank=True, null=True)  # Field name made lowercase.
    ipostarinvid = models.IntegerField(db_column='iPostARInvID', blank=True, null=True)  # Field name made lowercase.
    itaxperiodid = models.IntegerField(db_column='iTaxPeriodID', blank=True, null=True)  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount', blank=True, null=True)  # Field name made lowercase.
    ftaxamount = models.FloatField(db_column='fTaxAmount', blank=True, null=True)  # Field name made lowercase.
    field_etblgstprepayments_ibranchid = models.IntegerField(db_column='_etblGSTPrepayments_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_dcreateddate = models.DateTimeField(db_column='_etblGSTPrepayments_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_dmodifieddate = models.DateTimeField(db_column='_etblGSTPrepayments_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_icreatedbranchid = models.IntegerField(db_column='_etblGSTPrepayments_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_imodifiedbranchid = models.IntegerField(db_column='_etblGSTPrepayments_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_icreatedagentid = models.IntegerField(db_column='_etblGSTPrepayments_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_imodifiedagentid = models.IntegerField(db_column='_etblGSTPrepayments_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_ichangesetid = models.IntegerField(db_column='_etblGSTPrepayments_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstprepayments_checksum = models.TextField(db_column='_etblGSTPrepayments_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iallocatedinvid = models.BigIntegerField(db_column='iAllocatedInvID')  # Field name made lowercase.
    alloctxdate = models.DateTimeField(db_column='AllocTxDate')  # Field name made lowercase.
    funallocamount = models.FloatField(db_column='fUnAllocAmount')  # Field name made lowercase.
    funalloctaxamount = models.FloatField(db_column='fUnAllocTaxAmount')  # Field name made lowercase.
    unalloctxdate = models.DateTimeField(db_column='UnallocTxDate', blank=True, null=True)  # Field name made lowercase.
    iunalloctaxperiodid = models.IntegerField(db_column='iUnallocTaxPeriodID')  # Field name made lowercase.
    famountforeign = models.FloatField(db_column='fAmountForeign')  # Field name made lowercase.
    ftaxamountforeign = models.FloatField(db_column='fTaxAmountForeign')  # Field name made lowercase.
    funallocamountforeign = models.FloatField(db_column='fUnAllocAmountForeign')  # Field name made lowercase.
    funalloctaxamountforeign = models.FloatField(db_column='fUnAllocTaxAmountForeign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblGSTPrepayments'


class Etblgstreturnprocess(models.Model):
    idgstreturnprocess = models.AutoField(db_column='idGSTReturnProcess', primary_key=True)  # Field name made lowercase.
    istatusid = models.IntegerField(db_column='iStatusID', blank=True, null=True)  # Field name made lowercase.
    itaxperiodid = models.IntegerField(db_column='iTaxPeriodID', blank=True, null=True)  # Field name made lowercase.
    icreateduserid = models.IntegerField(db_column='iCreatedUserID', blank=True, null=True)  # Field name made lowercase.
    ifinalizeduserid = models.IntegerField(db_column='iFinalizedUserID', blank=True, null=True)  # Field name made lowercase.
    iversion = models.IntegerField(db_column='iVersion', blank=True, null=True)  # Field name made lowercase.
    ngstreturndoc = models.BinaryField(db_column='nGSTReturnDoc', blank=True, null=True)  # Field name made lowercase.
    field_etblgstreturnprocess_ibranchid = models.IntegerField(db_column='_etblGSTReturnProcess_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_dcreateddate = models.DateTimeField(db_column='_etblGSTReturnProcess_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_dmodifieddate = models.DateTimeField(db_column='_etblGSTReturnProcess_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_icreatedbranchid = models.IntegerField(db_column='_etblGSTReturnProcess_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_imodifiedbranchid = models.IntegerField(db_column='_etblGSTReturnProcess_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_icreatedagentid = models.IntegerField(db_column='_etblGSTReturnProcess_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_imodifiedagentid = models.IntegerField(db_column='_etblGSTReturnProcess_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_ichangesetid = models.IntegerField(db_column='_etblGSTReturnProcess_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblgstreturnprocess_checksum = models.TextField(db_column='_etblGSTReturnProcess_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    cauthorisedname = models.CharField(db_column='cAuthorisedName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnationality = models.CharField(db_column='cNationality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnewidcard = models.CharField(db_column='cNewIDCard', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coldidcard = models.CharField(db_column='cOldIDCard', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpassport = models.CharField(db_column='cPassport', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddate = models.DateTimeField(db_column='dDate', blank=True, null=True)  # Field name made lowercase.
    bcarryforwardrefund = models.BooleanField(db_column='bCarryForwardRefund')  # Field name made lowercase.
    bmalaysian = models.BooleanField(db_column='bMalaysian')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblGSTReturnProcess'


class Etblimportdeclitems(models.Model):
    idimportdeclitems = models.AutoField(db_column='idImportDeclItems', primary_key=True)  # Field name made lowercase.
    cimportdeclname = models.CharField(db_column='cImportDeclName', max_length=50)  # Field name made lowercase.
    field_etblimportdeclitems_ibranchid = models.IntegerField(db_column='_etblImportDeclItems_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_dcreateddate = models.DateTimeField(db_column='_etblImportDeclItems_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_dmodifieddate = models.DateTimeField(db_column='_etblImportDeclItems_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_icreatedbranchid = models.IntegerField(db_column='_etblImportDeclItems_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_imodifiedbranchid = models.IntegerField(db_column='_etblImportDeclItems_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_icreatedagentid = models.IntegerField(db_column='_etblImportDeclItems_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_imodifiedagentid = models.IntegerField(db_column='_etblImportDeclItems_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_ichangesetid = models.IntegerField(db_column='_etblImportDeclItems_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitems_checksum = models.TextField(db_column='_etblImportDeclItems_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblImportDeclItems'


class Etblimportdeclitemsgllink(models.Model):
    idimportdeclitemsgllink = models.AutoField(db_column='idImportDeclItemsGLLink', primary_key=True)  # Field name made lowercase.
    iimportdeclitemid = models.IntegerField(db_column='iImportDeclItemID')  # Field name made lowercase.
    iaccountlinkid = models.IntegerField(db_column='iAccountLinkID')  # Field name made lowercase.
    field_etblimportdeclitemsgllink_ibranchid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_dcreateddate = models.DateTimeField(db_column='_etblImportDeclItemsGLLink_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_dmodifieddate = models.DateTimeField(db_column='_etblImportDeclItemsGLLink_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_icreatedbranchid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_imodifiedbranchid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_icreatedagentid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_imodifiedagentid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_ichangesetid = models.IntegerField(db_column='_etblImportDeclItemsGLLink_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclitemsgllink_checksum = models.TextField(db_column='_etblImportDeclItemsGLLink_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblImportDeclItemsGLLink'


class Etblimportdeclaration(models.Model):
    idimportdeclaration = models.AutoField(db_column='idImportDeclaration', primary_key=True)  # Field name made lowercase.
    cimportdeclarationno = models.CharField(db_column='cImportDeclarationNo', max_length=50)  # Field name made lowercase.
    cimportdeclarationshipno = models.CharField(db_column='cImportDeclarationShipNo', max_length=50)  # Field name made lowercase.
    dimpdate = models.DateTimeField(db_column='dImpDate', blank=True, null=True)  # Field name made lowercase.
    ivendorid = models.IntegerField(db_column='iVendorID')  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    cpurchdescr = models.CharField(db_column='cPurchDescr', max_length=100)  # Field name made lowercase.
    cinvlist = models.TextField(db_column='cInvList')  # Field name made lowercase. This field type is a guess.
    ftotalamount = models.FloatField(db_column='fTotalAmount')  # Field name made lowercase.
    fforeigntotalamount = models.FloatField(db_column='fForeignTotalAmount')  # Field name made lowercase.
    fexrate = models.FloatField(db_column='fExRate')  # Field name made lowercase.
    fgstamount = models.FloatField(db_column='fGSTAmount')  # Field name made lowercase.
    itaxcodeid = models.IntegerField(db_column='iTaxCodeID')  # Field name made lowercase.
    itaxrate = models.FloatField(db_column='iTaxRate')  # Field name made lowercase.
    ftaxamount = models.FloatField(db_column='fTaxAmount')  # Field name made lowercase.
    idocstatus = models.IntegerField(db_column='iDocStatus')  # Field name made lowercase.
    field_etblimportdeclaration_ibranchid = models.IntegerField(db_column='_etblImportDeclaration_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_dcreateddate = models.DateTimeField(db_column='_etblImportDeclaration_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_dmodifieddate = models.DateTimeField(db_column='_etblImportDeclaration_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_icreatedbranchid = models.IntegerField(db_column='_etblImportDeclaration_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_imodifiedbranchid = models.IntegerField(db_column='_etblImportDeclaration_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_icreatedagentid = models.IntegerField(db_column='_etblImportDeclaration_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_imodifiedagentid = models.IntegerField(db_column='_etblImportDeclaration_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_ichangesetid = models.IntegerField(db_column='_etblImportDeclaration_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclaration_checksum = models.TextField(db_column='_etblImportDeclaration_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    cauditnumber = models.CharField(db_column='cAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iforagentid = models.IntegerField(db_column='iForAgentID')  # Field name made lowercase.
    creversalreason = models.CharField(db_column='cReversalReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dreversaldate = models.DateTimeField(db_column='dReversalDate', blank=True, null=True)  # Field name made lowercase.
    creversalauditnumber = models.CharField(db_column='cReversalAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iinvnumid = models.BigIntegerField(db_column='iInvNumID')  # Field name made lowercase.
    itaxperiodid = models.IntegerField(db_column='iTaxPeriodID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblImportDeclaration'


class Etblimportdeclarationline(models.Model):
    idimportdeclarationline = models.AutoField(db_column='idImportDeclarationLine', primary_key=True)  # Field name made lowercase.
    iimportdeclarationid = models.IntegerField(db_column='iImportDeclarationID')  # Field name made lowercase.
    iimportdeclitemid = models.IntegerField(db_column='iImportDeclItemID')  # Field name made lowercase.
    ftotalamount = models.FloatField(db_column='fTotalAmount', blank=True, null=True)  # Field name made lowercase.
    fforeigntotalamount = models.FloatField(db_column='fForeignTotalAmount', blank=True, null=True)  # Field name made lowercase.
    fexrate = models.FloatField(db_column='fExRate', blank=True, null=True)  # Field name made lowercase.
    ccostitemdesc = models.CharField(db_column='cCostItemDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cremarks = models.CharField(db_column='cRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblimportdeclarationline_ibranchid = models.IntegerField(db_column='_etblImportDeclarationLine_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_dcreateddate = models.DateTimeField(db_column='_etblImportDeclarationLine_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_dmodifieddate = models.DateTimeField(db_column='_etblImportDeclarationLine_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_icreatedbranchid = models.IntegerField(db_column='_etblImportDeclarationLine_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_imodifiedbranchid = models.IntegerField(db_column='_etblImportDeclarationLine_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_icreatedagentid = models.IntegerField(db_column='_etblImportDeclarationLine_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_imodifiedagentid = models.IntegerField(db_column='_etblImportDeclarationLine_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_ichangesetid = models.IntegerField(db_column='_etblImportDeclarationLine_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblimportdeclarationline_checksum = models.TextField(db_column='_etblImportDeclarationLine_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iaccountlinkid = models.IntegerField(db_column='iAccountLinkID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblImportDeclarationLine'


class Etblincidentsourcedoclinks(models.Model):
    idincidentsourcedoclinks = models.AutoField(db_column='idIncidentSourceDocLinks', primary_key=True)  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    isourcedocid = models.BigIntegerField(db_column='iSourceDocID', blank=True, null=True)  # Field name made lowercase.
    field_etblincidentsourcedoclinks_ibranchid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_dcreateddate = models.DateTimeField(db_column='_etblIncidentSourceDocLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_dmodifieddate = models.DateTimeField(db_column='_etblIncidentSourceDocLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_icreatedbranchid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_imodifiedbranchid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_icreatedagentid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_imodifiedagentid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_ichangesetid = models.IntegerField(db_column='_etblIncidentSourceDocLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblincidentsourcedoclinks_checksum = models.TextField(db_column='_etblIncidentSourceDocLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblIncidentSourceDocLinks'


class Etblinstructiontypes(models.Model):
    iinstructiontypeid = models.AutoField(db_column='iInstructionTypeID', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ceftsoutvalue = models.CharField(db_column='cEFTSOutValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinstructiontypes_ibranchid = models.IntegerField(db_column='_etblInstructionTypes_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_dcreateddate = models.DateTimeField(db_column='_etblInstructionTypes_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_dmodifieddate = models.DateTimeField(db_column='_etblInstructionTypes_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_icreatedbranchid = models.IntegerField(db_column='_etblInstructionTypes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_imodifiedbranchid = models.IntegerField(db_column='_etblInstructionTypes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_icreatedagentid = models.IntegerField(db_column='_etblInstructionTypes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_imodifiedagentid = models.IntegerField(db_column='_etblInstructionTypes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_ichangesetid = models.IntegerField(db_column='_etblInstructionTypes_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinstructiontypes_checksum = models.TextField(db_column='_etblInstructionTypes_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInstructionTypes'


class Etblinvcosttracking(models.Model):
    idcosttracking = models.BigAutoField(db_column='idCostTracking', primary_key=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID')  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID')  # Field name made lowercase.
    iautoidx = models.BigIntegerField(db_column='iAutoIdx')  # Field name made lowercase.
    dtxdate = models.DateTimeField(db_column='dTxDate')  # Field name made lowercase.
    ddatestamp = models.DateTimeField(db_column='dDateStamp')  # Field name made lowercase.
    faveragecost = models.FloatField(db_column='fAverageCost')  # Field name made lowercase.
    flatestcost = models.FloatField(db_column='fLatestCost')  # Field name made lowercase.
    flowestcost = models.FloatField(db_column='fLowestCost')  # Field name made lowercase.
    fhighestcost = models.FloatField(db_column='fHighestCost')  # Field name made lowercase.
    fmanualcost = models.FloatField(db_column='fManualCost')  # Field name made lowercase.
    fqtyonhand = models.FloatField(db_column='fQtyOnHand')  # Field name made lowercase.
    fjobqty = models.FloatField(db_column='fJobQty')  # Field name made lowercase.
    fmfpqty = models.FloatField(db_column='fMFPQty')  # Field name made lowercase.
    field_etblinvcosttracking_ibranchid = models.IntegerField(db_column='_etblInvCostTracking_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_dcreateddate = models.DateTimeField(db_column='_etblInvCostTracking_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_dmodifieddate = models.DateTimeField(db_column='_etblInvCostTracking_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_icreatedbranchid = models.IntegerField(db_column='_etblInvCostTracking_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_imodifiedbranchid = models.IntegerField(db_column='_etblInvCostTracking_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_icreatedagentid = models.IntegerField(db_column='_etblInvCostTracking_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_imodifiedagentid = models.IntegerField(db_column='_etblInvCostTracking_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_ichangesetid = models.IntegerField(db_column='_etblInvCostTracking_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvcosttracking_checksum = models.TextField(db_column='_etblInvCostTracking_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvCostTracking'


class Etblinvimages(models.Model):
    idinvimage = models.AutoField(db_column='idInvImage', primary_key=True)  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink')  # Field name made lowercase.
    ninvimage = models.BinaryField(db_column='nInvImage', blank=True, null=True)  # Field name made lowercase.
    cinvimagetype = models.CharField(db_column='cInvImageType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cinvimagedesc = models.CharField(db_column='cInvImageDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bdisplayproportion = models.BooleanField(db_column='bDisplayProportion', blank=True, null=True)  # Field name made lowercase.
    bdisplaystretch = models.BooleanField(db_column='bDisplayStretch', blank=True, null=True)  # Field name made lowercase.
    iwidth = models.IntegerField(db_column='iWidth', blank=True, null=True)  # Field name made lowercase.
    iheight = models.IntegerField(db_column='iHeight', blank=True, null=True)  # Field name made lowercase.
    cactualtype = models.CharField(db_column='cActualType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flongtitude = models.FloatField(db_column='fLongtitude', blank=True, null=True)  # Field name made lowercase.
    flatitude = models.FloatField(db_column='fLatitude', blank=True, null=True)  # Field name made lowercase.
    fsize = models.FloatField(db_column='fSize', blank=True, null=True)  # Field name made lowercase.
    ctitle = models.CharField(db_column='cTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinvimages_ibranchid = models.IntegerField(db_column='_etblInvImages_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_dcreateddate = models.DateTimeField(db_column='_etblInvImages_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_dmodifieddate = models.DateTimeField(db_column='_etblInvImages_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_icreatedbranchid = models.IntegerField(db_column='_etblInvImages_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_imodifiedbranchid = models.IntegerField(db_column='_etblInvImages_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_icreatedagentid = models.IntegerField(db_column='_etblInvImages_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_imodifiedagentid = models.IntegerField(db_column='_etblInvImages_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_ichangesetid = models.IntegerField(db_column='_etblInvImages_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvimages_checksum = models.TextField(db_column='_etblInvImages_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvImages'


class Etblinvjrbatchlinedetails(models.Model):
    idinvjrbatchlinedetails = models.BigAutoField(db_column='idInvJrBatchLineDetails', primary_key=True)  # Field name made lowercase.
    iinvjrldbatchid = models.BigIntegerField(db_column='iInvJrLDBatchID')  # Field name made lowercase.
    iinvjrldbatchlineid = models.BigIntegerField(db_column='iInvJrLDBatchLineID')  # Field name made lowercase.
    isngroupid = models.IntegerField(db_column='iSNGroupID')  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID')  # Field name made lowercase.
    clotnumber = models.CharField(db_column='cLotNumber', max_length=40)  # Field name made lowercase.
    dlotexpirydate = models.DateTimeField(db_column='dLotExpiryDate', blank=True, null=True)  # Field name made lowercase.
    istockbinlocationid = models.IntegerField(db_column='iStockBinLocationID')  # Field name made lowercase.
    iunitsofmeasureid = models.IntegerField(db_column='iUnitsOfMeasureID')  # Field name made lowercase.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fquantity = models.FloatField(db_column='fQuantity')  # Field name made lowercase.
    field_etblinvjrbatchlinedetails_ibranchid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_dcreateddate = models.DateTimeField(db_column='_etblInvJrBatchLineDetails_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_dmodifieddate = models.DateTimeField(db_column='_etblInvJrBatchLineDetails_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_icreatedbranchid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_imodifiedbranchid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_icreatedagentid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_imodifiedagentid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_ichangesetid = models.IntegerField(db_column='_etblInvJrBatchLineDetails_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinedetails_checksum = models.TextField(db_column='_etblInvJrBatchLineDetails_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvJrBatchLineDetails'


class Etblinvjrbatchlinesn(models.Model):
    idinvjrbatchlinesn = models.AutoField(db_column='IDInvJrBatchLineSN')  # Field name made lowercase.
    iinvjrbatchid = models.IntegerField(db_column='iInvJrBatchID', blank=True, null=True)  # Field name made lowercase.
    isngroupid = models.IntegerField(db_column='iSNGroupID', blank=True, null=True)  # Field name made lowercase.
    iserialmfid = models.IntegerField(db_column='iSerialMFID', blank=True, null=True)  # Field name made lowercase.
    cserialnumber = models.CharField(db_column='cSerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinvjrbatchlinesn_ibranchid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_dcreateddate = models.DateTimeField(db_column='_etblInvJrBatchLineSN_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_dmodifieddate = models.DateTimeField(db_column='_etblInvJrBatchLineSN_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_icreatedbranchid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_imodifiedbranchid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_icreatedagentid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_imodifiedagentid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_ichangesetid = models.IntegerField(db_column='_etblInvJrBatchLineSN_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlinesn_checksum = models.TextField(db_column='_etblInvJrBatchLineSN_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvJrBatchLineSN'


class Etblinvjrbatchlines(models.Model):
    idinvjrbatchlines = models.AutoField(db_column='idInvJrBatchLines', primary_key=True)  # Field name made lowercase.
    iinvjrbatchid = models.IntegerField(db_column='iInvJrBatchID')  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID')  # Field name made lowercase.
    dtrdate = models.DateTimeField(db_column='dTrDate')  # Field name made lowercase.
    itrcodeid = models.IntegerField(db_column='iTrCodeID')  # Field name made lowercase.
    iglcontraid = models.IntegerField(db_column='iGLContraID')  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fqtyin = models.FloatField(db_column='fQtyIn', blank=True, null=True)  # Field name made lowercase.
    fqtyout = models.FloatField(db_column='fQtyOut', blank=True, null=True)  # Field name made lowercase.
    fnewcost = models.FloatField(db_column='fNewCost', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem')  # Field name made lowercase.
    bislotitem = models.BooleanField(db_column='bIsLotItem')  # Field name made lowercase.
    ijobid = models.IntegerField(db_column='iJobID')  # Field name made lowercase.
    clinenotes = models.CharField(db_column='cLineNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurestockingid = models.IntegerField(db_column='iUnitsOfMeasureStockingID', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurecategoryid = models.IntegerField(db_column='iUnitsOfMeasureCategoryID', blank=True, null=True)  # Field name made lowercase.
    field_etblinvjrbatchlines_ibranchid = models.IntegerField(db_column='_etblInvJrBatchLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_dcreateddate = models.DateTimeField(db_column='_etblInvJrBatchLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_dmodifieddate = models.DateTimeField(db_column='_etblInvJrBatchLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_icreatedbranchid = models.IntegerField(db_column='_etblInvJrBatchLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_imodifiedbranchid = models.IntegerField(db_column='_etblInvJrBatchLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_icreatedagentid = models.IntegerField(db_column='_etblInvJrBatchLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_imodifiedagentid = models.IntegerField(db_column='_etblInvJrBatchLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_ichangesetid = models.IntegerField(db_column='_etblInvJrBatchLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatchlines_checksum = models.TextField(db_column='_etblInvJrBatchLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    bmatrixentry = models.BooleanField(db_column='bMatrixEntry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblInvJrBatchLines'
        unique_together = (('idinvjrbatchlines', 'iinvjrbatchid'),)


class Etblinvjrbatches(models.Model):
    idinvjrbatches = models.AutoField(db_column='IDInvJrBatches', primary_key=True)  # Field name made lowercase.
    cinvjrnumber = models.CharField(db_column='cInvJrNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cinvjrdescription = models.CharField(db_column='cInvJrDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cinvjrreference = models.CharField(db_column='cInvJrReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icreateagentid = models.IntegerField(db_column='iCreateAgentID')  # Field name made lowercase.
    bclearafterpost = models.BooleanField(db_column='bClearAfterPost')  # Field name made lowercase.
    ballowdupref = models.BooleanField(db_column='bAllowDupRef')  # Field name made lowercase.
    balloweditglcontra = models.BooleanField(db_column='bAllowEditGLContra')  # Field name made lowercase.
    inewlinedateopt = models.IntegerField(db_column='iNewLineDateOpt', blank=True, null=True)  # Field name made lowercase.
    dnewlinedatedef = models.DateTimeField(db_column='dNewLineDateDef', blank=True, null=True)  # Field name made lowercase.
    inewlinerefopt = models.IntegerField(db_column='iNewLineRefOpt', blank=True, null=True)  # Field name made lowercase.
    cnewlinerefdef = models.CharField(db_column='cNewLineRefDef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bnewlinerefinc = models.BooleanField(db_column='bNewLineRefInc')  # Field name made lowercase.
    inewlinedescopt = models.IntegerField(db_column='iNewLineDescOpt', blank=True, null=True)  # Field name made lowercase.
    cnewlinedescdef = models.CharField(db_column='cNewLineDescDef', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bnewlinedescinc = models.BooleanField(db_column='bNewLineDescInc')  # Field name made lowercase.
    inewlineprojectopt = models.IntegerField(db_column='iNewLineProjectOpt', blank=True, null=True)  # Field name made lowercase.
    inewlineprojectdefid = models.IntegerField(db_column='iNewLineProjectDefID')  # Field name made lowercase.
    inewlinewarehouseopt = models.IntegerField(db_column='iNewLineWarehouseOpt', blank=True, null=True)  # Field name made lowercase.
    inewlinewarehousedefid = models.IntegerField(db_column='iNewLineWarehouseDefID')  # Field name made lowercase.
    bjustcleared = models.BooleanField(db_column='bJustCleared')  # Field name made lowercase.
    itransactioncode = models.IntegerField(db_column='iTransactionCode', blank=True, null=True)  # Field name made lowercase.
    field_etblinvjrbatches_ibranchid = models.IntegerField(db_column='_etblInvJrBatches_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_dcreateddate = models.DateTimeField(db_column='_etblInvJrBatches_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_dmodifieddate = models.DateTimeField(db_column='_etblInvJrBatches_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_icreatedbranchid = models.IntegerField(db_column='_etblInvJrBatches_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_imodifiedbranchid = models.IntegerField(db_column='_etblInvJrBatches_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_icreatedagentid = models.IntegerField(db_column='_etblInvJrBatches_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_imodifiedagentid = models.IntegerField(db_column='_etblInvJrBatches_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_ichangesetid = models.IntegerField(db_column='_etblInvJrBatches_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvjrbatches_checksum = models.TextField(db_column='_etblInvJrBatches_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvJrBatches'


class Etblinvpriceupdatebatchlines(models.Model):
    idinvpriceupdatebatchlines = models.AutoField(db_column='idInvPriceUpdateBatchLines', primary_key=True)  # Field name made lowercase.
    iinvpriceupdatebatchid = models.IntegerField(db_column='iInvPriceUpdateBatchID')  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID')  # Field name made lowercase.
    ipricelistid = models.IntegerField(db_column='iPriceListID')  # Field name made lowercase.
    fexclprice = models.FloatField(db_column='fExclPrice', blank=True, null=True)  # Field name made lowercase.
    finclprice = models.FloatField(db_column='fInclPrice', blank=True, null=True)  # Field name made lowercase.
    icostmethod = models.IntegerField(db_column='iCostMethod', blank=True, null=True)  # Field name made lowercase.
    funitcost = models.FloatField(db_column='fUnitCost', blank=True, null=True)  # Field name made lowercase.
    fgrossmargin = models.FloatField(db_column='fGrossMargin', blank=True, null=True)  # Field name made lowercase.
    fgmpercentage = models.FloatField(db_column='fGMPercentage', blank=True, null=True)  # Field name made lowercase.
    iupdatetype = models.IntegerField(db_column='iUpdateType', blank=True, null=True)  # Field name made lowercase.
    iupdateaction = models.IntegerField(db_column='iUpdateAction', blank=True, null=True)  # Field name made lowercase.
    fpercentagechange = models.FloatField(db_column='fPercentageChange', blank=True, null=True)  # Field name made lowercase.
    irounding = models.IntegerField(db_column='iRounding', blank=True, null=True)  # Field name made lowercase.
    itonearest = models.IntegerField(db_column='iToNearest', blank=True, null=True)  # Field name made lowercase.
    fupdateprice = models.FloatField(db_column='fUpdatePrice', blank=True, null=True)  # Field name made lowercase.
    fnewexclprice = models.FloatField(db_column='fNewExclPrice', blank=True, null=True)  # Field name made lowercase.
    fnewinclprice = models.FloatField(db_column='fNewInclPrice', blank=True, null=True)  # Field name made lowercase.
    fnewgrossmargin = models.FloatField(db_column='fNewGrossMargin', blank=True, null=True)  # Field name made lowercase.
    fnewgmpercentage = models.FloatField(db_column='fNewGMPercentage', blank=True, null=True)  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_etblinvpriceupdatebatchlines_ibranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_dcreateddate = models.DateTimeField(db_column='_etblInvPriceUpdateBatchLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_dmodifieddate = models.DateTimeField(db_column='_etblInvPriceUpdateBatchLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_icreatedbranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_imodifiedbranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_icreatedagentid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_imodifiedagentid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_ichangesetid = models.IntegerField(db_column='_etblInvPriceUpdateBatchLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatchlines_checksum = models.TextField(db_column='_etblInvPriceUpdateBatchLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvPriceUpdateBatchLines'


class Etblinvpriceupdatebatches(models.Model):
    idinvpriceupdatebatches = models.AutoField(db_column='idInvPriceUpdateBatches', primary_key=True)  # Field name made lowercase.
    cinvpriceupdatenumber = models.CharField(db_column='cInvPriceUpdateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cinvpriceupdatedescription = models.CharField(db_column='cInvPriceUpdateDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cinvpriceupdatereference = models.CharField(db_column='cInvPriceUpdateReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstartcode = models.CharField(db_column='cStartCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cendcode = models.CharField(db_column='cEndCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cgroups = models.CharField(db_column='cGroups', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cwarehouses = models.CharField(db_column='cWarehouses', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    bupdateallwarehouses = models.BooleanField(db_column='bUpdateAllWarehouses')  # Field name made lowercase.
    bsaleswarehouses = models.BooleanField(db_column='bSalesWarehouses')  # Field name made lowercase.
    bignoreinactive = models.BooleanField(db_column='bIgnoreInactive')  # Field name made lowercase.
    cpricelists = models.CharField(db_column='cPriceLists', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    iupdatetype = models.IntegerField(db_column='iUpdateType', blank=True, null=True)  # Field name made lowercase.
    iupdateaction = models.IntegerField(db_column='iUpdateAction', blank=True, null=True)  # Field name made lowercase.
    irounding = models.IntegerField(db_column='iRounding', blank=True, null=True)  # Field name made lowercase.
    itonearest = models.IntegerField(db_column='iToNearest', blank=True, null=True)  # Field name made lowercase.
    bposted = models.BooleanField(db_column='bPosted')  # Field name made lowercase.
    cattributegroups = models.TextField(db_column='cAttributeGroups', blank=True, null=True)  # Field name made lowercase.
    cattributetypes = models.TextField(db_column='cAttributeTypes', blank=True, null=True)  # Field name made lowercase.
    xattributefiltervalues = models.TextField(db_column='xAttributeFilterValues', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bonlyglobalprices = models.BooleanField(db_column='bOnlyGlobalPrices')  # Field name made lowercase.
    bonlyexistingprices = models.BooleanField(db_column='bOnlyExistingPrices')  # Field name made lowercase.
    bbatchscheduling = models.BooleanField(db_column='bBatchScheduling')  # Field name made lowercase.
    bbatchvalidated = models.BooleanField(db_column='bBatchValidated')  # Field name made lowercase.
    bcreatepubfromimport = models.BooleanField(db_column='bCreatePUBFromImport')  # Field name made lowercase.
    field_etblinvpriceupdatebatches_ibranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_dcreateddate = models.DateTimeField(db_column='_etblInvPriceUpdateBatches_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_dmodifieddate = models.DateTimeField(db_column='_etblInvPriceUpdateBatches_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_icreatedbranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_imodifiedbranchid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_icreatedagentid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_imodifiedagentid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_ichangesetid = models.IntegerField(db_column='_etblInvPriceUpdateBatches_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvpriceupdatebatches_checksum = models.TextField(db_column='_etblInvPriceUpdateBatches_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvPriceUpdateBatches'


class Etblinvseggroup(models.Model):
    idinvseggroup = models.AutoField(db_column='idInvSegGroup', primary_key=True)  # Field name made lowercase.
    iinvsegtypeid = models.IntegerField(db_column='iInvSegTypeID')  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinvseggroup_ibranchid = models.IntegerField(db_column='_etblInvSegGroup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_dcreateddate = models.DateTimeField(db_column='_etblInvSegGroup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_dmodifieddate = models.DateTimeField(db_column='_etblInvSegGroup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_icreatedbranchid = models.IntegerField(db_column='_etblInvSegGroup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_imodifiedbranchid = models.IntegerField(db_column='_etblInvSegGroup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_icreatedagentid = models.IntegerField(db_column='_etblInvSegGroup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_imodifiedagentid = models.IntegerField(db_column='_etblInvSegGroup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_ichangesetid = models.IntegerField(db_column='_etblInvSegGroup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvseggroup_checksum = models.TextField(db_column='_etblInvSegGroup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvSegGroup'


class Etblinvsegtype(models.Model):
    idinvsegtype = models.AutoField(db_column='idInvSegType', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinvsegtype_ibranchid = models.IntegerField(db_column='_etblInvSegType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_dcreateddate = models.DateTimeField(db_column='_etblInvSegType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_dmodifieddate = models.DateTimeField(db_column='_etblInvSegType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_icreatedbranchid = models.IntegerField(db_column='_etblInvSegType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_imodifiedbranchid = models.IntegerField(db_column='_etblInvSegType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_icreatedagentid = models.IntegerField(db_column='_etblInvSegType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_imodifiedagentid = models.IntegerField(db_column='_etblInvSegType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_ichangesetid = models.IntegerField(db_column='_etblInvSegType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegtype_checksum = models.TextField(db_column='_etblInvSegType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvSegType'


class Etblinvsegvalue(models.Model):
    idinvsegvalue = models.AutoField(db_column='idInvSegValue', primary_key=True)  # Field name made lowercase.
    iinvseggroupid = models.IntegerField(db_column='iInvSegGroupID')  # Field name made lowercase.
    cvalue = models.CharField(db_column='cValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblinvsegvalue_ibranchid = models.IntegerField(db_column='_etblInvSegValue_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_dcreateddate = models.DateTimeField(db_column='_etblInvSegValue_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_dmodifieddate = models.DateTimeField(db_column='_etblInvSegValue_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_icreatedbranchid = models.IntegerField(db_column='_etblInvSegValue_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_imodifiedbranchid = models.IntegerField(db_column='_etblInvSegValue_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_icreatedagentid = models.IntegerField(db_column='_etblInvSegValue_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_imodifiedagentid = models.IntegerField(db_column='_etblInvSegValue_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_ichangesetid = models.IntegerField(db_column='_etblInvSegValue_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvsegvalue_checksum = models.TextField(db_column='_etblInvSegValue_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvSegValue'


class Etblinvoicedeposits(models.Model):
    idinvoicedeposits = models.AutoField(db_column='idInvoiceDeposits', primary_key=True)  # Field name made lowercase.
    iinvoiceid = models.BigIntegerField(db_column='iInvoiceID', blank=True, null=True)  # Field name made lowercase.
    fdepositamount = models.FloatField(db_column='fDepositAmount', blank=True, null=True)  # Field name made lowercase.
    funallocatedamount = models.FloatField(db_column='fUnallocatedAmount', blank=True, null=True)  # Field name made lowercase.
    ipostarid = models.BigIntegerField(db_column='iPostARID', blank=True, null=True)  # Field name made lowercase.
    iinvoiceidorig = models.BigIntegerField(db_column='iInvoiceIDOrig', blank=True, null=True)  # Field name made lowercase.
    field_etblinvoicedeposits_ibranchid = models.IntegerField(db_column='_etblInvoiceDeposits_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_dcreateddate = models.DateTimeField(db_column='_etblInvoiceDeposits_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_dmodifieddate = models.DateTimeField(db_column='_etblInvoiceDeposits_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_icreatedbranchid = models.IntegerField(db_column='_etblInvoiceDeposits_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_imodifiedbranchid = models.IntegerField(db_column='_etblInvoiceDeposits_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_icreatedagentid = models.IntegerField(db_column='_etblInvoiceDeposits_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_imodifiedagentid = models.IntegerField(db_column='_etblInvoiceDeposits_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_ichangesetid = models.IntegerField(db_column='_etblInvoiceDeposits_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblinvoicedeposits_checksum = models.TextField(db_column='_etblInvoiceDeposits_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblInvoiceDeposits'


class Etbllotstatus(models.Model):
    idlotstatus = models.AutoField(db_column='idLotStatus', primary_key=True)  # Field name made lowercase.
    clotstatusdescription = models.CharField(db_column='cLotStatusDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ballowpurchases = models.BooleanField(db_column='bAllowPurchases')  # Field name made lowercase.
    ballowsales = models.BooleanField(db_column='bAllowSales')  # Field name made lowercase.
    field_etbllotstatus_ibranchid = models.IntegerField(db_column='_etblLotStatus_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_dcreateddate = models.DateTimeField(db_column='_etblLotStatus_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_dmodifieddate = models.DateTimeField(db_column='_etblLotStatus_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_icreatedbranchid = models.IntegerField(db_column='_etblLotStatus_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_imodifiedbranchid = models.IntegerField(db_column='_etblLotStatus_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_icreatedagentid = models.IntegerField(db_column='_etblLotStatus_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_imodifiedagentid = models.IntegerField(db_column='_etblLotStatus_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_ichangesetid = models.IntegerField(db_column='_etblLotStatus_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllotstatus_checksum = models.TextField(db_column='_etblLotStatus_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblLotStatus'


class Etbllottracking(models.Model):
    idlottracking = models.AutoField(db_column='idLotTracking', primary_key=True)  # Field name made lowercase.
    clotdescription = models.CharField(db_column='cLotDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    ilotstatusid = models.IntegerField(db_column='iLotStatusID', blank=True, null=True)  # Field name made lowercase.
    dexpirydate = models.DateTimeField(db_column='dExpiryDate', blank=True, null=True)  # Field name made lowercase.
    bisactive = models.BooleanField(db_column='bIsActive')  # Field name made lowercase.
    dlastgrvdate = models.DateTimeField(db_column='dLastGRVDate', blank=True, null=True)  # Field name made lowercase.
    field_etbllottracking_ibranchid = models.IntegerField(db_column='_etblLotTracking_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_dcreateddate = models.DateTimeField(db_column='_etblLotTracking_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_dmodifieddate = models.DateTimeField(db_column='_etblLotTracking_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_icreatedbranchid = models.IntegerField(db_column='_etblLotTracking_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_imodifiedbranchid = models.IntegerField(db_column='_etblLotTracking_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_icreatedagentid = models.IntegerField(db_column='_etblLotTracking_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_imodifiedagentid = models.IntegerField(db_column='_etblLotTracking_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_ichangesetid = models.IntegerField(db_column='_etblLotTracking_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottracking_checksum = models.TextField(db_column='_etblLotTracking_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblLotTracking'


class Etbllottrackingqty(models.Model):
    idlottrackingqty = models.AutoField(db_column='idLotTrackingQty', primary_key=True)  # Field name made lowercase.
    ilottrackingid = models.IntegerField(db_column='iLotTrackingID', blank=True, null=True)  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    fqtyonhand = models.FloatField(db_column='fQtyOnHand', blank=True, null=True)  # Field name made lowercase.
    fqtypurchased = models.FloatField(db_column='fQtyPurchased', blank=True, null=True)  # Field name made lowercase.
    fqtysold = models.FloatField(db_column='fQtySold', blank=True, null=True)  # Field name made lowercase.
    fqtyadjustout = models.FloatField(db_column='fQtyAdjustOut', blank=True, null=True)  # Field name made lowercase.
    fqtyadjustin = models.FloatField(db_column='fQtyAdjustIn', blank=True, null=True)  # Field name made lowercase.
    fqtytosupplier = models.FloatField(db_column='fQtyToSupplier', blank=True, null=True)  # Field name made lowercase.
    fqtyfromclient = models.FloatField(db_column='fQtyFromClient', blank=True, null=True)  # Field name made lowercase.
    fqtyfromwarehouse = models.FloatField(db_column='fQtyFromWarehouse', blank=True, null=True)  # Field name made lowercase.
    fqtytowarehouse = models.FloatField(db_column='fQtyToWarehouse', blank=True, null=True)  # Field name made lowercase.
    fqtyreserved = models.FloatField(db_column='fQtyReserved', blank=True, null=True)  # Field name made lowercase.
    fqtyjcwip = models.FloatField(db_column='fQtyJCWIP', blank=True, null=True)  # Field name made lowercase.
    fqtymfwip = models.FloatField(db_column='fQtyMFWIP', blank=True, null=True)  # Field name made lowercase.
    field_etbllottrackingqty_ibranchid = models.IntegerField(db_column='_etblLotTrackingQty_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_dcreateddate = models.DateTimeField(db_column='_etblLotTrackingQty_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_dmodifieddate = models.DateTimeField(db_column='_etblLotTrackingQty_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_icreatedbranchid = models.IntegerField(db_column='_etblLotTrackingQty_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_imodifiedbranchid = models.IntegerField(db_column='_etblLotTrackingQty_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_icreatedagentid = models.IntegerField(db_column='_etblLotTrackingQty_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_imodifiedagentid = models.IntegerField(db_column='_etblLotTrackingQty_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_ichangesetid = models.IntegerField(db_column='_etblLotTrackingQty_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingqty_checksum = models.TextField(db_column='_etblLotTrackingQty_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ibinlocationid = models.IntegerField(db_column='iBinLocationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblLotTrackingQty'


class Etbllottrackingtx(models.Model):
    idlottrackingtx = models.BigAutoField(db_column='idLotTrackingTx', primary_key=True)  # Field name made lowercase.
    ilottrackingid = models.IntegerField(db_column='iLotTrackingID', blank=True, null=True)  # Field name made lowercase.
    dlttxdate = models.DateTimeField(db_column='dLTTxDate', blank=True, null=True)  # Field name made lowercase.
    ilttxaccountid = models.IntegerField(db_column='iLTTxAccountID', blank=True, null=True)  # Field name made lowercase.
    clttxreference = models.CharField(db_column='cLTTxReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clttxreference2 = models.CharField(db_column='cLTTxReference2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ilttxtrcodeid = models.IntegerField(db_column='iLTTxTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ilttxtranstypeid = models.IntegerField(db_column='iLTTxTransTypeID', blank=True, null=True)  # Field name made lowercase.
    ilttxwarehouseid = models.IntegerField(db_column='iLTTxWarehouseID', blank=True, null=True)  # Field name made lowercase.
    clttxauditnumber = models.CharField(db_column='cLTTxAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dlttxexpirydate = models.DateTimeField(db_column='dLTTxExpiryDate', blank=True, null=True)  # Field name made lowercase.
    ilttxstatusid = models.IntegerField(db_column='iLTTxStatusID', blank=True, null=True)  # Field name made lowercase.
    flttxqty = models.FloatField(db_column='fLTTxQty', blank=True, null=True)  # Field name made lowercase.
    itxbranchid = models.IntegerField(db_column='iTxBranchID', blank=True, null=True)  # Field name made lowercase.
    field_etbllottrackingtx_ibranchid = models.IntegerField(db_column='_etblLotTrackingTx_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_dcreateddate = models.DateTimeField(db_column='_etblLotTrackingTx_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_dmodifieddate = models.DateTimeField(db_column='_etblLotTrackingTx_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_icreatedbranchid = models.IntegerField(db_column='_etblLotTrackingTx_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_imodifiedbranchid = models.IntegerField(db_column='_etblLotTrackingTx_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_icreatedagentid = models.IntegerField(db_column='_etblLotTrackingTx_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_imodifiedagentid = models.IntegerField(db_column='_etblLotTrackingTx_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_ichangesetid = models.IntegerField(db_column='_etblLotTrackingTx_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbllottrackingtx_checksum = models.TextField(db_column='_etblLotTrackingTx_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ilttxbinlocationid = models.IntegerField(db_column='iLTTxBinLocationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblLotTrackingTx'


class Etblmcagentcriteria(models.Model):
    idagentcriteria = models.AutoField(db_column='idAgentCriteria', primary_key=True)  # Field name made lowercase.
    cagentcriteriadesc = models.CharField(db_column='cAgentCriteriaDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cagent = models.CharField(db_column='cAgent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=40)  # Field name made lowercase.
    cmonitorvalue = models.CharField(db_column='cMonitorValue', max_length=100)  # Field name made lowercase.
    coperator = models.CharField(db_column='cOperator', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cresultvalue = models.CharField(db_column='cResultValue', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cownresultvalue = models.CharField(db_column='cOwnResultValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csql = models.TextField(db_column='cSQL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cfrequencydescription = models.CharField(db_column='cFrequencyDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ifrequencytimeinmin = models.IntegerField(db_column='iFrequencyTimeInMin', blank=True, null=True)  # Field name made lowercase.
    dfrequencystarttime = models.DateTimeField(db_column='dFrequencyStartTime', blank=True, null=True)  # Field name made lowercase.
    dfrequencyendtime = models.DateTimeField(db_column='dFrequencyEndTime', blank=True, null=True)  # Field name made lowercase.
    cnotificationfrequency = models.CharField(db_column='cNotificationFrequency', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bnotifytrayicon = models.BooleanField(db_column='bNotifyTrayIcon')  # Field name made lowercase.
    bnotifyemail = models.BooleanField(db_column='bNotifyEmail')  # Field name made lowercase.
    bnotifysms = models.BooleanField(db_column='bNotifySMS')  # Field name made lowercase.
    blognotification = models.BooleanField(db_column='bLogNotification')  # Field name made lowercase.
    baddtomynotifications = models.BooleanField(db_column='bAddToMyNotifications')  # Field name made lowercase.
    cemailtoaddress = models.TextField(db_column='cEmailToAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cemailfromaddress = models.CharField(db_column='cEmailFromAddress', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cemailsubject = models.CharField(db_column='cEmailSubject', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cemailmessage = models.TextField(db_column='cEmailMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csmstoaddress = models.TextField(db_column='cSMSToAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csmsmessage = models.TextField(db_column='cSMSMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ctrayiconmessage = models.TextField(db_column='cTrayIconMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cmynotificationsmessage = models.TextField(db_column='cMyNotificationsMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dlastnotificationdatetime = models.DateTimeField(db_column='dLastNotificationDateTime', blank=True, null=True)  # Field name made lowercase.
    cprocessing = models.CharField(db_column='cProcessing', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cemailcc = models.TextField(db_column='cEmailCC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cemailbcc = models.TextField(db_column='cEmailBcc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID')  # Field name made lowercase.
    field_etblmcagentcriteria_ibranchid = models.IntegerField(db_column='_etblMCAgentCriteria_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_dcreateddate = models.DateTimeField(db_column='_etblMCAgentCriteria_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_dmodifieddate = models.DateTimeField(db_column='_etblMCAgentCriteria_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_icreatedbranchid = models.IntegerField(db_column='_etblMCAgentCriteria_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_imodifiedbranchid = models.IntegerField(db_column='_etblMCAgentCriteria_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_icreatedagentid = models.IntegerField(db_column='_etblMCAgentCriteria_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_imodifiedagentid = models.IntegerField(db_column='_etblMCAgentCriteria_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_ichangesetid = models.IntegerField(db_column='_etblMCAgentCriteria_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentcriteria_checksum = models.TextField(db_column='_etblMCAgentCriteria_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblMCAgentCriteria'


class Etblmcagentnotifications(models.Model):
    idagentnotification = models.AutoField(db_column='idAgentNotification', primary_key=True)  # Field name made lowercase.
    cagent = models.CharField(db_column='cAgent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agentcriteriaid = models.IntegerField(db_column='AgentCriteriaID')  # Field name made lowercase.
    cnotificationdesc = models.CharField(db_column='cNotificationDesc', max_length=50)  # Field name made lowercase.
    cnotificationmessage = models.CharField(db_column='cNotificationMessage', max_length=1024)  # Field name made lowercase.
    dnotificationdate = models.DateTimeField(db_column='dNotificationDate')  # Field name made lowercase.
    backnowledged = models.BooleanField(db_column='bAcknowledged')  # Field name made lowercase.
    bprocessed = models.BooleanField(db_column='bProcessed')  # Field name made lowercase.
    cprocessactions = models.CharField(db_column='cProcessActions', max_length=1, blank=True, null=True)  # Field name made lowercase.
    field_etblmcagentnotifications_ibranchid = models.IntegerField(db_column='_etblMCAgentNotifications_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_dcreateddate = models.DateTimeField(db_column='_etblMCAgentNotifications_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_dmodifieddate = models.DateTimeField(db_column='_etblMCAgentNotifications_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_icreatedbranchid = models.IntegerField(db_column='_etblMCAgentNotifications_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_imodifiedbranchid = models.IntegerField(db_column='_etblMCAgentNotifications_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_icreatedagentid = models.IntegerField(db_column='_etblMCAgentNotifications_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_imodifiedagentid = models.IntegerField(db_column='_etblMCAgentNotifications_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_ichangesetid = models.IntegerField(db_column='_etblMCAgentNotifications_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcagentnotifications_checksum = models.TextField(db_column='_etblMCAgentNotifications_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblMCAgentNotifications'


class Etblmcdefaultcriteria(models.Model):
    iddefaultcriteria = models.AutoField(db_column='idDefaultCriteria', primary_key=True)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=100)  # Field name made lowercase.
    cmonitorvalue = models.CharField(db_column='cMonitorValue', max_length=200)  # Field name made lowercase.
    cmonitorfield = models.CharField(db_column='cMonitorField', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cmonitorfieldtype = models.CharField(db_column='cMonitorFieldType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    coperator = models.CharField(db_column='cOperator', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cresultvalue = models.CharField(db_column='cResultValue', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cfieldsforresult = models.CharField(db_column='cFieldsForResult', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cmessagevaluedesc = models.CharField(db_column='cMessageValueDesc', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cmessagevaluefield = models.CharField(db_column='cMessageValueField', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ccriteriasqltext = models.CharField(db_column='cCriteriaSQLText', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    field_etblmcdefaultcriteria_ibranchid = models.IntegerField(db_column='_etblMCDefaultCriteria_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_dcreateddate = models.DateTimeField(db_column='_etblMCDefaultCriteria_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_dmodifieddate = models.DateTimeField(db_column='_etblMCDefaultCriteria_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_icreatedbranchid = models.IntegerField(db_column='_etblMCDefaultCriteria_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_imodifiedbranchid = models.IntegerField(db_column='_etblMCDefaultCriteria_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_icreatedagentid = models.IntegerField(db_column='_etblMCDefaultCriteria_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_imodifiedagentid = models.IntegerField(db_column='_etblMCDefaultCriteria_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_ichangesetid = models.IntegerField(db_column='_etblMCDefaultCriteria_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmcdefaultcriteria_checksum = models.TextField(db_column='_etblMCDefaultCriteria_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblMCDefaultCriteria'


class Etblmajorindustrycodes(models.Model):
    idmajorindustrycode = models.AutoField(db_column='idMajorIndustryCode', primary_key=True)  # Field name made lowercase.
    cmajorindustrycode = models.CharField(db_column='cMajorIndustryCode', max_length=20)  # Field name made lowercase.
    cmajorindustrydescription = models.CharField(db_column='cMajorIndustryDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblmajorindustrycodes_ibranchid = models.IntegerField(db_column='_etblMajorIndustryCodes_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_dcreateddate = models.DateTimeField(db_column='_etblMajorIndustryCodes_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_dmodifieddate = models.DateTimeField(db_column='_etblMajorIndustryCodes_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_icreatedbranchid = models.IntegerField(db_column='_etblMajorIndustryCodes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_imodifiedbranchid = models.IntegerField(db_column='_etblMajorIndustryCodes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_icreatedagentid = models.IntegerField(db_column='_etblMajorIndustryCodes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_imodifiedagentid = models.IntegerField(db_column='_etblMajorIndustryCodes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_ichangesetid = models.IntegerField(db_column='_etblMajorIndustryCodes_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmajorindustrycodes_checksum = models.TextField(db_column='_etblMajorIndustryCodes_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    imajorindustrycategory = models.IntegerField(db_column='iMajorIndustryCategory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblMajorIndustryCodes'


class Etblmanufprocess(models.Model):
    idmanufprocess = models.AutoField(db_column='idManufProcess', primary_key=True)  # Field name made lowercase.
    istatus = models.CharField(db_column='iStatus', max_length=1)  # Field name made lowercase.
    cprocessrefnumber = models.CharField(db_column='cProcessRefNumber', max_length=50)  # Field name made lowercase.
    cotherrefnumber = models.CharField(db_column='cOtherRefNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ibommasterid = models.IntegerField(db_column='iBOMMasterID')  # Field name made lowercase.
    cmanufdescription = models.CharField(db_column='cManufDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dcreated = models.DateTimeField(db_column='dCreated')  # Field name made lowercase.
    dlastupdated = models.DateTimeField(db_column='dLastUpdated')  # Field name made lowercase.
    fmanufquantity = models.FloatField(db_column='fManufQuantity', blank=True, null=True)  # Field name made lowercase.
    fqtymanufactured = models.FloatField(db_column='fQtyManufactured', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.
    imanufwarehouseid = models.IntegerField(db_column='iManufWarehouseID', blank=True, null=True)  # Field name made lowercase.
    boverridecompwhse = models.BooleanField(db_column='bOverrideCompWhse')  # Field name made lowercase.
    iinvoicelineid = models.BigIntegerField(db_column='iInvoiceLineID')  # Field name made lowercase.
    bislinkedtoorder = models.BooleanField(db_column='bIsLinkedToOrder')  # Field name made lowercase.
    iinvnumid = models.BigIntegerField(db_column='iInvNumID', blank=True, null=True)  # Field name made lowercase.
    ijcmasterid = models.IntegerField(db_column='iJCMasterID', blank=True, null=True)  # Field name made lowercase.
    dprojectedcompletiondate = models.DateTimeField(db_column='dProjectedCompletionDate', blank=True, null=True)  # Field name made lowercase.
    dactualcompletiondate = models.DateTimeField(db_column='dActualCompletionDate', blank=True, null=True)  # Field name made lowercase.
    field_etblmanufprocess_fleaddays = models.FloatField(db_column='_etblManufProcess_fLeadDays', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_ibranchid = models.IntegerField(db_column='_etblManufProcess_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_dcreateddate = models.DateTimeField(db_column='_etblManufProcess_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_dmodifieddate = models.DateTimeField(db_column='_etblManufProcess_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_icreatedbranchid = models.IntegerField(db_column='_etblManufProcess_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_imodifiedbranchid = models.IntegerField(db_column='_etblManufProcess_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_icreatedagentid = models.IntegerField(db_column='_etblManufProcess_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_imodifiedagentid = models.IntegerField(db_column='_etblManufProcess_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_ichangesetid = models.IntegerField(db_column='_etblManufProcess_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocess_checksum = models.TextField(db_column='_etblManufProcess_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ibomattributegroupid = models.IntegerField(db_column='iBOMAttributeGroupID')  # Field name made lowercase.
    xbomattribute = models.TextField(db_column='xBOMAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblManufProcess'


class Etblmanufprocessitem(models.Model):
    idmanufprocessitem = models.BigAutoField(db_column='idManufProcessItem', primary_key=True)  # Field name made lowercase.
    imfpitemid = models.FloatField(db_column='iMFPItemID', blank=True, null=True)  # Field name made lowercase.
    iparentmfpitemid = models.IntegerField(db_column='iParentMFPItemID')  # Field name made lowercase.
    imanufprocessid = models.IntegerField(db_column='iManufProcessID')  # Field name made lowercase.
    iinvitemid = models.IntegerField(db_column='iInvItemID', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fproductionqty = models.FloatField(db_column='fProductionQty', blank=True, null=True)  # Field name made lowercase.
    cunitofmeasure = models.CharField(db_column='cUnitOfMeasure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    funitcost = models.FloatField(db_column='fUnitCost', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    idefaultwhseid = models.IntegerField(db_column='iDefaultWhseID', blank=True, null=True)  # Field name made lowercase.
    field_etblmanufprocessitem_ibranchid = models.IntegerField(db_column='_etblManufProcessItem_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_dcreateddate = models.DateTimeField(db_column='_etblManufProcessItem_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_dmodifieddate = models.DateTimeField(db_column='_etblManufProcessItem_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_icreatedbranchid = models.IntegerField(db_column='_etblManufProcessItem_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_imodifiedbranchid = models.IntegerField(db_column='_etblManufProcessItem_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_icreatedagentid = models.IntegerField(db_column='_etblManufProcessItem_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_imodifiedagentid = models.IntegerField(db_column='_etblManufProcessItem_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_ichangesetid = models.IntegerField(db_column='_etblManufProcessItem_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessitem_checksum = models.TextField(db_column='_etblManufProcessItem_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    idefaultstockbinid = models.IntegerField(db_column='iDefaultStockBinID', blank=True, null=True)  # Field name made lowercase.
    xdefaultattribute = models.TextField(db_column='xDefaultAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblManufProcessItem'


class Etblmanufprocessline(models.Model):
    idmanufprocessline = models.BigAutoField(db_column='idManufProcessLine', primary_key=True)  # Field name made lowercase.
    imanufprocessid = models.IntegerField(db_column='iManufProcessID')  # Field name made lowercase.
    iaction = models.IntegerField(db_column='iAction')  # Field name made lowercase.
    ilineno = models.IntegerField(db_column='iLineNo')  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imfpitemid = models.FloatField(db_column='iMFPItemID', blank=True, null=True)  # Field name made lowercase.
    iinvitemid = models.IntegerField(db_column='iInvItemID')  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    inewinvitemid = models.IntegerField(db_column='iNewInvItemID', blank=True, null=True)  # Field name made lowercase.
    inewwarehouseid = models.IntegerField(db_column='iNewWarehouseID', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    fcost = models.FloatField(db_column='fCost', blank=True, null=True)  # Field name made lowercase.
    bprocessed = models.BooleanField(db_column='bProcessed')  # Field name made lowercase.
    dtransactiondate = models.DateTimeField(db_column='dTransactionDate', blank=True, null=True)  # Field name made lowercase.
    dlastupdatedate = models.DateTimeField(db_column='dLastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    fqtyavailable = models.FloatField(db_column='fQtyAvailable', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID', blank=True, null=True)  # Field name made lowercase.
    ipickingslipprinted = models.IntegerField(db_column='iPickingSlipPrinted')  # Field name made lowercase.
    iunmanufacturelineno = models.IntegerField(db_column='iUnmanufactureLineNo')  # Field name made lowercase.
    idocversion = models.IntegerField(db_column='iDocVersion')  # Field name made lowercase.
    flinecost = models.FloatField(db_column='fLineCost')  # Field name made lowercase.
    field_etblmanufprocessline_ibranchid = models.IntegerField(db_column='_etblManufProcessLine_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_dcreateddate = models.DateTimeField(db_column='_etblManufProcessLine_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_dmodifieddate = models.DateTimeField(db_column='_etblManufProcessLine_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_icreatedbranchid = models.IntegerField(db_column='_etblManufProcessLine_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_imodifiedbranchid = models.IntegerField(db_column='_etblManufProcessLine_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_icreatedagentid = models.IntegerField(db_column='_etblManufProcessLine_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_imodifiedagentid = models.IntegerField(db_column='_etblManufProcessLine_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_ichangesetid = models.IntegerField(db_column='_etblManufProcessLine_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblmanufprocessline_checksum = models.TextField(db_column='_etblManufProcessLine_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    istockbinlocationid = models.IntegerField(db_column='iStockBinLocationID', blank=True, null=True)  # Field name made lowercase.
    inewstockbinlocationid = models.IntegerField(db_column='iNewStockBinLocationID', blank=True, null=True)  # Field name made lowercase.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblManufProcessLine'


class Etblordercancelreason(models.Model):
    idordercancelreason = models.AutoField(db_column='idOrderCancelReason', primary_key=True)  # Field name made lowercase.
    ccancellationreasoncode = models.CharField(db_column='cCancellationReasonCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccancellationreasondesc = models.CharField(db_column='cCancellationReasonDesc', max_length=30)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_etblordercancelreason_ibranchid = models.IntegerField(db_column='_etblOrderCancelReason_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_dcreateddate = models.DateTimeField(db_column='_etblOrderCancelReason_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_dmodifieddate = models.DateTimeField(db_column='_etblOrderCancelReason_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_icreatedbranchid = models.IntegerField(db_column='_etblOrderCancelReason_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_imodifiedbranchid = models.IntegerField(db_column='_etblOrderCancelReason_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_icreatedagentid = models.IntegerField(db_column='_etblOrderCancelReason_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_imodifiedagentid = models.IntegerField(db_column='_etblOrderCancelReason_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_ichangesetid = models.IntegerField(db_column='_etblOrderCancelReason_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblordercancelreason_checksum = models.TextField(db_column='_etblOrderCancelReason_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblOrderCancelReason'


class Etblpopdefaults(models.Model):
    idpopdefaults = models.AutoField(db_column='idPOPDefaults', primary_key=True)  # Field name made lowercase.
    bautorequisition = models.BooleanField(db_column='bAutoRequisition')  # Field name made lowercase.
    crequisitionprefix = models.CharField(db_column='cRequisitionPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inextrequisitionno = models.IntegerField(db_column='iNextRequisitionNo', blank=True, null=True)  # Field name made lowercase.
    ipadrequisitionlength = models.IntegerField(db_column='iPadRequisitionLength', blank=True, null=True)  # Field name made lowercase.
    breqbudgetcheck = models.BooleanField(db_column='bReqBudgetCheck')  # Field name made lowercase.
    breqbudgetannual = models.BooleanField(db_column='bReqBudgetAnnual')  # Field name made lowercase.
    breqtopoignoreexpdate = models.BooleanField(db_column='bReqToPOIgnoreExpDate')  # Field name made lowercase.
    bforceproject = models.BooleanField(db_column='bForceProject')  # Field name made lowercase.
    field_etblpopdefaults_ibranchid = models.IntegerField(db_column='_etblPOPDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_dcreateddate = models.DateTimeField(db_column='_etblPOPDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_dmodifieddate = models.DateTimeField(db_column='_etblPOPDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_icreatedbranchid = models.IntegerField(db_column='_etblPOPDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_imodifiedbranchid = models.IntegerField(db_column='_etblPOPDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_icreatedagentid = models.IntegerField(db_column='_etblPOPDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_imodifiedagentid = models.IntegerField(db_column='_etblPOPDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_ichangesetid = models.IntegerField(db_column='_etblPOPDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpopdefaults_checksum = models.TextField(db_column='_etblPOPDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPOPDefaults'


class Etblpoprequisitionlines(models.Model):
    idpoprequisitionlines = models.AutoField(db_column='idPOPRequisitionLines', primary_key=True)  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionID')  # Field name made lowercase.
    imoduleid = models.IntegerField(db_column='iModuleID')  # Field name made lowercase.
    iaccountid = models.IntegerField(db_column='iAccountID')  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID')  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity')  # Field name made lowercase.
    fexpectedprice = models.FloatField(db_column='fExpectedPrice')  # Field name made lowercase.
    dexpecteddate = models.DateTimeField(db_column='dExpectedDate', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    ijobid = models.IntegerField(db_column='iJobID')  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID')  # Field name made lowercase.
    iescalategroupid = models.IntegerField(db_column='iEscalateGroupID')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    clinenotes = models.CharField(db_column='cLineNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ilinestatus = models.IntegerField(db_column='iLineStatus')  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    ipoinvoiceid = models.BigIntegerField(db_column='iPOInvoiceID')  # Field name made lowercase.
    factualprice = models.FloatField(db_column='fActualPrice', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    fexpectedpriceforeign = models.FloatField(db_column='fExpectedPriceForeign', blank=True, null=True)  # Field name made lowercase.
    factualpriceforeign = models.FloatField(db_column='fActualPriceForeign', blank=True, null=True)  # Field name made lowercase.
    dapprovaldate = models.DateTimeField(db_column='dApprovalDate', blank=True, null=True)  # Field name made lowercase.
    iactionagentid = models.IntegerField(db_column='iActionAgentID', blank=True, null=True)  # Field name made lowercase.
    field_etblpoprequisitionlines_ibranchid = models.IntegerField(db_column='_etblPOPRequisitionLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_dcreateddate = models.DateTimeField(db_column='_etblPOPRequisitionLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_dmodifieddate = models.DateTimeField(db_column='_etblPOPRequisitionLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_icreatedbranchid = models.IntegerField(db_column='_etblPOPRequisitionLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_imodifiedbranchid = models.IntegerField(db_column='_etblPOPRequisitionLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_icreatedagentid = models.IntegerField(db_column='_etblPOPRequisitionLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_imodifiedagentid = models.IntegerField(db_column='_etblPOPRequisitionLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_ichangesetid = models.IntegerField(db_column='_etblPOPRequisitionLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlines_checksum = models.TextField(db_column='_etblPOPRequisitionLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csector = models.CharField(db_column='cSector', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ccostcentre = models.CharField(db_column='cCostCentre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    igenrfqagentid = models.IntegerField(db_column='iGenRFQAgentID', blank=True, null=True)  # Field name made lowercase.
    iareaid = models.IntegerField(db_column='iAreaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblPOPRequisitionLines'


class Etblpoprequisitionlineshist(models.Model):
    idpoprequisitionlineshist = models.AutoField(db_column='idPOPRequisitionLinesHist', primary_key=True)  # Field name made lowercase.
    irequisitionhistid = models.IntegerField(db_column='iRequisitionHistID')  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionID')  # Field name made lowercase.
    imoduleid = models.IntegerField(db_column='iModuleID')  # Field name made lowercase.
    iaccountid = models.IntegerField(db_column='iAccountID')  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID')  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity')  # Field name made lowercase.
    fexpectedprice = models.FloatField(db_column='fExpectedPrice')  # Field name made lowercase.
    dexpecteddate = models.DateTimeField(db_column='dExpectedDate', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    ijobid = models.IntegerField(db_column='iJobID')  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID')  # Field name made lowercase.
    iescalategroupid = models.IntegerField(db_column='iEscalateGroupID')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    clinenotes = models.CharField(db_column='cLineNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ilinestatus = models.IntegerField(db_column='iLineStatus')  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    ipoinvoiceid = models.BigIntegerField(db_column='iPOInvoiceID')  # Field name made lowercase.
    factualprice = models.FloatField(db_column='fActualPrice', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    fexpectedpriceforeign = models.FloatField(db_column='fExpectedPriceForeign', blank=True, null=True)  # Field name made lowercase.
    factualpriceforeign = models.FloatField(db_column='fActualPriceForeign', blank=True, null=True)  # Field name made lowercase.
    dapprovaldate = models.DateTimeField(db_column='dApprovalDate', blank=True, null=True)  # Field name made lowercase.
    iactionagentid = models.IntegerField(db_column='iActionAgentID', blank=True, null=True)  # Field name made lowercase.
    field_etblpoprequisitionlineshist_ibranchid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_dcreateddate = models.DateTimeField(db_column='_etblPOPRequisitionLinesHist_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_dmodifieddate = models.DateTimeField(db_column='_etblPOPRequisitionLinesHist_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_icreatedbranchid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_imodifiedbranchid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_icreatedagentid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_imodifiedagentid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_ichangesetid = models.IntegerField(db_column='_etblPOPRequisitionLinesHist_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionlineshist_checksum = models.TextField(db_column='_etblPOPRequisitionLinesHist_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPOPRequisitionLinesHist'


class Etblpoprequisitions(models.Model):
    idpoprequisitions = models.AutoField(db_column='idPOPRequisitions', primary_key=True)  # Field name made lowercase.
    crequisitionno = models.CharField(db_column='cRequisitionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drequisitiondate = models.DateTimeField(db_column='dRequisitionDate')  # Field name made lowercase.
    iprojectdefaultid = models.IntegerField(db_column='iProjectDefaultID')  # Field name made lowercase.
    crequestedby = models.CharField(db_column='cRequestedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iincidenttypedefaultid = models.IntegerField(db_column='iIncidentTypeDefaultID')  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    field_etblpoprequisitions_ibranchid = models.IntegerField(db_column='_etblPOPRequisitions_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_dcreateddate = models.DateTimeField(db_column='_etblPOPRequisitions_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_dmodifieddate = models.DateTimeField(db_column='_etblPOPRequisitions_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_icreatedbranchid = models.IntegerField(db_column='_etblPOPRequisitions_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_imodifiedbranchid = models.IntegerField(db_column='_etblPOPRequisitions_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_icreatedagentid = models.IntegerField(db_column='_etblPOPRequisitions_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_imodifiedagentid = models.IntegerField(db_column='_etblPOPRequisitions_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_ichangesetid = models.IntegerField(db_column='_etblPOPRequisitions_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitions_checksum = models.TextField(db_column='_etblPOPRequisitions_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    csector = models.CharField(db_column='cSector', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblPOPRequisitions'


class Etblpoprequisitionshist(models.Model):
    idpoprequisitionshist = models.AutoField(db_column='idPOPRequisitionsHist', primary_key=True)  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionID')  # Field name made lowercase.
    crequisitionno = models.CharField(db_column='cRequisitionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drequisitiondate = models.DateTimeField(db_column='dRequisitionDate')  # Field name made lowercase.
    iprojectdefaultid = models.IntegerField(db_column='iProjectDefaultID')  # Field name made lowercase.
    crequestedby = models.CharField(db_column='cRequestedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iincidenttypedefaultid = models.IntegerField(db_column='iIncidentTypeDefaultID')  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    iversion = models.IntegerField(db_column='iVersion')  # Field name made lowercase.
    field_etblpoprequisitionshist_ibranchid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_dcreateddate = models.DateTimeField(db_column='_etblPOPRequisitionsHist_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_dmodifieddate = models.DateTimeField(db_column='_etblPOPRequisitionsHist_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_icreatedbranchid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_imodifiedbranchid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_icreatedagentid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_imodifiedagentid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_ichangesetid = models.IntegerField(db_column='_etblPOPRequisitionsHist_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpoprequisitionshist_checksum = models.TextField(db_column='_etblPOPRequisitionsHist_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPOPRequisitionsHist'


class Etblposdevices(models.Model):
    idposdevices = models.AutoField(db_column='idPOSDevices', primary_key=True)  # Field name made lowercase.
    cdevicecode = models.CharField(db_column='cDeviceCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cdevicedescription = models.CharField(db_column='cDeviceDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idevicetype = models.IntegerField(db_column='iDeviceType', blank=True, null=True)  # Field name made lowercase.
    iporttype = models.IntegerField(db_column='iPortType', blank=True, null=True)  # Field name made lowercase.
    iportnum = models.IntegerField(db_column='iPortNum', blank=True, null=True)  # Field name made lowercase.
    ibaudrate = models.IntegerField(db_column='iBaudrate', blank=True, null=True)  # Field name made lowercase.
    ccontrolcodes = models.CharField(db_column='cControlCodes', max_length=120, blank=True, null=True)  # Field name made lowercase.
    ipoledisplaywidth = models.IntegerField(db_column='iPoleDisplayWidth', blank=True, null=True)  # Field name made lowercase.
    ifiscalprinterid = models.IntegerField(db_column='iFiscalPrinterId', blank=True, null=True)  # Field name made lowercase.
    cprintername = models.CharField(db_column='cPrinterName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ifiscalprintermodelsid = models.IntegerField(db_column='iFiscalPrinterModelsId', blank=True, null=True)  # Field name made lowercase.
    cprintercomname = models.CharField(db_column='cPrinterCOMName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblposdevices_ibranchid = models.IntegerField(db_column='_etblPOSDevices_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_dcreateddate = models.DateTimeField(db_column='_etblPOSDevices_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_dmodifieddate = models.DateTimeField(db_column='_etblPOSDevices_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_icreatedbranchid = models.IntegerField(db_column='_etblPOSDevices_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_imodifiedbranchid = models.IntegerField(db_column='_etblPOSDevices_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_icreatedagentid = models.IntegerField(db_column='_etblPOSDevices_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_imodifiedagentid = models.IntegerField(db_column='_etblPOSDevices_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_ichangesetid = models.IntegerField(db_column='_etblPOSDevices_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblposdevices_checksum = models.TextField(db_column='_etblPOSDevices_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPOSDevices'


class Etblpaymentsbasedtax(models.Model):
    idpaymentsbasedtax = models.AutoField(db_column='idPaymentsBasedTax', primary_key=True)  # Field name made lowercase.
    ifromperiod = models.IntegerField(db_column='iFromPeriod', blank=True, null=True)  # Field name made lowercase.
    itoperiod = models.IntegerField(db_column='iToPeriod', blank=True, null=True)  # Field name made lowercase.
    dprocessdate = models.DateTimeField(db_column='dProcessDate', blank=True, null=True)  # Field name made lowercase.
    cnumber = models.CharField(db_column='cNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itrcodeid = models.IntegerField(db_column='iTrCodeID', blank=True, null=True)  # Field name made lowercase.
    fexcludelessthan = models.FloatField(db_column='fExcludeLessThan', blank=True, null=True)  # Field name made lowercase.
    bprocessed = models.BooleanField(db_column='bProcessed')  # Field name made lowercase.
    cprocessedauditnumber = models.CharField(db_column='cProcessedAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblpaymentsbasedtax_ibranchid = models.IntegerField(db_column='_etblPaymentsBasedTax_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_dcreateddate = models.DateTimeField(db_column='_etblPaymentsBasedTax_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_dmodifieddate = models.DateTimeField(db_column='_etblPaymentsBasedTax_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_icreatedbranchid = models.IntegerField(db_column='_etblPaymentsBasedTax_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_imodifiedbranchid = models.IntegerField(db_column='_etblPaymentsBasedTax_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_icreatedagentid = models.IntegerField(db_column='_etblPaymentsBasedTax_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_imodifiedagentid = models.IntegerField(db_column='_etblPaymentsBasedTax_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_ichangesetid = models.IntegerField(db_column='_etblPaymentsBasedTax_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtax_checksum = models.TextField(db_column='_etblPaymentsBasedTax_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPaymentsBasedTax'


class Etblpaymentsbasedtaxpayments(models.Model):
    idpaymentsbasedtaxpayments = models.AutoField(db_column='idPaymentsBasedTaxPayments', primary_key=True)  # Field name made lowercase.
    ipbtbatchid = models.IntegerField(db_column='iPBTBatchID', blank=True, null=True)  # Field name made lowercase.
    imodule = models.IntegerField(db_column='iModule', blank=True, null=True)  # Field name made lowercase.
    iaccountid = models.IntegerField(db_column='iAccountID', blank=True, null=True)  # Field name made lowercase.
    ipostingid = models.BigIntegerField(db_column='iPostingID', blank=True, null=True)  # Field name made lowercase.
    fexclusive = models.FloatField(db_column='fExclusive', blank=True, null=True)  # Field name made lowercase.
    ftax = models.FloatField(db_column='fTax', blank=True, null=True)  # Field name made lowercase.
    finclusive = models.FloatField(db_column='fInclusive', blank=True, null=True)  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID', blank=True, null=True)  # Field name made lowercase.
    igltaxaccountid = models.IntegerField(db_column='iGLTaxAccountID', blank=True, null=True)  # Field name made lowercase.
    callocatedtoreference = models.CharField(db_column='cAllocatedToReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iallocatedpostingid = models.BigIntegerField(db_column='iAllocatedPostingID', blank=True, null=True)  # Field name made lowercase.
    iallocatedstatus = models.IntegerField(db_column='iAllocatedStatus')  # Field name made lowercase.
    field_etblpaymentsbasedtaxpayments_ibranchid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_dcreateddate = models.DateTimeField(db_column='_etblPaymentsBasedTaxPayments_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_dmodifieddate = models.DateTimeField(db_column='_etblPaymentsBasedTaxPayments_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_icreatedbranchid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_imodifiedbranchid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_icreatedagentid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_imodifiedagentid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_ichangesetid = models.IntegerField(db_column='_etblPaymentsBasedTaxPayments_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpaymentsbasedtaxpayments_checksum = models.TextField(db_column='_etblPaymentsBasedTaxPayments_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPaymentsBasedTaxPayments'


class Etblperiod(models.Model):
    idperiod = models.IntegerField(db_column='idPeriod', primary_key=True)  # Field name made lowercase.
    dperioddate = models.DateTimeField(db_column='dPeriodDate')  # Field name made lowercase.
    bblocked = models.BooleanField(db_column='bBlocked')  # Field name made lowercase.
    bpbtprocessed = models.BooleanField(db_column='bPBTProcessed')  # Field name made lowercase.
    bperiodprocessed = models.BooleanField(db_column='bPeriodProcessed')  # Field name made lowercase.
    iyearid = models.IntegerField(db_column='iYearID')  # Field name made lowercase.
    field_etblperiod_ibranchid = models.IntegerField(db_column='_etblPeriod_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_dcreateddate = models.DateTimeField(db_column='_etblPeriod_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_dmodifieddate = models.DateTimeField(db_column='_etblPeriod_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_icreatedbranchid = models.IntegerField(db_column='_etblPeriod_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_imodifiedbranchid = models.IntegerField(db_column='_etblPeriod_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_icreatedagentid = models.IntegerField(db_column='_etblPeriod_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_imodifiedagentid = models.IntegerField(db_column='_etblPeriod_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_ichangesetid = models.IntegerField(db_column='_etblPeriod_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiod_checksum = models.TextField(db_column='_etblPeriod_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPeriod'


class Etblperiodtxids(models.Model):
    idperiodtxids = models.AutoField(db_column='idPeriodTxIDs', primary_key=True)  # Field name made lowercase.
    itxmodule = models.IntegerField(db_column='iTxModule')  # Field name made lowercase.
    itxperiodid = models.IntegerField(db_column='iTxPeriodID')  # Field name made lowercase.
    itxtaxcloseperiodid = models.IntegerField(db_column='iTxTaxClosePeriodID')  # Field name made lowercase.
    iincludedintaxperiodcloseid = models.IntegerField(db_column='iIncludedInTaxPeriodCloseID')  # Field name made lowercase.
    ipostingtxid = models.BigIntegerField(db_column='iPostingTxID')  # Field name made lowercase.
    ipostingtaxtypeid = models.IntegerField(db_column='iPostingTaxTypeID')  # Field name made lowercase.
    fpostingexclusive = models.FloatField(db_column='fPostingExclusive')  # Field name made lowercase.
    fpostingtax = models.FloatField(db_column='fPostingTax')  # Field name made lowercase.
    fpostinginclusive = models.FloatField(db_column='fPostingInclusive')  # Field name made lowercase.
    field_etblperiodtxids_ibranchid = models.IntegerField(db_column='_etblPeriodTxIDs_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_dcreateddate = models.DateTimeField(db_column='_etblPeriodTxIDs_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_dmodifieddate = models.DateTimeField(db_column='_etblPeriodTxIDs_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_icreatedbranchid = models.IntegerField(db_column='_etblPeriodTxIDs_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_imodifiedbranchid = models.IntegerField(db_column='_etblPeriodTxIDs_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_icreatedagentid = models.IntegerField(db_column='_etblPeriodTxIDs_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_imodifiedagentid = models.IntegerField(db_column='_etblPeriodTxIDs_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_ichangesetid = models.IntegerField(db_column='_etblPeriodTxIDs_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxids_checksum = models.TextField(db_column='_etblPeriodTxIDs_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPeriodTxIDs'


class Etblperiodtxsummary(models.Model):
    idperiodtxsummary = models.AutoField(db_column='idPeriodTxSummary', primary_key=True)  # Field name made lowercase.
    dtaxperiodclose = models.DateTimeField(db_column='dTaxPeriodClose')  # Field name made lowercase.
    itaxperiodcloseid = models.IntegerField(db_column='iTaxPeriodCloseID')  # Field name made lowercase.
    fexclusivetotal = models.FloatField(db_column='fExclusiveTotal')  # Field name made lowercase.
    ftaxtotal = models.FloatField(db_column='fTaxTotal')  # Field name made lowercase.
    finclusivetotal = models.FloatField(db_column='fInclusiveTotal')  # Field name made lowercase.
    istatusid = models.IntegerField(db_column='iStatusID')  # Field name made lowercase.
    dstatusupdated = models.DateTimeField(db_column='dStatusUpdated', blank=True, null=True)  # Field name made lowercase.
    cincludedtaxperiodcloseids = models.CharField(db_column='cIncludedTaxPeriodCloseIDs', max_length=100)  # Field name made lowercase.
    field_etblperiodtxsummary_ibranchid = models.IntegerField(db_column='_etblPeriodTxSummary_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_dcreateddate = models.DateTimeField(db_column='_etblPeriodTxSummary_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_dmodifieddate = models.DateTimeField(db_column='_etblPeriodTxSummary_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_icreatedbranchid = models.IntegerField(db_column='_etblPeriodTxSummary_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_imodifiedbranchid = models.IntegerField(db_column='_etblPeriodTxSummary_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_icreatedagentid = models.IntegerField(db_column='_etblPeriodTxSummary_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_imodifiedagentid = models.IntegerField(db_column='_etblPeriodTxSummary_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_ichangesetid = models.IntegerField(db_column='_etblPeriodTxSummary_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodtxsummary_checksum = models.TextField(db_column='_etblPeriodTxSummary_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPeriodTxSummary'


class Etblperiodyear(models.Model):
    idyear = models.IntegerField(db_column='idYear', primary_key=True)  # Field name made lowercase.
    cyeardescription = models.CharField(db_column='cYearDescription', max_length=50)  # Field name made lowercase.
    dyearstartdate = models.DateTimeField(db_column='dYearStartDate')  # Field name made lowercase.
    barchived = models.BooleanField(db_column='bArchived')  # Field name made lowercase.
    bpurged = models.BooleanField(db_column='bPurged')  # Field name made lowercase.
    field_etblperiodyear_ibranchid = models.IntegerField(db_column='_etblPeriodYear_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_dcreateddate = models.DateTimeField(db_column='_etblPeriodYear_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_dmodifieddate = models.DateTimeField(db_column='_etblPeriodYear_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_icreatedbranchid = models.IntegerField(db_column='_etblPeriodYear_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_imodifiedbranchid = models.IntegerField(db_column='_etblPeriodYear_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_icreatedagentid = models.IntegerField(db_column='_etblPeriodYear_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_imodifiedagentid = models.IntegerField(db_column='_etblPeriodYear_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_ichangesetid = models.IntegerField(db_column='_etblPeriodYear_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblperiodyear_checksum = models.TextField(db_column='_etblPeriodYear_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPeriodYear'


class Etblpostdatedcheques(models.Model):
    idpostdatedcheques = models.AutoField(db_column='idPostDatedCheques', primary_key=True)  # Field name made lowercase.
    dpdcdate = models.DateTimeField(db_column='dpdcDate', blank=True, null=True)  # Field name made lowercase.
    ipdcaccountid = models.IntegerField(db_column='ipdcAccountID')  # Field name made lowercase.
    ipdctrcodeid = models.IntegerField(db_column='ipdcTrCodeID')  # Field name made lowercase.
    ipdctaxtypeid = models.IntegerField(db_column='ipdcTaxTypeID')  # Field name made lowercase.
    ipdcprojectid = models.IntegerField(db_column='ipdcProjectID')  # Field name made lowercase.
    ipdcrepid = models.IntegerField(db_column='ipdcRepID')  # Field name made lowercase.
    ipdccontraledgerid = models.IntegerField(db_column='ipdcContraLedgerID')  # Field name made lowercase.
    cpdcreference = models.CharField(db_column='cpdcReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpdcreference2 = models.CharField(db_column='cpdcReference2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpdcdescription = models.CharField(db_column='cpdcDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpdcorderno = models.CharField(db_column='cpdcOrderNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fpdcinclusive = models.FloatField(db_column='fpdcInclusive')  # Field name made lowercase.
    fpdcexclusive = models.FloatField(db_column='fpdcExclusive')  # Field name made lowercase.
    fpdctax = models.FloatField(db_column='fpdcTax')  # Field name made lowercase.
    fpdcfcinclusive = models.FloatField(db_column='fpdcFCInclusive')  # Field name made lowercase.
    fpdcfcexclusive = models.FloatField(db_column='fpdcFCExclusive')  # Field name made lowercase.
    fpdcfctax = models.FloatField(db_column='fpdcFCTax')  # Field name made lowercase.
    ipdcdisctrcodeid = models.IntegerField(db_column='ipdcDiscTrCodeID')  # Field name made lowercase.
    ipdcdisctaxtypeid = models.IntegerField(db_column='ipdcDiscTaxTypeID')  # Field name made lowercase.
    ipdcdisctaxledgerid = models.IntegerField(db_column='ipdcDiscTaxLedgerID')  # Field name made lowercase.
    ipdcdisccontraledgerid = models.IntegerField(db_column='ipdcDiscContraLedgerID')  # Field name made lowercase.
    cpdcdiscdescription = models.CharField(db_column='cpdcDiscDescription', max_length=35)  # Field name made lowercase.
    fpdcdiscinclusive = models.FloatField(db_column='fpdcDiscInclusive')  # Field name made lowercase.
    fpdcdiscexclusive = models.FloatField(db_column='fpdcDiscExclusive')  # Field name made lowercase.
    fpdcdisctax = models.FloatField(db_column='fpdcDiscTax')  # Field name made lowercase.
    fpdcdiscfcinclusive = models.FloatField(db_column='fpdcDiscFCInclusive')  # Field name made lowercase.
    fpdcdiscfcexclusive = models.FloatField(db_column='fpdcDiscFCExclusive')  # Field name made lowercase.
    fpdcdiscfctax = models.FloatField(db_column='fpdcDiscFCTax')  # Field name made lowercase.
    fpdcexchangerate = models.FloatField(db_column='fpdcExchangeRate')  # Field name made lowercase.
    ipdcglcontrolid = models.IntegerField(db_column='ipdcGLControlID')  # Field name made lowercase.
    bpdccancelled = models.BooleanField(db_column='bpdcCancelled')  # Field name made lowercase.
    cpdccancellationreason = models.CharField(db_column='cpdcCancellationReason', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ivmvoucherid = models.IntegerField(db_column='iVMVoucherID')  # Field name made lowercase.
    ipdcdcmodule = models.IntegerField(db_column='ipdcDCModule')  # Field name made lowercase.
    field_etblpostdatedcheques_ibranchid = models.IntegerField(db_column='_etblPostDatedCheques_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_dcreateddate = models.DateTimeField(db_column='_etblPostDatedCheques_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_dmodifieddate = models.DateTimeField(db_column='_etblPostDatedCheques_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_icreatedbranchid = models.IntegerField(db_column='_etblPostDatedCheques_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_imodifiedbranchid = models.IntegerField(db_column='_etblPostDatedCheques_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_icreatedagentid = models.IntegerField(db_column='_etblPostDatedCheques_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_imodifiedagentid = models.IntegerField(db_column='_etblPostDatedCheques_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_ichangesetid = models.IntegerField(db_column='_etblPostDatedCheques_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostdatedcheques_checksum = models.TextField(db_column='_etblPostDatedCheques_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPostDatedCheques'


class Etblpostglhist(models.Model):
    autoidx = models.BigAutoField(db_column='AutoIdx', primary_key=True)  # Field name made lowercase.
    txdate = models.DateTimeField(db_column='TxDate', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='Id', max_length=5)  # Field name made lowercase.
    accountlink = models.IntegerField(db_column='AccountLink', blank=True, null=True)  # Field name made lowercase.
    trcodeid = models.IntegerField(db_column='TrCodeID', blank=True, null=True)  # Field name made lowercase.
    debit = models.FloatField(db_column='Debit', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    fforeigndebit = models.FloatField(db_column='fForeignDebit', blank=True, null=True)  # Field name made lowercase.
    fforeigncredit = models.FloatField(db_column='fForeignCredit', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxtypeid = models.IntegerField(db_column='TaxTypeID', blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='Order_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extordernum = models.CharField(db_column='ExtOrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cauditnumber = models.CharField(db_column='cAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_amount = models.FloatField(db_column='Tax_Amount', blank=True, null=True)  # Field name made lowercase.
    fforeigntax = models.FloatField(db_column='fForeignTax', blank=True, null=True)  # Field name made lowercase.
    project = models.IntegerField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    drcraccount = models.IntegerField(db_column='DrCrAccount', blank=True, null=True)  # Field name made lowercase.
    jobcodelink = models.IntegerField(db_column='JobCodeLink', blank=True, null=True)  # Field name made lowercase.
    crccheck = models.FloatField(db_column='CRCCheck', blank=True, null=True)  # Field name made lowercase.
    dtstamp = models.DateTimeField(db_column='DTStamp', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itaxperiodid = models.IntegerField(db_column='iTaxPeriodID', blank=True, null=True)  # Field name made lowercase.
    cpayeename = models.CharField(db_column='cPayeeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bprintcheque = models.BooleanField(db_column='bPrintCheque')  # Field name made lowercase.
    creference2 = models.CharField(db_column='cReference2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    repid = models.IntegerField(db_column='RepID', blank=True, null=True)  # Field name made lowercase.
    fjcrepcost = models.FloatField(db_column='fJCRepCost', blank=True, null=True)  # Field name made lowercase.
    imfpid = models.IntegerField(db_column='iMFPID', blank=True, null=True)  # Field name made lowercase.
    bisjcdocline = models.BooleanField(db_column='bIsJCDocLine')  # Field name made lowercase.
    bisstgldocline = models.BooleanField(db_column='bIsSTGLDocLine')  # Field name made lowercase.
    iinvlineid = models.BigIntegerField(db_column='iInvLineID')  # Field name made lowercase.
    itxbranchid = models.IntegerField(db_column='iTxBranchID', blank=True, null=True)  # Field name made lowercase.
    cbankref = models.CharField(db_column='cBankRef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bpbtpaid = models.BooleanField(db_column='bPBTPaid')  # Field name made lowercase.
    igltaxaccountid = models.IntegerField(db_column='iGLTaxAccountID', blank=True, null=True)  # Field name made lowercase.
    breconciled = models.BooleanField(db_column='bReconciled')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_etblpostglhist_ibranchid = models.IntegerField(db_column='_etblPostGLHist_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_dcreateddate = models.DateTimeField(db_column='_etblPostGLHist_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_dmodifieddate = models.DateTimeField(db_column='_etblPostGLHist_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_icreatedbranchid = models.IntegerField(db_column='_etblPostGLHist_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_imodifiedbranchid = models.IntegerField(db_column='_etblPostGLHist_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_icreatedagentid = models.IntegerField(db_column='_etblPostGLHist_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_imodifiedagentid = models.IntegerField(db_column='_etblPostGLHist_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_ichangesetid = models.IntegerField(db_column='_etblPostGLHist_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostglhist_checksum = models.TextField(db_column='_etblPostGLHist_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    imajorindustrycodeid = models.IntegerField(db_column='iMajorIndustryCodeID', blank=True, null=True)  # Field name made lowercase.
    iimportdeclarationid = models.IntegerField(db_column='iImportDeclarationID', blank=True, null=True)  # Field name made lowercase.
    chash = models.CharField(db_column='cHash', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ikeyversion = models.IntegerField(db_column='iKeyVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblPostGLHist'


class Etblpostoutstandingexclap(models.Model):
    idpostoutstandingexcl = models.AutoField(db_column='idPostOutstandingExcl')  # Field name made lowercase.
    ipostlnk = models.IntegerField(db_column='iPostLnk')  # Field name made lowercase.
    flnkamount = models.FloatField(db_column='fLnkAmount')  # Field name made lowercase.
    ffclnkamount = models.FloatField(db_column='fFCLnkAmount', blank=True, null=True)  # Field name made lowercase.
    field_etblpostoutstandingexclap_ibranchid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_dcreateddate = models.DateTimeField(db_column='_etblPostOutstandingExclAP_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_dmodifieddate = models.DateTimeField(db_column='_etblPostOutstandingExclAP_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_icreatedbranchid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_imodifiedbranchid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_icreatedagentid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_imodifiedagentid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_ichangesetid = models.IntegerField(db_column='_etblPostOutstandingExclAP_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclap_checksum = models.TextField(db_column='_etblPostOutstandingExclAP_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPostOutstandingExclAP'


class Etblpostoutstandingexclar(models.Model):
    idpostoutstandingexcl = models.AutoField(db_column='idPostOutstandingExcl')  # Field name made lowercase.
    ipostlnk = models.IntegerField(db_column='iPostLnk')  # Field name made lowercase.
    flnkamount = models.FloatField(db_column='fLnkAmount')  # Field name made lowercase.
    ffclnkamount = models.FloatField(db_column='fFCLnkAmount', blank=True, null=True)  # Field name made lowercase.
    field_etblpostoutstandingexclar_ibranchid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_dcreateddate = models.DateTimeField(db_column='_etblPostOutstandingExclAR_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_dmodifieddate = models.DateTimeField(db_column='_etblPostOutstandingExclAR_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_icreatedbranchid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_imodifiedbranchid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_icreatedagentid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_imodifiedagentid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_ichangesetid = models.IntegerField(db_column='_etblPostOutstandingExclAR_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpostoutstandingexclar_checksum = models.TextField(db_column='_etblPostOutstandingExclAR_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPostOutstandingExclAR'


class Etblpricelistname(models.Model):
    idpricelistname = models.AutoField(db_column='IDPriceListName', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=30)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault')  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    dplnametimestamp = models.DateTimeField(db_column='dPLNameTimeStamp', blank=True, null=True)  # Field name made lowercase.
    field_etblpricelistname_ibranchid = models.IntegerField(db_column='_etblPriceListName_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_dcreateddate = models.DateTimeField(db_column='_etblPriceListName_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_dmodifieddate = models.DateTimeField(db_column='_etblPriceListName_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_icreatedbranchid = models.IntegerField(db_column='_etblPriceListName_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_imodifiedbranchid = models.IntegerField(db_column='_etblPriceListName_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_icreatedagentid = models.IntegerField(db_column='_etblPriceListName_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_imodifiedagentid = models.IntegerField(db_column='_etblPriceListName_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_ichangesetid = models.IntegerField(db_column='_etblPriceListName_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistname_checksum = models.TextField(db_column='_etblPriceListName_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPriceListName'


class Etblpricelistprices(models.Model):
    idpricelistprices = models.BigAutoField(db_column='IDPriceListPrices', primary_key=True)  # Field name made lowercase.
    ipricelistnameid = models.IntegerField(db_column='iPriceListNameID')  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    busemarkup = models.BooleanField(db_column='bUseMarkup')  # Field name made lowercase.
    imarkuponcost = models.IntegerField(db_column='iMarkupOnCost')  # Field name made lowercase.
    fmarkuprate = models.FloatField(db_column='fMarkupRate', blank=True, null=True)  # Field name made lowercase.
    fexclprice = models.FloatField(db_column='fExclPrice', blank=True, null=True)  # Field name made lowercase.
    finclprice = models.FloatField(db_column='fInclPrice', blank=True, null=True)  # Field name made lowercase.
    dplpricestimestamp = models.DateTimeField(db_column='dPLPricesTimeStamp', blank=True, null=True)  # Field name made lowercase.
    iuomid = models.IntegerField(db_column='iUOMID')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_etblpricelistprices_ibranchid = models.IntegerField(db_column='_etblPriceListPrices_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_dcreateddate = models.DateTimeField(db_column='_etblPriceListPrices_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_dmodifieddate = models.DateTimeField(db_column='_etblPriceListPrices_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_icreatedbranchid = models.IntegerField(db_column='_etblPriceListPrices_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_imodifiedbranchid = models.IntegerField(db_column='_etblPriceListPrices_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_icreatedagentid = models.IntegerField(db_column='_etblPriceListPrices_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_imodifiedagentid = models.IntegerField(db_column='_etblPriceListPrices_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_ichangesetid = models.IntegerField(db_column='_etblPriceListPrices_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpricelistprices_checksum = models.TextField(db_column='_etblPriceListPrices_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPriceListPrices'


class Etblpromotion(models.Model):
    ipromotionid = models.BigAutoField(db_column='iPromotionID', primary_key=True)  # Field name made lowercase.
    cpromotioncode = models.CharField(db_column='cPromotionCode', max_length=20)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itriggerqty = models.IntegerField(db_column='iTriggerQTY', blank=True, null=True)  # Field name made lowercase.
    iqualifyingqty = models.IntegerField(db_column='iQualifyingQTY', blank=True, null=True)  # Field name made lowercase.
    fdiscount = models.FloatField(db_column='fDiscount', blank=True, null=True)  # Field name made lowercase.
    ffixedprice = models.FloatField(db_column='fFixedPrice', blank=True, null=True)  # Field name made lowercase.
    dstartdate = models.DateTimeField(db_column='dStartDate', blank=True, null=True)  # Field name made lowercase.
    denddate = models.DateTimeField(db_column='dEndDate', blank=True, null=True)  # Field name made lowercase.
    bproportion = models.BooleanField(db_column='bProportion', blank=True, null=True)  # Field name made lowercase.
    blimit = models.BooleanField(db_column='bLimit')  # Field name made lowercase.
    ilimitqty = models.IntegerField(db_column='iLimitQTY', blank=True, null=True)  # Field name made lowercase.
    ipromotiontype = models.IntegerField(db_column='iPromotionType')  # Field name made lowercase.
    ftriggervalue = models.FloatField(db_column='fTriggerValue', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    itriggeruom = models.IntegerField(db_column='iTriggerUOM', blank=True, null=True)  # Field name made lowercase.
    iqualifyinguom = models.IntegerField(db_column='iQualifyingUOM', blank=True, null=True)  # Field name made lowercase.
    icustomertype = models.IntegerField(db_column='iCustomerType', blank=True, null=True)  # Field name made lowercase.
    binclusive = models.BooleanField(db_column='bInclusive')  # Field name made lowercase.
    bapplyonlaybys = models.BooleanField(db_column='bApplyOnLaybys', blank=True, null=True)  # Field name made lowercase.
    field_etblpromotion_ibranchid = models.IntegerField(db_column='_etblPromotion_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_dcreateddate = models.DateTimeField(db_column='_etblPromotion_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_dmodifieddate = models.DateTimeField(db_column='_etblPromotion_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_icreatedbranchid = models.IntegerField(db_column='_etblPromotion_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_imodifiedbranchid = models.IntegerField(db_column='_etblPromotion_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_icreatedagentid = models.IntegerField(db_column='_etblPromotion_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_imodifiedagentid = models.IntegerField(db_column='_etblPromotion_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_ichangesetid = models.IntegerField(db_column='_etblPromotion_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotion_checksum = models.TextField(db_column='_etblPromotion_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ballowreturns = models.BooleanField(db_column='bAllowReturns', blank=True, null=True)  # Field name made lowercase.
    bforcefullbasketreturn = models.BooleanField(db_column='bForceFullBasketReturn', blank=True, null=True)  # Field name made lowercase.
    ireturndays = models.IntegerField(db_column='iReturnDays', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblPromotion'


class Etblpromotionitem(models.Model):
    ipromotionitemid = models.BigAutoField(db_column='iPromotionItemID', primary_key=True)  # Field name made lowercase.
    ipromotionitemlistid = models.BigIntegerField(db_column='iPromotionItemListID', blank=True, null=True)  # Field name made lowercase.
    stocklink = models.IntegerField(db_column='StockLink', blank=True, null=True)  # Field name made lowercase.
    citemgroup = models.CharField(db_column='cItemGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itriggerqty = models.IntegerField(db_column='iTriggerQTY', blank=True, null=True)  # Field name made lowercase.
    iqualifyingqty = models.IntegerField(db_column='iQualifyingQTY', blank=True, null=True)  # Field name made lowercase.
    iuomid = models.IntegerField(db_column='iUOMID', blank=True, null=True)  # Field name made lowercase.
    ipriority = models.IntegerField(db_column='iPriority', blank=True, null=True)  # Field name made lowercase.
    field_etblpromotionitem_ibranchid = models.IntegerField(db_column='_etblPromotionItem_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_dcreateddate = models.DateTimeField(db_column='_etblPromotionItem_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_dmodifieddate = models.DateTimeField(db_column='_etblPromotionItem_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_icreatedbranchid = models.IntegerField(db_column='_etblPromotionItem_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_imodifiedbranchid = models.IntegerField(db_column='_etblPromotionItem_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_icreatedagentid = models.IntegerField(db_column='_etblPromotionItem_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_imodifiedagentid = models.IntegerField(db_column='_etblPromotionItem_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_ichangesetid = models.IntegerField(db_column='_etblPromotionItem_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitem_checksum = models.TextField(db_column='_etblPromotionItem_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPromotionItem'


class Etblpromotionitemlist(models.Model):
    ipromotionitemlistid = models.BigAutoField(db_column='iPromotionItemListID', primary_key=True)  # Field name made lowercase.
    ipromotionid = models.BigIntegerField(db_column='iPromotionID', blank=True, null=True)  # Field name made lowercase.
    clistcode = models.CharField(db_column='cListCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    btriggeritem = models.BooleanField(db_column='bTriggerItem', blank=True, null=True)  # Field name made lowercase.
    bqualifyingitem = models.BooleanField(db_column='bQualifyingItem', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_etblpromotionitemlist_ibranchid = models.IntegerField(db_column='_etblPromotionItemList_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_dcreateddate = models.DateTimeField(db_column='_etblPromotionItemList_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_dmodifieddate = models.DateTimeField(db_column='_etblPromotionItemList_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_icreatedbranchid = models.IntegerField(db_column='_etblPromotionItemList_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_imodifiedbranchid = models.IntegerField(db_column='_etblPromotionItemList_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_icreatedagentid = models.IntegerField(db_column='_etblPromotionItemList_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_imodifiedagentid = models.IntegerField(db_column='_etblPromotionItemList_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_ichangesetid = models.IntegerField(db_column='_etblPromotionItemList_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlist_checksum = models.TextField(db_column='_etblPromotionItemList_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPromotionItemList'


class Etblpromotionitemlistlink(models.Model):
    ipromotionitemlistlinkid = models.BigAutoField(db_column='iPromotionItemListLinkID', primary_key=True)  # Field name made lowercase.
    ipromotionid = models.BigIntegerField(db_column='iPromotionID', blank=True, null=True)  # Field name made lowercase.
    ipromotionitemlistid = models.BigIntegerField(db_column='iPromotionItemListID', blank=True, null=True)  # Field name made lowercase.
    blimit = models.BooleanField(db_column='bLimit')  # Field name made lowercase.
    ilimitqty = models.IntegerField(db_column='iLimitQTY', blank=True, null=True)  # Field name made lowercase.
    bmultibuy = models.BooleanField(db_column='bMultiBuy')  # Field name made lowercase.
    field_etblpromotionitemlistlink_ibranchid = models.IntegerField(db_column='_etblPromotionItemListLink_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_dcreateddate = models.DateTimeField(db_column='_etblPromotionItemListLink_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_dmodifieddate = models.DateTimeField(db_column='_etblPromotionItemListLink_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_icreatedbranchid = models.IntegerField(db_column='_etblPromotionItemListLink_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_imodifiedbranchid = models.IntegerField(db_column='_etblPromotionItemListLink_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_icreatedagentid = models.IntegerField(db_column='_etblPromotionItemListLink_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_imodifiedagentid = models.IntegerField(db_column='_etblPromotionItemListLink_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_ichangesetid = models.IntegerField(db_column='_etblPromotionItemListLink_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistlink_checksum = models.TextField(db_column='_etblPromotionItemListLink_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPromotionItemListLink'


class Etblpromotionitemlistqty(models.Model):
    ipromotionitemlistqtyid = models.BigAutoField(db_column='iPromotionItemListQTYID', primary_key=True)  # Field name made lowercase.
    ipromotionitemlistlinkid = models.BigIntegerField(db_column='iPromotionItemListLinkID', blank=True, null=True)  # Field name made lowercase.
    fdiscountvalue = models.FloatField(db_column='fDiscountValue', blank=True, null=True)  # Field name made lowercase.
    ivaluetype = models.IntegerField(db_column='iValueType', blank=True, null=True)  # Field name made lowercase.
    ftriggerqty = models.FloatField(db_column='fTriggerQTY', blank=True, null=True)  # Field name made lowercase.
    fqualifyingqty = models.FloatField(db_column='fQualifyingQTY', blank=True, null=True)  # Field name made lowercase.
    field_etblpromotionitemlistqty_ibranchid = models.IntegerField(db_column='_etblPromotionItemListQTY_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_dcreateddate = models.DateTimeField(db_column='_etblPromotionItemListQTY_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_dmodifieddate = models.DateTimeField(db_column='_etblPromotionItemListQTY_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_icreatedbranchid = models.IntegerField(db_column='_etblPromotionItemListQTY_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_imodifiedbranchid = models.IntegerField(db_column='_etblPromotionItemListQTY_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_icreatedagentid = models.IntegerField(db_column='_etblPromotionItemListQTY_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_imodifiedagentid = models.IntegerField(db_column='_etblPromotionItemListQTY_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_ichangesetid = models.IntegerField(db_column='_etblPromotionItemListQTY_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblpromotionitemlistqty_checksum = models.TextField(db_column='_etblPromotionItemListQTY_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblPromotionItemListQTY'


class Etblremittancebatchdefaults(models.Model):
    idremittancebatchdefaults = models.AutoField(db_column='idRemittanceBatchDefaults', primary_key=True)  # Field name made lowercase.
    bautonumbers = models.BooleanField(db_column='bAutoNumbers', blank=True, null=True)  # Field name made lowercase.
    iautonumpadlength = models.IntegerField(db_column='iAutoNumPadLength', blank=True, null=True)  # Field name made lowercase.
    cautonumprefix = models.CharField(db_column='cAutoNumPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    bautorefnumbers = models.BooleanField(db_column='bAutoRefNumbers', blank=True, null=True)  # Field name made lowercase.
    iautorefnumpadlength = models.IntegerField(db_column='iAutoRefNumPadLength', blank=True, null=True)  # Field name made lowercase.
    cautorefnumprefix = models.CharField(db_column='cAutoRefNumPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    field_etblremittancebatchdefaults_ibranchid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_dcreateddate = models.DateTimeField(db_column='_etblRemittanceBatchDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_dmodifieddate = models.DateTimeField(db_column='_etblRemittanceBatchDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_icreatedbranchid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_imodifiedbranchid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_icreatedagentid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_imodifiedagentid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_ichangesetid = models.IntegerField(db_column='_etblRemittanceBatchDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatchdefaults_checksum = models.TextField(db_column='_etblRemittanceBatchDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    blinerefautorefnumbers = models.BooleanField(db_column='bLineRefAutoRefNumbers')  # Field name made lowercase.
    ilinerefautorefnumpadlength = models.IntegerField(db_column='iLineRefAutoRefNumPadLength')  # Field name made lowercase.
    clinerefautorefnumprefix = models.CharField(db_column='cLineRefAutoRefNumPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblRemittanceBatchDefaults'


class Etblremittancebatches(models.Model):
    idremittancebatches = models.AutoField(db_column='idRemittanceBatches', primary_key=True)  # Field name made lowercase.
    cbatchno = models.CharField(db_column='cBatchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbatchdesc = models.CharField(db_column='cBatchDesc', max_length=50)  # Field name made lowercase.
    cbatchref = models.CharField(db_column='cBatchRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bclearafterpost = models.BooleanField(db_column='bClearAfterPost')  # Field name made lowercase.
    bcheckedout = models.BooleanField(db_column='bCheckedOut', blank=True, null=True)  # Field name made lowercase.
    iagentcheckedout = models.IntegerField(db_column='iAgentCheckedOut', blank=True, null=True)  # Field name made lowercase.
    dprocesseddate = models.DateTimeField(db_column='dProcessedDate', blank=True, null=True)  # Field name made lowercase.
    bchequeeftsrun = models.BooleanField(db_column='bChequeEFTSRun', blank=True, null=True)  # Field name made lowercase.
    idefaulttrantype = models.IntegerField(db_column='idefaultTranType', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bincdescription = models.BooleanField(db_column='bIncDescription', blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bincreference = models.BooleanField(db_column='bIncReference', blank=True, null=True)  # Field name made lowercase.
    bdefaultprintcheque = models.BooleanField(db_column='bdefaultPrintCheque', blank=True, null=True)  # Field name made lowercase.
    ballinvoicespaid = models.BooleanField(db_column='bAllInvoicesPaid', blank=True, null=True)  # Field name made lowercase.
    bprintchequeoreftsonly = models.BooleanField(db_column='bPrintChequeOrEFTSOnly', blank=True, null=True)  # Field name made lowercase.
    bprintremittance = models.BooleanField(db_column='bPrintRemittance', blank=True, null=True)  # Field name made lowercase.
    bprintalsochequeorefts = models.BooleanField(db_column='bPrintAlsoChequeOrEFTS', blank=True, null=True)  # Field name made lowercase.
    bprintsamepageremcheq = models.BooleanField(db_column='bPrintSamePageRemCheq', blank=True, null=True)  # Field name made lowercase.
    ceftsfilename = models.CharField(db_column='cEFTSFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idisctrantype = models.IntegerField(db_column='iDiscTranType', blank=True, null=True)  # Field name made lowercase.
    bpromptvalidationonclose = models.BooleanField(db_column='bPromptValidationOnClose', blank=True, null=True)  # Field name made lowercase.
    bwarnnotincludedinrun = models.BooleanField(db_column='bWarnNotIncludedInRun', blank=True, null=True)  # Field name made lowercase.
    bpreviewbeforeprint = models.BooleanField(db_column='bPreviewBeforePrint', blank=True, null=True)  # Field name made lowercase.
    idisctaxtype = models.IntegerField(db_column='iDiscTaxType', blank=True, null=True)  # Field name made lowercase.
    bdefaulteftsproc = models.BooleanField(db_column='bdefaultEFTSProc', blank=True, null=True)  # Field name made lowercase.
    deftsactiondate = models.DateTimeField(db_column='dEFTSActionDate', blank=True, null=True)  # Field name made lowercase.
    bapplyterms = models.BooleanField(db_column='bApplyTerms', blank=True, null=True)  # Field name made lowercase.
    ceftsbatchdescription = models.CharField(db_column='cEFTSBatchDescription', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ieftsbatchnumber = models.IntegerField(db_column='iEFTSBatchNumber', blank=True, null=True)  # Field name made lowercase.
    ddefaultpaymentdate = models.DateTimeField(db_column='ddefaultPaymentDate', blank=True, null=True)  # Field name made lowercase.
    ceftsacbservicetype = models.CharField(db_column='cEFTSACBServiceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ieftstype = models.IntegerField(db_column='iEFTSType', blank=True, null=True)  # Field name made lowercase.
    bincludesuponhold = models.BooleanField(db_column='bIncludeSupOnHold', blank=True, null=True)  # Field name made lowercase.
    fmaxamt = models.FloatField(db_column='fMaxAmt', blank=True, null=True)  # Field name made lowercase.
    fminamt = models.FloatField(db_column='fMinAmt', blank=True, null=True)  # Field name made lowercase.
    dpayduedate = models.DateTimeField(db_column='dPayDueDate', blank=True, null=True)  # Field name made lowercase.
    csuparea = models.CharField(db_column='cSupArea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    csupfrom = models.CharField(db_column='cSupFrom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csupgrp = models.CharField(db_column='cSupGrp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    csupto = models.CharField(db_column='cSupTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ceftstransactiondesc = models.CharField(db_column='cEFTSTransactionDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ctrcodes = models.CharField(db_column='cTrCodes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ceftslayoutdesc = models.CharField(db_column='cEFTSLayoutDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ballocatetooldest = models.BooleanField(db_column='bAllocateToOldest', blank=True, null=True)  # Field name made lowercase.
    ballowsettdisc = models.BooleanField(db_column='bAllowSettDisc', blank=True, null=True)  # Field name made lowercase.
    ceftsbatchtypestring = models.CharField(db_column='cEFTSBatchTypeString', max_length=5, blank=True, null=True)  # Field name made lowercase.
    beftsautodateforward = models.BooleanField(db_column='bEFTSAutoDateForward', blank=True, null=True)  # Field name made lowercase.
    beftstxproofofpayment = models.BooleanField(db_column='bEFTSTxProofOfPayment', blank=True, null=True)  # Field name made lowercase.
    beftsduplicatefile = models.BooleanField(db_column='bEFTSDuplicateFile', blank=True, null=True)  # Field name made lowercase.
    beftsexportorderletter = models.BooleanField(db_column='bEFTSExportOrderLetter', blank=True, null=True)  # Field name made lowercase.
    ceftsorderletter = models.CharField(db_column='cEFTSOrderLetter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bincloutstandingdebits = models.BooleanField(db_column='bInclOutstandingDebits', blank=True, null=True)  # Field name made lowercase.
    bautoallocoutstanding = models.BooleanField(db_column='bAutoAllocOutstanding', blank=True, null=True)  # Field name made lowercase.
    btxonhold = models.BooleanField(db_column='bTxOnHold', blank=True, null=True)  # Field name made lowercase.
    btxonholdremove = models.BooleanField(db_column='bTxOnHoldRemove', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus')  # Field name made lowercase.
    ibankdetailid = models.IntegerField(db_column='iBankDetailID', blank=True, null=True)  # Field name made lowercase.
    field_etblremittancebatches_ibranchid = models.IntegerField(db_column='_etblRemittanceBatches_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_dcreateddate = models.DateTimeField(db_column='_etblRemittanceBatches_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_dmodifieddate = models.DateTimeField(db_column='_etblRemittanceBatches_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_icreatedbranchid = models.IntegerField(db_column='_etblRemittanceBatches_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_imodifiedbranchid = models.IntegerField(db_column='_etblRemittanceBatches_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_icreatedagentid = models.IntegerField(db_column='_etblRemittanceBatches_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_imodifiedagentid = models.IntegerField(db_column='_etblRemittanceBatches_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_ichangesetid = models.IntegerField(db_column='_etblRemittanceBatches_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancebatches_checksum = models.TextField(db_column='_etblRemittanceBatches_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblRemittanceBatches'


class Etblremittancedefaults(models.Model):
    idremittancedefaults = models.AutoField(db_column='IDRemittanceDefaults', primary_key=True)  # Field name made lowercase.
    bchequeeftsrun = models.BooleanField(db_column='bChequeEFTSRun')  # Field name made lowercase.
    idefaulttrantype = models.IntegerField(db_column='iDefaultTranType', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bincdescription = models.BooleanField(db_column='bIncDescription')  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bincreference = models.BooleanField(db_column='bIncReference')  # Field name made lowercase.
    bdefaultprintcheque = models.BooleanField(db_column='bDefaultPrintCheque')  # Field name made lowercase.
    ballinvoicespaid = models.BooleanField(db_column='bAllInvoicesPaid')  # Field name made lowercase.
    bprintchequeoreftsonly = models.BooleanField(db_column='bPrintChequeOrEFTSOnly')  # Field name made lowercase.
    bprintremittance = models.BooleanField(db_column='bPrintRemittance')  # Field name made lowercase.
    bprintalsochequeorefts = models.BooleanField(db_column='bPrintAlsoChequeOrEFTS')  # Field name made lowercase.
    bprintsamepageremcheq = models.BooleanField(db_column='bPrintSamePageRemCheq')  # Field name made lowercase.
    ceftsfilename = models.CharField(db_column='cEFTSFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idisctrantype = models.IntegerField(db_column='iDiscTranType', blank=True, null=True)  # Field name made lowercase.
    bpromptvalidationonclose = models.BooleanField(db_column='bPromptValidationOnClose')  # Field name made lowercase.
    bwarnnotincludedinrun = models.BooleanField(db_column='bWarnNotIncludedInRun')  # Field name made lowercase.
    bpreviewbeforeprint = models.BooleanField(db_column='bPreviewBeforePrint')  # Field name made lowercase.
    idisctaxtype = models.IntegerField(db_column='iDiscTaxType', blank=True, null=True)  # Field name made lowercase.
    bdefaulteftsproc = models.BooleanField(db_column='bDefaultEFTSProc')  # Field name made lowercase.
    deftsactiondate = models.DateTimeField(db_column='dEFTSActionDate', blank=True, null=True)  # Field name made lowercase.
    bapplyterms = models.BooleanField(db_column='bApplyTerms')  # Field name made lowercase.
    ceftsbatchdescription = models.CharField(db_column='cEFTSBatchDescription', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ieftsbatchnumber = models.IntegerField(db_column='iEFTSBatchNumber', blank=True, null=True)  # Field name made lowercase.
    ddefaultpaymentdate = models.DateTimeField(db_column='dDefaultPaymentDate', blank=True, null=True)  # Field name made lowercase.
    ceftsacbservicetype = models.CharField(db_column='cEFTSACBServiceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ieftstype = models.IntegerField(db_column='iEFTSType', blank=True, null=True)  # Field name made lowercase.
    bincludesuponhold = models.BooleanField(db_column='bIncludeSupOnHold')  # Field name made lowercase.
    fmaxamt = models.FloatField(db_column='fMaxAmt', blank=True, null=True)  # Field name made lowercase.
    fminamt = models.FloatField(db_column='fMinAmt', blank=True, null=True)  # Field name made lowercase.
    dpayduedate = models.DateTimeField(db_column='dPayDueDate', blank=True, null=True)  # Field name made lowercase.
    csuparea = models.CharField(db_column='cSupArea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    csupfrom = models.CharField(db_column='cSupFrom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csupgrp = models.CharField(db_column='cSupGrp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    csupto = models.CharField(db_column='cSupTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ceftstransactiondesc = models.CharField(db_column='cEFTSTransactionDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ctrcodes = models.CharField(db_column='cTrCodes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ceftslayoutdesc = models.CharField(db_column='cEFTSLayoutDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ballocatetooldest = models.BooleanField(db_column='bAllocateToOldest')  # Field name made lowercase.
    ballowsettdisc = models.BooleanField(db_column='bAllowSettDisc')  # Field name made lowercase.
    ceftsbatchtypestring = models.CharField(db_column='cEFTSBatchTypeString', max_length=5, blank=True, null=True)  # Field name made lowercase.
    beftsautodateforward = models.BooleanField(db_column='bEFTSAutoDateForward')  # Field name made lowercase.
    beftstxproofofpayment = models.BooleanField(db_column='bEFTSTxProofOfPayment')  # Field name made lowercase.
    beftsduplicatefile = models.BooleanField(db_column='bEFTSDuplicateFile')  # Field name made lowercase.
    beftsexportorderletter = models.BooleanField(db_column='bEFTSExportOrderLetter')  # Field name made lowercase.
    ceftsorderletter = models.CharField(db_column='cEFTSOrderLetter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bincloutsandingdebits = models.BooleanField(db_column='bInclOutsandingDebits')  # Field name made lowercase.
    bautoallocoutstanding = models.BooleanField(db_column='bAutoAllocOutstanding')  # Field name made lowercase.
    bloaddefaults = models.BooleanField(db_column='bLoadDefaults', blank=True, null=True)  # Field name made lowercase.
    btxonhold = models.BooleanField(db_column='bTxOnHold')  # Field name made lowercase.
    btxonholdremove = models.BooleanField(db_column='bTxOnHoldRemove')  # Field name made lowercase.
    field_etblremittancedefaults_ibranchid = models.IntegerField(db_column='_etblRemittanceDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_dcreateddate = models.DateTimeField(db_column='_etblRemittanceDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_dmodifieddate = models.DateTimeField(db_column='_etblRemittanceDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_icreatedbranchid = models.IntegerField(db_column='_etblRemittanceDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_imodifiedbranchid = models.IntegerField(db_column='_etblRemittanceDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_icreatedagentid = models.IntegerField(db_column='_etblRemittanceDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_imodifiedagentid = models.IntegerField(db_column='_etblRemittanceDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_ichangesetid = models.IntegerField(db_column='_etblRemittanceDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancedefaults_checksum = models.TextField(db_column='_etblRemittanceDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblRemittanceDefaults'


class Etblremittancelines(models.Model):
    idremittancelines = models.AutoField(db_column='IDRemittanceLines', primary_key=True)  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID', blank=True, null=True)  # Field name made lowercase.
    cdocumentnumber = models.CharField(db_column='cDocumentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    famountoutstanding = models.FloatField(db_column='fAmountOutstanding', blank=True, null=True)  # Field name made lowercase.
    fdiscamount = models.FloatField(db_column='fDiscAmount', blank=True, null=True)  # Field name made lowercase.
    famounttopay = models.FloatField(db_column='fAmountToPay', blank=True, null=True)  # Field name made lowercase.
    bpaytransaction = models.BooleanField(db_column='bPayTransaction')  # Field name made lowercase.
    fdiscamountexcl = models.FloatField(db_column='fDiscAmountExcl', blank=True, null=True)  # Field name made lowercase.
    fdisctaxamount = models.FloatField(db_column='fDiscTaxAmount', blank=True, null=True)  # Field name made lowercase.
    ddocumentdate = models.DateTimeField(db_column='dDocumentDate', blank=True, null=True)  # Field name made lowercase.
    fdocumentamount = models.FloatField(db_column='fDocumentAmount', blank=True, null=True)  # Field name made lowercase.
    ballocated = models.BooleanField(db_column='bAllocated')  # Field name made lowercase.
    iinvrecid = models.BigIntegerField(db_column='iInvRecID', blank=True, null=True)  # Field name made lowercase.
    cinvdescription = models.CharField(db_column='cInvDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cinvreference1 = models.CharField(db_column='cInvReference1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cinvreference2 = models.CharField(db_column='cInvReference2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iinvsettlementtermsid = models.IntegerField(db_column='iInvSettlementTermsID')  # Field name made lowercase.
    fsettdiscamount = models.FloatField(db_column='fSettDiscAmount')  # Field name made lowercase.
    csetttermcode = models.CharField(db_column='cSettTermCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fsetttermdiscperc = models.FloatField(db_column='fSettTermDiscPerc')  # Field name made lowercase.
    isetttermdays = models.IntegerField(db_column='iSettTermDays')  # Field name made lowercase.
    isetttermpaymethod = models.IntegerField(db_column='iSettTermPayMethod')  # Field name made lowercase.
    bapplydisc = models.BooleanField(db_column='bApplyDisc')  # Field name made lowercase.
    fdiscperc = models.FloatField(db_column='fDiscPerc')  # Field name made lowercase.
    cinvordernumber = models.CharField(db_column='cInvOrderNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    btxonhold = models.BooleanField(db_column='bTxOnHold')  # Field name made lowercase.
    ibatchid = models.IntegerField(db_column='iBatchID')  # Field name made lowercase.
    famountpaid = models.FloatField(db_column='fAmountPaid')  # Field name made lowercase.
    field_etblremittancelines_ibranchid = models.IntegerField(db_column='_etblRemittanceLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_dcreateddate = models.DateTimeField(db_column='_etblRemittanceLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_dmodifieddate = models.DateTimeField(db_column='_etblRemittanceLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_icreatedbranchid = models.IntegerField(db_column='_etblRemittanceLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_imodifiedbranchid = models.IntegerField(db_column='_etblRemittanceLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_icreatedagentid = models.IntegerField(db_column='_etblRemittanceLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_imodifiedagentid = models.IntegerField(db_column='_etblRemittanceLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_ichangesetid = models.IntegerField(db_column='_etblRemittanceLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancelines_checksum = models.TextField(db_column='_etblRemittanceLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblRemittanceLines'


class Etblremittancesuppliers(models.Model):
    idremittancesuppliers = models.AutoField(db_column='IDRemittanceSuppliers', primary_key=True)  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID', blank=True, null=True)  # Field name made lowercase.
    cpayeename = models.CharField(db_column='cPayeeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bprintcheque = models.BooleanField(db_column='bPrintCheque')  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdiscreceived = models.FloatField(db_column='fDiscReceived', blank=True, null=True)  # Field name made lowercase.
    ftotalpaid = models.FloatField(db_column='fTotalPaid', blank=True, null=True)  # Field name made lowercase.
    fdocumenttotal = models.FloatField(db_column='fDocumentTotal', blank=True, null=True)  # Field name made lowercase.
    bincludedinrun = models.BooleanField(db_column='bIncludedInRun')  # Field name made lowercase.
    bchequeprinted = models.BooleanField(db_column='bChequePrinted')  # Field name made lowercase.
    bremittanceprinted = models.BooleanField(db_column='bRemittancePrinted')  # Field name made lowercase.
    beftsprocessed = models.BooleanField(db_column='bEFTSProcessed')  # Field name made lowercase.
    funallocateddebits = models.FloatField(db_column='fUnallocatedDebits', blank=True, null=True)  # Field name made lowercase.
    fallocateddebits = models.FloatField(db_column='fAllocatedDebits', blank=True, null=True)  # Field name made lowercase.
    fdiscreceivedexcl = models.FloatField(db_column='fDiscReceivedExcl', blank=True, null=True)  # Field name made lowercase.
    ftotalpaidexcl = models.FloatField(db_column='fTotalPaidExcl', blank=True, null=True)  # Field name made lowercase.
    fdisctaxamount = models.FloatField(db_column='fDiscTaxAmount', blank=True, null=True)  # Field name made lowercase.
    bposted = models.BooleanField(db_column='bPosted')  # Field name made lowercase.
    bproduceefts = models.BooleanField(db_column='bProduceEFTS')  # Field name made lowercase.
    idisctaxtype = models.IntegerField(db_column='iDiscTaxType', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.
    dpaymentdate = models.DateTimeField(db_column='dPaymentDate', blank=True, null=True)  # Field name made lowercase.
    cpayrecids = models.CharField(db_column='cPayRecIDs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bdefaultpayallinvoices = models.BooleanField(db_column='bDefaultPayAllInvoices')  # Field name made lowercase.
    cdccode = models.CharField(db_column='cDCCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdcname = models.CharField(db_column='cDCName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    funallocatedcredits = models.FloatField(db_column='fUnallocatedCredits', blank=True, null=True)  # Field name made lowercase.
    iinvoicecount = models.IntegerField(db_column='iInvoiceCount', blank=True, null=True)  # Field name made lowercase.
    iconfiguredcount = models.FloatField(db_column='iConfiguredCount', blank=True, null=True)  # Field name made lowercase.
    ibatchid = models.IntegerField(db_column='iBatchID')  # Field name made lowercase.
    famounttopay = models.FloatField(db_column='fAmountToPay')  # Field name made lowercase.
    field_etblremittancesuppliers_ibranchid = models.IntegerField(db_column='_etblRemittanceSuppliers_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_dcreateddate = models.DateTimeField(db_column='_etblRemittanceSuppliers_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_dmodifieddate = models.DateTimeField(db_column='_etblRemittanceSuppliers_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_icreatedbranchid = models.IntegerField(db_column='_etblRemittanceSuppliers_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_imodifiedbranchid = models.IntegerField(db_column='_etblRemittanceSuppliers_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_icreatedagentid = models.IntegerField(db_column='_etblRemittanceSuppliers_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_imodifiedagentid = models.IntegerField(db_column='_etblRemittanceSuppliers_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_ichangesetid = models.IntegerField(db_column='_etblRemittanceSuppliers_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblremittancesuppliers_checksum = models.TextField(db_column='_etblRemittanceSuppliers_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    iinstructiontype = models.IntegerField(db_column='iInstructionType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblRemittanceSuppliers'


class Etblrepllog(models.Model):
    idrepllog = models.AutoField(db_column='idReplLog', primary_key=True)  # Field name made lowercase.
    ichangesetid = models.IntegerField(db_column='iChangeSetID')  # Field name made lowercase.
    ibranchid = models.IntegerField(db_column='iBranchID')  # Field name made lowercase.
    caction = models.CharField(db_column='cAction', max_length=1)  # Field name made lowercase.
    dinitdateutc = models.DateTimeField(db_column='dInitDateUtc', blank=True, null=True)  # Field name made lowercase.
    cfilename = models.CharField(db_column='cFileName', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblReplLog'


class Etblreportjoblog(models.Model):
    idreportjoblog = models.AutoField(db_column='idReportJobLog', primary_key=True)  # Field name made lowercase.
    ijobtype = models.IntegerField(db_column='iJobType', blank=True, null=True)  # Field name made lowercase.
    ireportjobid = models.IntegerField(db_column='iReportJobID', blank=True, null=True)  # Field name made lowercase.
    dlogtime = models.DateTimeField(db_column='dLogTime', blank=True, null=True)  # Field name made lowercase.
    ilogtype = models.IntegerField(db_column='iLogType', blank=True, null=True)  # Field name made lowercase.
    clogdescription = models.CharField(db_column='cLogDescription', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    nlogdata = models.BinaryField(db_column='nLogData', blank=True, null=True)  # Field name made lowercase.
    field_etblreportjoblog_ibranchid = models.IntegerField(db_column='_etblReportJobLog_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_dcreateddate = models.DateTimeField(db_column='_etblReportJobLog_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_dmodifieddate = models.DateTimeField(db_column='_etblReportJobLog_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_icreatedbranchid = models.IntegerField(db_column='_etblReportJobLog_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_imodifiedbranchid = models.IntegerField(db_column='_etblReportJobLog_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_icreatedagentid = models.IntegerField(db_column='_etblReportJobLog_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_imodifiedagentid = models.IntegerField(db_column='_etblReportJobLog_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_ichangesetid = models.IntegerField(db_column='_etblReportJobLog_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjoblog_checksum = models.TextField(db_column='_etblReportJobLog_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblReportJobLog'


class Etblreportjobs(models.Model):
    idreportjobs = models.AutoField(db_column='idReportJobs', primary_key=True)  # Field name made lowercase.
    ireportjobparentid = models.IntegerField(db_column='iReportJobParentID', blank=True, null=True)  # Field name made lowercase.
    creportjobname = models.CharField(db_column='cReportJobName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ireportjobtype = models.IntegerField(db_column='iReportJobType', blank=True, null=True)  # Field name made lowercase.
    nreportjobprops = models.TextField(db_column='nReportJobProps', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ireportjobagentid = models.IntegerField(db_column='iReportJobAgentID', blank=True, null=True)  # Field name made lowercase.
    ibatchid = models.IntegerField(db_column='iBatchID')  # Field name made lowercase.
    field_etblreportjobs_ibranchid = models.IntegerField(db_column='_etblReportJobs_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_dcreateddate = models.DateTimeField(db_column='_etblReportJobs_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_dmodifieddate = models.DateTimeField(db_column='_etblReportJobs_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_icreatedbranchid = models.IntegerField(db_column='_etblReportJobs_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_imodifiedbranchid = models.IntegerField(db_column='_etblReportJobs_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_icreatedagentid = models.IntegerField(db_column='_etblReportJobs_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_imodifiedagentid = models.IntegerField(db_column='_etblReportJobs_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_ichangesetid = models.IntegerField(db_column='_etblReportJobs_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblreportjobs_checksum = models.TextField(db_column='_etblReportJobs_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    cbackuptopath = models.TextField(db_column='cBackupToPath', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblReportJobs'


class Etblrevaluationhistory(models.Model):
    idrevaluationhistory = models.AutoField(db_column='idRevaluationHistory', primary_key=True)  # Field name made lowercase.
    imodule = models.IntegerField(db_column='iModule', blank=True, null=True)  # Field name made lowercase.
    iaccountid = models.IntegerField(db_column='iAccountID', blank=True, null=True)  # Field name made lowercase.
    dtransactiondate = models.DateTimeField(db_column='dTransactionDate', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    frevaluationrate = models.FloatField(db_column='fRevaluationRate', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    bposted = models.BooleanField(db_column='bPosted', blank=True, null=True)  # Field name made lowercase.
    frevaluationamount = models.FloatField(db_column='fRevaluationAmount', blank=True, null=True)  # Field name made lowercase.
    foldhomebalance = models.FloatField(db_column='fOldHomeBalance', blank=True, null=True)  # Field name made lowercase.
    fnewhomebalance = models.FloatField(db_column='fNewHomeBalance', blank=True, null=True)  # Field name made lowercase.
    cbatchnumber = models.CharField(db_column='cBatchNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iglaccountprofitloss = models.IntegerField(db_column='iGLAccountProfitLoss', blank=True, null=True)  # Field name made lowercase.
    iglaccountprovision = models.IntegerField(db_column='iGLAccountProvision', blank=True, null=True)  # Field name made lowercase.
    caccountname = models.CharField(db_column='cAccountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iperiodid = models.IntegerField(db_column='iPeriodID')  # Field name made lowercase.
    fforeignbalance = models.FloatField(db_column='fForeignBalance')  # Field name made lowercase.
    duptotxdate = models.DateTimeField(db_column='dUpToTxDate', blank=True, null=True)  # Field name made lowercase.
    drevalratedate = models.DateTimeField(db_column='dRevalRateDate', blank=True, null=True)  # Field name made lowercase.
    field_etblrevaluationhistory_ibranchid = models.IntegerField(db_column='_etblRevaluationHistory_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_dcreateddate = models.DateTimeField(db_column='_etblRevaluationHistory_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_dmodifieddate = models.DateTimeField(db_column='_etblRevaluationHistory_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_icreatedbranchid = models.IntegerField(db_column='_etblRevaluationHistory_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_imodifiedbranchid = models.IntegerField(db_column='_etblRevaluationHistory_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_icreatedagentid = models.IntegerField(db_column='_etblRevaluationHistory_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_imodifiedagentid = models.IntegerField(db_column='_etblRevaluationHistory_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_ichangesetid = models.IntegerField(db_column='_etblRevaluationHistory_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblrevaluationhistory_checksum = models.TextField(db_column='_etblRevaluationHistory_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblRevaluationHistory'


class Etblsagebankfeedshistory(models.Model):
    idsagebankfeedshistory = models.AutoField(db_column='idSageBankFeedsHistory', primary_key=True)  # Field name made lowercase.
    iglbankaccid = models.IntegerField(db_column='iGLBankAccID', blank=True, null=True)  # Field name made lowercase.
    csbforganisationid = models.CharField(db_column='cSBFOrganisationID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csbfadminuser = models.CharField(db_column='cSBFAdminUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csbfcompanyid = models.CharField(db_column='cSBFCompanyID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csbfcompanyname = models.CharField(db_column='cSBFCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbfbankaccountid = models.CharField(db_column='cSBFBankAccountID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cbankaccountname = models.CharField(db_column='cBankAccountName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cconnordisconn = models.CharField(db_column='cConnOrDisconn', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dmodifieddate = models.DateTimeField(db_column='dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    field_etblsagebankfeedshistory_ibranchid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_dcreateddate = models.DateTimeField(db_column='_etblSageBankFeedsHistory_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_dmodifieddate = models.DateTimeField(db_column='_etblSageBankFeedsHistory_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_icreatedbranchid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_imodifiedbranchid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_icreatedagentid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_imodifiedagentid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_ichangesetid = models.IntegerField(db_column='_etblSageBankFeedsHistory_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagebankfeedshistory_checksum = models.TextField(db_column='_etblSageBankFeedsHistory_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSageBankFeedsHistory'


class Etblsagepaybanks(models.Model):
    sagepaybankid = models.AutoField(db_column='SagePayBankID', primary_key=True)  # Field name made lowercase.
    countrycode = models.SmallIntegerField(db_column='CountryCode', blank=True, null=True)  # Field name made lowercase.
    banknamedisplay = models.CharField(db_column='BankNameDisplay', max_length=100, blank=True, null=True)  # Field name made lowercase.
    banknamefile = models.CharField(db_column='BankNameFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblsagepaybanks_ibranchid = models.IntegerField(db_column='_etblSagePayBanks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_dcreateddate = models.DateTimeField(db_column='_etblSagePayBanks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_dmodifieddate = models.DateTimeField(db_column='_etblSagePayBanks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_icreatedbranchid = models.IntegerField(db_column='_etblSagePayBanks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_imodifiedbranchid = models.IntegerField(db_column='_etblSagePayBanks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_icreatedagentid = models.IntegerField(db_column='_etblSagePayBanks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_imodifiedagentid = models.IntegerField(db_column='_etblSagePayBanks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_ichangesetid = models.IntegerField(db_column='_etblSagePayBanks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaybanks_checksum = models.TextField(db_column='_etblSagePayBanks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSagePayBanks'


class Etblsagepayerrorcodes(models.Model):
    idsagepayerrorcode = models.AutoField(db_column='idSagePayErrorCode', primary_key=True)  # Field name made lowercase.
    iserviceid = models.IntegerField(db_column='iServiceID', blank=True, null=True)  # Field name made lowercase.
    iresponse = models.IntegerField(db_column='iResponse', blank=True, null=True)  # Field name made lowercase.
    bwebservicefailure = models.BooleanField(db_column='bWebServiceFailure', blank=True, null=True)  # Field name made lowercase.
    cresponse = models.CharField(db_column='cResponse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblsagepayerrorcodes_ibranchid = models.IntegerField(db_column='_etblSagePayErrorCodes_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_dcreateddate = models.DateTimeField(db_column='_etblSagePayErrorCodes_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_dmodifieddate = models.DateTimeField(db_column='_etblSagePayErrorCodes_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_icreatedbranchid = models.IntegerField(db_column='_etblSagePayErrorCodes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_imodifiedbranchid = models.IntegerField(db_column='_etblSagePayErrorCodes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_icreatedagentid = models.IntegerField(db_column='_etblSagePayErrorCodes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_imodifiedagentid = models.IntegerField(db_column='_etblSagePayErrorCodes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_ichangesetid = models.IntegerField(db_column='_etblSagePayErrorCodes_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayerrorcodes_checksum = models.TextField(db_column='_etblSagePayErrorCodes_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSagePayErrorCodes'


class Etblsagepaynow(models.Model):
    idsagepaynow = models.AutoField(db_column='idSagePayNow', primary_key=True)  # Field name made lowercase.
    invnumid = models.BigIntegerField(db_column='InvNumID')  # Field name made lowercase.
    uniquereference = models.CharField(db_column='UniqueReference', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankstatementref = models.CharField(db_column='BankStatementRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cardholdersemailaddress = models.CharField(db_column='CardHoldersEmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    extra1debtorsref = models.TextField(db_column='Extra1DebtorsRef', blank=True, null=True)  # Field name made lowercase.
    extra2 = models.TextField(db_column='Extra2', blank=True, null=True)  # Field name made lowercase.
    extra3 = models.TextField(db_column='Extra3', blank=True, null=True)  # Field name made lowercase.
    acceptdeclineurlparams = models.CharField(db_column='AcceptDeclineURLParams', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    paynowresponse = models.TextField(db_column='PayNowResponse', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_etblsagepaynow_ibranchid = models.IntegerField(db_column='_etblSagePayNow_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_dcreateddate = models.DateTimeField(db_column='_etblSagePayNow_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_dmodifieddate = models.DateTimeField(db_column='_etblSagePayNow_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_icreatedbranchid = models.IntegerField(db_column='_etblSagePayNow_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_imodifiedbranchid = models.IntegerField(db_column='_etblSagePayNow_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_icreatedagentid = models.IntegerField(db_column='_etblSagePayNow_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_imodifiedagentid = models.IntegerField(db_column='_etblSagePayNow_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_ichangesetid = models.IntegerField(db_column='_etblSagePayNow_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepaynow_checksum = models.TextField(db_column='_etblSagePayNow_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    doctype = models.IntegerField(db_column='DocType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblSagePayNow'


class Etblsagepayqueue(models.Model):
    idspqueue = models.AutoField(db_column='idSPQueue', primary_key=True)  # Field name made lowercase.
    iservice = models.IntegerField(db_column='iService', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cinstruction = models.CharField(db_column='cInstruction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    btestonly = models.BooleanField(db_column='bTestOnly', blank=True, null=True)  # Field name made lowercase.
    isubmissionstatus = models.IntegerField(db_column='iSubmissionStatus', blank=True, null=True)  # Field name made lowercase.
    iresponsestatus = models.IntegerField(db_column='iResponseStatus', blank=True, null=True)  # Field name made lowercase.
    dcreated = models.DateTimeField(db_column='dCreated', blank=True, null=True)  # Field name made lowercase.
    dlastpolled = models.DateTimeField(db_column='dLastPolled', blank=True, null=True)  # Field name made lowercase.
    ctoken = models.CharField(db_column='cToken', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbatchname = models.CharField(db_column='cBatchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbatchdata = models.TextField(db_column='cBatchData', blank=True, null=True)  # Field name made lowercase.
    irecordid = models.IntegerField(db_column='iRecordID', blank=True, null=True)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csubmissiondata = models.TextField(db_column='cSubmissionData', blank=True, null=True)  # Field name made lowercase.
    cresponsedata = models.TextField(db_column='cResponseData', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    field_etblsagepayqueue_ibranchid = models.IntegerField(db_column='_etblSagePayQueue_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_dcreateddate = models.DateTimeField(db_column='_etblSagePayQueue_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_dmodifieddate = models.DateTimeField(db_column='_etblSagePayQueue_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_icreatedbranchid = models.IntegerField(db_column='_etblSagePayQueue_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_imodifiedbranchid = models.IntegerField(db_column='_etblSagePayQueue_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_icreatedagentid = models.IntegerField(db_column='_etblSagePayQueue_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_imodifiedagentid = models.IntegerField(db_column='_etblSagePayQueue_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_ichangesetid = models.IntegerField(db_column='_etblSagePayQueue_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayqueue_checksum = models.TextField(db_column='_etblSagePayQueue_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSagePayQueue'


class Etblsagepayservicekeys(models.Model):
    idsagepayservicekey = models.AutoField(db_column='idSagePayServiceKey', primary_key=True)  # Field name made lowercase.
    iservicetype = models.IntegerField(db_column='iServiceType')  # Field name made lowercase.
    cservicekeyname = models.CharField(db_column='cServiceKeyName', max_length=50)  # Field name made lowercase.
    cservicedescription = models.CharField(db_column='cServiceDescription', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cservicekeyvalue = models.CharField(db_column='cServiceKeyValue', max_length=37, blank=True, null=True)  # Field name made lowercase.
    iconnectiontimeout = models.IntegerField(db_column='iConnectionTimeout', blank=True, null=True)  # Field name made lowercase.
    ireceivetimeout = models.IntegerField(db_column='iReceiveTimeout', blank=True, null=True)  # Field name made lowercase.
    isendtimeout = models.IntegerField(db_column='iSendTimeout', blank=True, null=True)  # Field name made lowercase.
    bisactive = models.BooleanField(db_column='bIsActive')  # Field name made lowercase.
    field_etblsagepayservicekeys_ibranchid = models.IntegerField(db_column='_etblSagePayServiceKeys_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_dcreateddate = models.DateTimeField(db_column='_etblSagePayServiceKeys_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_dmodifieddate = models.DateTimeField(db_column='_etblSagePayServiceKeys_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_icreatedbranchid = models.IntegerField(db_column='_etblSagePayServiceKeys_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_imodifiedbranchid = models.IntegerField(db_column='_etblSagePayServiceKeys_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_icreatedagentid = models.IntegerField(db_column='_etblSagePayServiceKeys_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_imodifiedagentid = models.IntegerField(db_column='_etblSagePayServiceKeys_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_ichangesetid = models.IntegerField(db_column='_etblSagePayServiceKeys_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsagepayservicekeys_checksum = models.TextField(db_column='_etblSagePayServiceKeys_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSagePayServiceKeys'


class Etblsettlementterms(models.Model):
    idsettlementterms = models.AutoField(db_column='idSettlementTerms', primary_key=True)  # Field name made lowercase.
    csettlementcode = models.CharField(db_column='cSettlementCode', max_length=20)  # Field name made lowercase.
    csettlementdescription = models.CharField(db_column='cSettlementDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipaymentmethod = models.IntegerField(db_column='iPaymentMethod', blank=True, null=True)  # Field name made lowercase.
    isettlementdays = models.IntegerField(db_column='iSettlementDays', blank=True, null=True)  # Field name made lowercase.
    fsettlementdisc = models.FloatField(db_column='fSettlementDisc')  # Field name made lowercase.
    cinvmessage = models.CharField(db_column='cInvMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_etblsettlementterms_ibranchid = models.IntegerField(db_column='_etblSettlementTerms_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_dcreateddate = models.DateTimeField(db_column='_etblSettlementTerms_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_dmodifieddate = models.DateTimeField(db_column='_etblSettlementTerms_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_icreatedbranchid = models.IntegerField(db_column='_etblSettlementTerms_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_imodifiedbranchid = models.IntegerField(db_column='_etblSettlementTerms_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_icreatedagentid = models.IntegerField(db_column='_etblSettlementTerms_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_imodifiedagentid = models.IntegerField(db_column='_etblSettlementTerms_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_ichangesetid = models.IntegerField(db_column='_etblSettlementTerms_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsettlementterms_checksum = models.TextField(db_column='_etblSettlementTerms_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSettlementTerms'


class Etblstockbinlocations(models.Model):
    idstockbinlocations = models.AutoField(db_column='idStockBinLocations', primary_key=True)  # Field name made lowercase.
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    whseid = models.IntegerField(db_column='WhseID')  # Field name made lowercase.
    binid = models.IntegerField(db_column='BinID')  # Field name made lowercase.
    minlevel = models.FloatField(db_column='MinLevel')  # Field name made lowercase.
    maxlevel = models.FloatField(db_column='MaxLevel')  # Field name made lowercase.
    field_etblstockbinlocations_ibranchid = models.IntegerField(db_column='_etblStockBinLocations_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_dcreateddate = models.DateTimeField(db_column='_etblStockBinLocations_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_dmodifieddate = models.DateTimeField(db_column='_etblStockBinLocations_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_icreatedbranchid = models.IntegerField(db_column='_etblStockBinLocations_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_imodifiedbranchid = models.IntegerField(db_column='_etblStockBinLocations_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_icreatedagentid = models.IntegerField(db_column='_etblStockBinLocations_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_imodifiedagentid = models.IntegerField(db_column='_etblStockBinLocations_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_ichangesetid = models.IntegerField(db_column='_etblStockBinLocations_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockbinlocations_checksum = models.TextField(db_column='_etblStockBinLocations_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblStockBinLocations'


class Etblstockcategories(models.Model):
    idstockcategories = models.AutoField(db_column='idStockCategories', primary_key=True)  # Field name made lowercase.
    ccategoryname = models.CharField(db_column='cCategoryName', max_length=30)  # Field name made lowercase.
    ccategorydescription = models.CharField(db_column='cCategoryDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblstockcategories_ibranchid = models.IntegerField(db_column='_etblStockCategories_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_dcreateddate = models.DateTimeField(db_column='_etblStockCategories_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_dmodifieddate = models.DateTimeField(db_column='_etblStockCategories_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_icreatedbranchid = models.IntegerField(db_column='_etblStockCategories_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_imodifiedbranchid = models.IntegerField(db_column='_etblStockCategories_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_icreatedagentid = models.IntegerField(db_column='_etblStockCategories_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_imodifiedagentid = models.IntegerField(db_column='_etblStockCategories_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_ichangesetid = models.IntegerField(db_column='_etblStockCategories_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcategories_checksum = models.TextField(db_column='_etblStockCategories_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblStockCategories'


class Etblstockcosts(models.Model):
    idstockcosts = models.BigAutoField(db_column='idStockCosts', primary_key=True)  # Field name made lowercase.
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    whseid = models.IntegerField(db_column='WhseID')  # Field name made lowercase.
    lotid = models.IntegerField(db_column='LotID')  # Field name made lowercase.
    averagecost = models.FloatField(db_column='AverageCost')  # Field name made lowercase.
    latestcost = models.FloatField(db_column='LatestCost')  # Field name made lowercase.
    lowestcost = models.FloatField(db_column='LowestCost')  # Field name made lowercase.
    highestcost = models.FloatField(db_column='HighestCost')  # Field name made lowercase.
    manualcost = models.FloatField(db_column='ManualCost')  # Field name made lowercase.
    lastgrvcost = models.FloatField(db_column='LastGRVCost')  # Field name made lowercase.
    field_etblstockcosts_ibranchid = models.IntegerField(db_column='_etblStockCosts_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_dcreateddate = models.DateTimeField(db_column='_etblStockCosts_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_dmodifieddate = models.DateTimeField(db_column='_etblStockCosts_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_icreatedbranchid = models.IntegerField(db_column='_etblStockCosts_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_imodifiedbranchid = models.IntegerField(db_column='_etblStockCosts_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_icreatedagentid = models.IntegerField(db_column='_etblStockCosts_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_imodifiedagentid = models.IntegerField(db_column='_etblStockCosts_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_ichangesetid = models.IntegerField(db_column='_etblStockCosts_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockcosts_checksum = models.TextField(db_column='_etblStockCosts_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblStockCosts'
        unique_together = (('stockid', 'whseid', 'lotid'),)


class Etblstockdetails(models.Model):
    idstockdetails = models.BigAutoField(db_column='idStockDetails', primary_key=True)  # Field name made lowercase.
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    whseid = models.IntegerField(db_column='WhseID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    buyingagentid = models.IntegerField(db_column='BuyingAgentID')  # Field name made lowercase.
    itemcategoryid = models.IntegerField(db_column='ItemCategoryID')  # Field name made lowercase.
    barcodeid = models.IntegerField(db_column='BarcodeID')  # Field name made lowercase.
    ttinvid = models.IntegerField(db_column='TTInvID')  # Field name made lowercase.
    ttcrnid = models.IntegerField(db_column='TTCrnID')  # Field name made lowercase.
    ttgrvid = models.IntegerField(db_column='TTGrvID')  # Field name made lowercase.
    ttrtsid = models.IntegerField(db_column='TTRtsID')  # Field name made lowercase.
    packcodeid = models.IntegerField(db_column='PackCodeID')  # Field name made lowercase.
    allownegstock = models.BooleanField(db_column='AllowNegStock')  # Field name made lowercase.
    reorderlevel = models.FloatField(db_column='ReorderLevel')  # Field name made lowercase.
    reorderqty = models.FloatField(db_column='ReorderQty')  # Field name made lowercase.
    minlevel = models.FloatField(db_column='MinLevel')  # Field name made lowercase.
    maxlevel = models.FloatField(db_column='MaxLevel')  # Field name made lowercase.
    leaddays = models.FloatField(db_column='LeadDays')  # Field name made lowercase.
    field_etblstockdetails_ibranchid = models.IntegerField(db_column='_etblStockDetails_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_dcreateddate = models.DateTimeField(db_column='_etblStockDetails_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_dmodifieddate = models.DateTimeField(db_column='_etblStockDetails_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_icreatedbranchid = models.IntegerField(db_column='_etblStockDetails_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_imodifiedbranchid = models.IntegerField(db_column='_etblStockDetails_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_icreatedagentid = models.IntegerField(db_column='_etblStockDetails_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_imodifiedagentid = models.IntegerField(db_column='_etblStockDetails_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_ichangesetid = models.IntegerField(db_column='_etblStockDetails_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockdetails_checksum = models.TextField(db_column='_etblStockDetails_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    idefaultsalesbinid = models.IntegerField(db_column='iDefaultSalesBinID', blank=True, null=True)  # Field name made lowercase.
    idefaultpurchasesbinid = models.IntegerField(db_column='iDefaultPurchasesBinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblStockDetails'
        unique_together = (('stockid', 'whseid'),)


class Etblstockqtys(models.Model):
    idstockqtys = models.BigAutoField(db_column='idStockQtys', primary_key=True)  # Field name made lowercase.
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    whseid = models.IntegerField(db_column='WhseID')  # Field name made lowercase.
    lotid = models.IntegerField(db_column='LotID')  # Field name made lowercase.
    binlocationid = models.IntegerField(db_column='BinLocationID')  # Field name made lowercase.
    qtyonhand = models.FloatField(db_column='QtyOnHand')  # Field name made lowercase.
    qtyonso = models.FloatField(db_column='QtyOnSO')  # Field name made lowercase.
    qtyonpo = models.FloatField(db_column='QtyOnPO')  # Field name made lowercase.
    qtyreserved = models.FloatField(db_column='QtyReserved')  # Field name made lowercase.
    qtytodeliver = models.FloatField(db_column='QtyToDeliver')  # Field name made lowercase.
    qtyjcwip = models.FloatField(db_column='QtyJCWIP')  # Field name made lowercase.
    qtymfpwip = models.FloatField(db_column='QtyMFPWIP')  # Field name made lowercase.
    qtyibttoissue = models.FloatField(db_column='QtyIBTToIssue')  # Field name made lowercase.
    qtyibttoreceive = models.FloatField(db_column='QtyIBTToReceive')  # Field name made lowercase.
    qtylastgrvcount = models.FloatField(db_column='QtyLastGrvCount')  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qtyibtissued = models.FloatField(db_column='QtyIBTIssued')  # Field name made lowercase.
    qtyibtreceived = models.FloatField(db_column='QtyIBTReceived')  # Field name made lowercase.
    field_etblstockqtys_ibranchid = models.IntegerField(db_column='_etblStockQtys_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_dcreateddate = models.DateTimeField(db_column='_etblStockQtys_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_dmodifieddate = models.DateTimeField(db_column='_etblStockQtys_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_icreatedbranchid = models.IntegerField(db_column='_etblStockQtys_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_imodifiedbranchid = models.IntegerField(db_column='_etblStockQtys_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_icreatedagentid = models.IntegerField(db_column='_etblStockQtys_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_imodifiedagentid = models.IntegerField(db_column='_etblStockQtys_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_ichangesetid = models.IntegerField(db_column='_etblStockQtys_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblstockqtys_checksum = models.TextField(db_column='_etblStockQtys_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblStockQtys'


class Etblsyncinfo(models.Model):
    idsyncinfo = models.AutoField(db_column='idSyncInfo', primary_key=True)  # Field name made lowercase.
    ireccount = models.BigIntegerField(db_column='iRecCount', blank=True, null=True)  # Field name made lowercase.
    ctablename = models.CharField(db_column='cTablename', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ibranchid = models.IntegerField(db_column='iBranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblSyncInfo'


class Etblsyncinfodetails(models.Model):
    idsyncinfodetails = models.BigAutoField(db_column='idSyncInfoDetails', primary_key=True)  # Field name made lowercase.
    isyncinfoid = models.IntegerField(db_column='iSyncInfoID', blank=True, null=True)  # Field name made lowercase.
    rowchecksum = models.TextField(db_column='rowChecksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSyncInfoDetails'


class Etblsystem(models.Model):
    idsystem = models.AutoField(db_column='idSystem', primary_key=True)  # Field name made lowercase.
    cidentity = models.CharField(db_column='cIdentity', max_length=35)  # Field name made lowercase.
    cvalue = models.CharField(db_column='cValue', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblSystem'


class Etblsystemdefaults(models.Model):
    idsystemdefaults = models.AutoField(db_column='idSystemDefaults', primary_key=True)  # Field name made lowercase.
    defaultaccess = models.CharField(db_column='DefaultAccess', max_length=5, blank=True, null=True)  # Field name made lowercase.
    security = models.CharField(db_column='Security', max_length=684, blank=True, null=True)  # Field name made lowercase.
    checkvalue = models.CharField(db_column='CheckValue', max_length=684, blank=True, null=True)  # Field name made lowercase.
    smartfilter = models.BooleanField(db_column='SmartFilter')  # Field name made lowercase.
    smtpaccount = models.CharField(db_column='SMTPAccount', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpauthenticate = models.BooleanField(db_column='SMTPAuthenticate')  # Field name made lowercase.
    smtpauthpass = models.CharField(db_column='SMTPAuthPass', max_length=684, blank=True, null=True)  # Field name made lowercase.
    smtpauthuser = models.CharField(db_column='SMTPAuthUser', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpfrom = models.CharField(db_column='SMTPFrom', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpname = models.CharField(db_column='SMTPName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtporg = models.CharField(db_column='SMTPOrg', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtppassword = models.CharField(db_column='SMTPPassword', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpport = models.IntegerField(db_column='SMTPPort', blank=True, null=True)  # Field name made lowercase.
    smtpreplyto = models.CharField(db_column='SMTPReplyTo', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpserver = models.CharField(db_column='SMTPServer', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smtpuseglobalfromaddr = models.BooleanField(db_column='SMTPUseGlobalFromAddr')  # Field name made lowercase.
    syncdatafolder = models.CharField(db_column='SyncDataFolder', max_length=256, blank=True, null=True)  # Field name made lowercase.
    syncdbserverdatafolder = models.CharField(db_column='SyncDBServerDataFolder', max_length=256, blank=True, null=True)  # Field name made lowercase.
    updatecheck = models.IntegerField(db_column='UpdateCheck', blank=True, null=True)  # Field name made lowercase.
    updatecheckinterval = models.IntegerField(db_column='UpdateCheckInterval', blank=True, null=True)  # Field name made lowercase.
    bicrepository = models.CharField(db_column='BICRepository', max_length=256, blank=True, null=True)  # Field name made lowercase.
    bicrptfinancialyear = models.IntegerField(db_column='BICRptFinancialYear', blank=True, null=True)  # Field name made lowercase.
    htmlroot = models.CharField(db_column='HtmlRoot', max_length=256, blank=True, null=True)  # Field name made lowercase.
    usesegmentedgl = models.BooleanField(db_column='UseSegmentedGL')  # Field name made lowercase.
    busetls = models.IntegerField(db_column='bUseTLS', blank=True, null=True)  # Field name made lowercase.
    bdisablertf = models.BooleanField(db_column='bDisableRTF')  # Field name made lowercase.
    busecom = models.BooleanField(db_column='bUseCOM', blank=True, null=True)  # Field name made lowercase.
    busemapi = models.BooleanField(db_column='bUseMapi')  # Field name made lowercase.
    csmtpbccaddresss = models.CharField(db_column='cSMTPBccAddresss', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bupdateglbalances = models.BooleanField(db_column='bUpdateGLBalances')  # Field name made lowercase.
    iglrelinkcheckinterval = models.IntegerField(db_column='iGLRelinkCheckInterval')  # Field name made lowercase.
    ipwrnumberchar = models.IntegerField(db_column='iPwrNumberChar')  # Field name made lowercase.
    ipwrletterchar = models.IntegerField(db_column='iPwrLetterChar')  # Field name made lowercase.
    ipwrsymbolchar = models.IntegerField(db_column='iPwrSymbolChar')  # Field name made lowercase.
    ipwruppercasechar = models.IntegerField(db_column='iPwrUppercaseChar')  # Field name made lowercase.
    ipwrlowercasechar = models.IntegerField(db_column='iPwrLowercaseChar')  # Field name made lowercase.
    ilockoutattempts = models.IntegerField(db_column='iLockOutAttempts')  # Field name made lowercase.
    ilockoutduration = models.IntegerField(db_column='iLockOutDuration')  # Field name made lowercase.
    bpwrcomplexity = models.BooleanField(db_column='bPwrComplexity')  # Field name made lowercase.
    benablelockout = models.BooleanField(db_column='bEnableLockOut')  # Field name made lowercase.
    cfreedomservice = models.CharField(db_column='cFreedomService', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cfailoverservice = models.CharField(db_column='cFailOverService', max_length=250, blank=True, null=True)  # Field name made lowercase.
    buselocalservice = models.BooleanField(db_column='bUseLocalService')  # Field name made lowercase.
    ifssessiontimeout = models.IntegerField(db_column='iFSSessionTimeOut')  # Field name made lowercase.
    bexceptiontrapping = models.BooleanField(db_column='bExceptionTrapping', blank=True, null=True)  # Field name made lowercase.
    field_etblsystemdefaults_ibranchid = models.IntegerField(db_column='_etblSystemDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_dcreateddate = models.DateTimeField(db_column='_etblSystemDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_dmodifieddate = models.DateTimeField(db_column='_etblSystemDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_icreatedbranchid = models.IntegerField(db_column='_etblSystemDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_imodifiedbranchid = models.IntegerField(db_column='_etblSystemDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_icreatedagentid = models.IntegerField(db_column='_etblSystemDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_imodifiedagentid = models.IntegerField(db_column='_etblSystemDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_ichangesetid = models.IntegerField(db_column='_etblSystemDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemdefaults_checksum = models.TextField(db_column='_etblSystemDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    buseoutgoingserversettings = models.BooleanField(db_column='bUseOutgoingServerSettings')  # Field name made lowercase.
    ismtpprovider = models.IntegerField(db_column='iSMTPProvider')  # Field name made lowercase.
    bappstatsdisabled = models.BooleanField(db_column='bAppStatsDisabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblSystemDefaults'


class Etblsystemupdate(models.Model):
    idsystemupdate = models.AutoField(db_column='idSystemUpdate', primary_key=True)  # Field name made lowercase.
    iupdate = models.IntegerField(db_column='iUpdate')  # Field name made lowercase.
    bforce = models.BooleanField(db_column='bForce')  # Field name made lowercase.
    field_etblsystemupdate_ibranchid = models.IntegerField(db_column='_etblSystemUpdate_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_dcreateddate = models.DateTimeField(db_column='_etblSystemUpdate_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_dmodifieddate = models.DateTimeField(db_column='_etblSystemUpdate_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_icreatedbranchid = models.IntegerField(db_column='_etblSystemUpdate_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_imodifiedbranchid = models.IntegerField(db_column='_etblSystemUpdate_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_icreatedagentid = models.IntegerField(db_column='_etblSystemUpdate_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_imodifiedagentid = models.IntegerField(db_column='_etblSystemUpdate_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_ichangesetid = models.IntegerField(db_column='_etblSystemUpdate_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblsystemupdate_checksum = models.TextField(db_column='_etblSystemUpdate_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblSystemUpdate'


class Etbltaxbaddebt(models.Model):
    itaxbaddebtid = models.AutoField(db_column='iTaxBadDebtID', primary_key=True)  # Field name made lowercase.
    iperiodid = models.IntegerField(db_column='iPeriodID', blank=True, null=True)  # Field name made lowercase.
    ipostar = models.IntegerField(db_column='iPostAR')  # Field name made lowercase.
    ipostap = models.IntegerField(db_column='iPostAP')  # Field name made lowercase.
    reliefamt = models.FloatField(db_column='ReliefAmt')  # Field name made lowercase.
    relieftaxamt = models.FloatField(db_column='ReliefTaxAmt')  # Field name made lowercase.
    recoveredamt = models.FloatField(db_column='RecoveredAmt')  # Field name made lowercase.
    recoveredtaxamt = models.FloatField(db_column='RecoveredTaxAmt')  # Field name made lowercase.
    refundamt = models.FloatField(db_column='RefundAmt')  # Field name made lowercase.
    refundtaxamt = models.FloatField(db_column='RefundTaxAmt')  # Field name made lowercase.
    reclaimamt = models.FloatField(db_column='ReclaimAmt')  # Field name made lowercase.
    reclaimtaxamt = models.FloatField(db_column='ReclaimTaxAmt')  # Field name made lowercase.
    auditnumber = models.CharField(db_column='AuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    txdate = models.DateTimeField(db_column='TxDate')  # Field name made lowercase.
    iprocessedtaxperiodid = models.IntegerField(db_column='iProcessedTaxPeriodID')  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID')  # Field name made lowercase.
    reliefamtforeign = models.FloatField(db_column='ReliefAmtForeign')  # Field name made lowercase.
    relieftaxamtforeign = models.FloatField(db_column='ReliefTaxAmtForeign')  # Field name made lowercase.
    recoveredamtforeign = models.FloatField(db_column='RecoveredAmtForeign')  # Field name made lowercase.
    recoveredtaxamtforeign = models.FloatField(db_column='RecoveredTaxAmtForeign')  # Field name made lowercase.
    refundamtforeign = models.FloatField(db_column='RefundAmtForeign')  # Field name made lowercase.
    refundtaxamtforeign = models.FloatField(db_column='RefundTaxAmtForeign')  # Field name made lowercase.
    reclaimamtforeign = models.FloatField(db_column='ReclaimAmtForeign')  # Field name made lowercase.
    reclaimtaxamtforeign = models.FloatField(db_column='ReclaimTaxAmtForeign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblTaxBadDebt'


class Etbltaxboxlayout(models.Model):
    idtaxboxlayout = models.AutoField(db_column='idTaxBoxLayout', primary_key=True)  # Field name made lowercase.
    itaxgroupid = models.IntegerField(db_column='iTaxGroupID', blank=True, null=True)  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID', blank=True, null=True)  # Field name made lowercase.
    itaxboxsetupid = models.IntegerField(db_column='iTaxBoxSetupID', blank=True, null=True)  # Field name made lowercase.
    field_etbltaxboxlayout_ibranchid = models.IntegerField(db_column='_etblTaxBoxLayout_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_dcreateddate = models.DateTimeField(db_column='_etblTaxBoxLayout_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_dmodifieddate = models.DateTimeField(db_column='_etblTaxBoxLayout_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_icreatedbranchid = models.IntegerField(db_column='_etblTaxBoxLayout_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_imodifiedbranchid = models.IntegerField(db_column='_etblTaxBoxLayout_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_icreatedagentid = models.IntegerField(db_column='_etblTaxBoxLayout_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_imodifiedagentid = models.IntegerField(db_column='_etblTaxBoxLayout_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_ichangesetid = models.IntegerField(db_column='_etblTaxBoxLayout_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxlayout_checksum = models.TextField(db_column='_etblTaxBoxLayout_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxBoxLayout'


class Etbltaxboxsetup(models.Model):
    idtaxboxsetup = models.AutoField(db_column='idTaxBoxSetup', primary_key=True)  # Field name made lowercase.
    iboxnumber = models.IntegerField(db_column='iBoxNumber')  # Field name made lowercase.
    cboxlabel = models.CharField(db_column='cBoxLabel', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cboxheading = models.CharField(db_column='cBoxHeading', max_length=256, blank=True, null=True)  # Field name made lowercase.
    cexamples = models.CharField(db_column='cExamples', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ivaluetypeid = models.IntegerField(db_column='iValueTypeID', blank=True, null=True)  # Field name made lowercase.
    ivalueid = models.IntegerField(db_column='iValueID', blank=True, null=True)  # Field name made lowercase.
    iroundingid = models.IntegerField(db_column='iRoundingID', blank=True, null=True)  # Field name made lowercase.
    field_etbltaxboxsetup_ibranchid = models.IntegerField(db_column='_etblTaxBoxSetup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_dcreateddate = models.DateTimeField(db_column='_etblTaxBoxSetup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_dmodifieddate = models.DateTimeField(db_column='_etblTaxBoxSetup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_icreatedbranchid = models.IntegerField(db_column='_etblTaxBoxSetup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_imodifiedbranchid = models.IntegerField(db_column='_etblTaxBoxSetup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_icreatedagentid = models.IntegerField(db_column='_etblTaxBoxSetup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_imodifiedagentid = models.IntegerField(db_column='_etblTaxBoxSetup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_ichangesetid = models.IntegerField(db_column='_etblTaxBoxSetup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxboxsetup_checksum = models.TextField(db_column='_etblTaxBoxSetup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxBoxSetup'


class Etbltaxcountry(models.Model):
    idtaxcountry = models.AutoField(db_column='idTaxCountry', primary_key=True)  # Field name made lowercase.
    ctaxcountrycode = models.CharField(db_column='cTaxCountryCode', max_length=20)  # Field name made lowercase.
    ctaxcountrydescription = models.CharField(db_column='cTaxCountryDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etbltaxcountry_ibranchid = models.IntegerField(db_column='_etblTaxCountry_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_dcreateddate = models.DateTimeField(db_column='_etblTaxCountry_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_dmodifieddate = models.DateTimeField(db_column='_etblTaxCountry_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_icreatedbranchid = models.IntegerField(db_column='_etblTaxCountry_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_imodifiedbranchid = models.IntegerField(db_column='_etblTaxCountry_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_icreatedagentid = models.IntegerField(db_column='_etblTaxCountry_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_imodifiedagentid = models.IntegerField(db_column='_etblTaxCountry_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_ichangesetid = models.IntegerField(db_column='_etblTaxCountry_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxcountry_checksum = models.TextField(db_column='_etblTaxCountry_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxCountry'


class Etbltaxdefaults(models.Model):
    idtaxdefaults = models.AutoField(db_column='idTaxDefaults', primary_key=True)  # Field name made lowercase.
    ctaxnumber = models.CharField(db_column='cTaxNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cregistration = models.CharField(db_column='cRegistration', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccustomscode = models.CharField(db_column='cCustomsCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    itaxdueledgeraccount = models.IntegerField(db_column='iTaxDueLedgerAccount', blank=True, null=True)  # Field name made lowercase.
    ipbtstartperiodid = models.IntegerField(db_column='iPBTStartPeriodID', blank=True, null=True)  # Field name made lowercase.
    bprincipalvendor = models.BooleanField(db_column='bPrincipalVendor', blank=True, null=True)  # Field name made lowercase.
    bvalidatetaxgroups = models.BooleanField(db_column='bValidateTaxGroups', blank=True, null=True)  # Field name made lowercase.
    ctaxcontactname = models.CharField(db_column='cTaxContactName', max_length=90, blank=True, null=True)  # Field name made lowercase.
    ctaxcontactsurname = models.CharField(db_column='cTaxContactSurname', max_length=53, blank=True, null=True)  # Field name made lowercase.
    ctaxcontacttelephone1 = models.CharField(db_column='cTaxContactTelephone1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ctaxcontacttelephone2 = models.CharField(db_column='cTaxContactTelephone2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ctaxcontactcellular = models.CharField(db_column='cTaxContactCellular', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ctaxcontactfax = models.CharField(db_column='cTaxContactFax', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ctaxcontactemail = models.CharField(db_column='cTaxContactEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bforceclienttaxidentification = models.BooleanField(db_column='bForceClientTaxIdentification', blank=True, null=True)  # Field name made lowercase.
    bforcesuppliertaxidentification = models.BooleanField(db_column='bForceSupplierTaxIdentification', blank=True, null=True)  # Field name made lowercase.
    bvalidateclienttaxidentification = models.BooleanField(db_column='bValidateClientTaxIdentification')  # Field name made lowercase.
    bvalidatesuppliertaxidentification = models.BooleanField(db_column='bValidateSupplierTaxIdentification')  # Field name made lowercase.
    bshowinactivetaxtypes = models.BooleanField(db_column='bShowInactiveTaxTypes')  # Field name made lowercase.
    bforcetaxdetails = models.BooleanField(db_column='bForceTaxDetails')  # Field name made lowercase.
    field_etbltaxdefaults_ibranchid = models.IntegerField(db_column='_etblTaxDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_dcreateddate = models.DateTimeField(db_column='_etblTaxDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_dmodifieddate = models.DateTimeField(db_column='_etblTaxDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_icreatedbranchid = models.IntegerField(db_column='_etblTaxDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_imodifiedbranchid = models.IntegerField(db_column='_etblTaxDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_icreatedagentid = models.IntegerField(db_column='_etblTaxDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_imodifiedagentid = models.IntegerField(db_column='_etblTaxDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_ichangesetid = models.IntegerField(db_column='_etblTaxDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxdefaults_checksum = models.TextField(db_column='_etblTaxDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    imajorindustrycodeid = models.IntegerField(db_column='iMajorIndustryCodeID', blank=True, null=True)  # Field name made lowercase.
    ibaddebtrecovered = models.IntegerField(db_column='iBadDebtRecovered')  # Field name made lowercase.
    ibaddebtrelief = models.IntegerField(db_column='iBadDebtRelief')  # Field name made lowercase.
    ibaddebtrefund = models.IntegerField(db_column='iBadDebtRefund')  # Field name made lowercase.
    ibaddebtreclaim = models.IntegerField(db_column='iBadDebtReclaim')  # Field name made lowercase.
    iidftaxcodeid = models.IntegerField(db_column='iIDFTaxCodeID')  # Field name made lowercase.
    iidftranstypeid = models.IntegerField(db_column='iIDFTransTypeID')  # Field name made lowercase.
    iidfforagenttaxcodeid = models.IntegerField(db_column='iIDFForAgentTaxCodeID')  # Field name made lowercase.
    bidfuseagent = models.BooleanField(db_column='bIDFUseAgent')  # Field name made lowercase.
    iimportservicesrptaxcodeid = models.IntegerField(db_column='iImportServiceSRPTaxCodeID')  # Field name made lowercase.
    iimportservicesrstaxcodeid = models.IntegerField(db_column='iImportServiceSRSTaxCodeID')  # Field name made lowercase.
    iprepaymenttaxledgerid = models.IntegerField(db_column='iPrepaymentTaxLedgerID')  # Field name made lowercase.
    iinputtaxcode = models.IntegerField(db_column='iInputTaxCode')  # Field name made lowercase.
    ioutputtaxcode = models.IntegerField(db_column='iOutputTaxCode')  # Field name made lowercase.
    itaxcountry = models.IntegerField(db_column='iTaxCountry')  # Field name made lowercase.
    itaxcloseperiodfrequency = models.IntegerField(db_column='iTaxClosePeriodFrequency')  # Field name made lowercase.
    itaxcloseperiodstartid = models.IntegerField(db_column='iTaxClosePeriodStartID')  # Field name made lowercase.
    brevenueintegration = models.BooleanField(db_column='bRevenueIntegration')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblTaxDefaults'


class Etbltaxgroup(models.Model):
    idtaxgroup = models.AutoField(db_column='idTaxGroup', primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=120, blank=True, null=True)  # Field name made lowercase.
    field_etbltaxgroup_ibranchid = models.IntegerField(db_column='_etblTaxGroup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_dcreateddate = models.DateTimeField(db_column='_etblTaxGroup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_dmodifieddate = models.DateTimeField(db_column='_etblTaxGroup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_icreatedbranchid = models.IntegerField(db_column='_etblTaxGroup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_imodifiedbranchid = models.IntegerField(db_column='_etblTaxGroup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_icreatedagentid = models.IntegerField(db_column='_etblTaxGroup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_imodifiedagentid = models.IntegerField(db_column='_etblTaxGroup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_ichangesetid = models.IntegerField(db_column='_etblTaxGroup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgroup_checksum = models.TextField(db_column='_etblTaxGroup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxGroup'


class Etbltaxgrouptranstype(models.Model):
    idtaxgrouptranstype = models.AutoField(db_column='idTaxGroupTransType', primary_key=True)  # Field name made lowercase.
    itaxgroupid = models.IntegerField(db_column='iTaxGroupID')  # Field name made lowercase.
    itranstypeid = models.IntegerField(db_column='iTransTypeID')  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=30, blank=True, null=True)  # Field name made lowercase.
    field_etbltaxgrouptranstype_ibranchid = models.IntegerField(db_column='_etblTaxGroupTransType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_dcreateddate = models.DateTimeField(db_column='_etblTaxGroupTransType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_dmodifieddate = models.DateTimeField(db_column='_etblTaxGroupTransType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_icreatedbranchid = models.IntegerField(db_column='_etblTaxGroupTransType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_imodifiedbranchid = models.IntegerField(db_column='_etblTaxGroupTransType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_icreatedagentid = models.IntegerField(db_column='_etblTaxGroupTransType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_imodifiedagentid = models.IntegerField(db_column='_etblTaxGroupTransType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_ichangesetid = models.IntegerField(db_column='_etblTaxGroupTransType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxgrouptranstype_checksum = models.TextField(db_column='_etblTaxGroupTransType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxGroupTransType'


class Etbltaxsubmissiondetails(models.Model):
    idtaxsubmissiondetails = models.AutoField(db_column='idTaxSubmissionDetails', primary_key=True)  # Field name made lowercase.
    ctaxcompanyname = models.CharField(db_column='cTaxCompanyName', max_length=150)  # Field name made lowercase.
    ctaxcompanyregistrationno = models.CharField(db_column='cTaxCompanyRegistrationNo', max_length=150)  # Field name made lowercase.
    ctaxregistrationno = models.CharField(db_column='cTaxRegistrationNo', max_length=150)  # Field name made lowercase.
    itaxglpostingid = models.BigIntegerField(db_column='iTaxGLPostingID')  # Field name made lowercase.
    field_etbltaxsubmissiondetails_ibranchid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_dcreateddate = models.DateTimeField(db_column='_etblTaxSubmissionDetails_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_dmodifieddate = models.DateTimeField(db_column='_etblTaxSubmissionDetails_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_icreatedbranchid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_imodifiedbranchid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_icreatedagentid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_imodifiedagentid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_ichangesetid = models.IntegerField(db_column='_etblTaxSubmissionDetails_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbltaxsubmissiondetails_checksum = models.TextField(db_column='_etblTaxSubmissionDetails_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTaxSubmissionDetails'


class Etblterms(models.Model):
    itermid = models.AutoField(db_column='iTermID', primary_key=True)  # Field name made lowercase.
    imodule = models.IntegerField(db_column='iModule')  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=20)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itermdescoption = models.IntegerField(db_column='iTermDescOption', blank=True, null=True)  # Field name made lowercase.
    ctermdesc1 = models.CharField(db_column='cTermDesc1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc2 = models.CharField(db_column='cTermDesc2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc3 = models.CharField(db_column='cTermDesc3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc4 = models.CharField(db_column='cTermDesc4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc5 = models.CharField(db_column='cTermDesc5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc6 = models.CharField(db_column='cTermDesc6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctermdesc7 = models.CharField(db_column='cTermDesc7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iagetypeoption = models.IntegerField(db_column='iAgeTypeOption', blank=True, null=True)  # Field name made lowercase.
    iintervaloption = models.IntegerField(db_column='iIntervalOption', blank=True, null=True)  # Field name made lowercase.
    iinterval1days = models.IntegerField(db_column='iInterval1Days', blank=True, null=True)  # Field name made lowercase.
    iinterval2days = models.IntegerField(db_column='iInterval2Days', blank=True, null=True)  # Field name made lowercase.
    iinterval3days = models.IntegerField(db_column='iInterval3Days', blank=True, null=True)  # Field name made lowercase.
    iinterval4days = models.IntegerField(db_column='iInterval4Days', blank=True, null=True)  # Field name made lowercase.
    iinterval5days = models.IntegerField(db_column='iInterval5Days', blank=True, null=True)  # Field name made lowercase.
    iinterval6days = models.IntegerField(db_column='iInterval6Days', blank=True, null=True)  # Field name made lowercase.
    iinterval7days = models.IntegerField(db_column='iInterval7Days', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate1 = models.DateTimeField(db_column='dStateCloseDate1', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate2 = models.DateTimeField(db_column='dStateCloseDate2', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate3 = models.DateTimeField(db_column='dStateCloseDate3', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate4 = models.DateTimeField(db_column='dStateCloseDate4', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate5 = models.DateTimeField(db_column='dStateCloseDate5', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate6 = models.DateTimeField(db_column='dStateCloseDate6', blank=True, null=True)  # Field name made lowercase.
    dstateclosedate7 = models.DateTimeField(db_column='dStateCloseDate7', blank=True, null=True)  # Field name made lowercase.
    bautosettoperiod = models.BooleanField(db_column='bAutoSetToPeriod')  # Field name made lowercase.
    cage1message1 = models.CharField(db_column='cAge1Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage1message2 = models.CharField(db_column='cAge1Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage2message1 = models.CharField(db_column='cAge2Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage2message2 = models.CharField(db_column='cAge2Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage3message1 = models.CharField(db_column='cAge3Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage3message2 = models.CharField(db_column='cAge3Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage4message1 = models.CharField(db_column='cAge4Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage4message2 = models.CharField(db_column='cAge4Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage5message1 = models.CharField(db_column='cAge5Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage5message2 = models.CharField(db_column='cAge5Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage6message1 = models.CharField(db_column='cAge6Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage6message2 = models.CharField(db_column='cAge6Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage7message1 = models.CharField(db_column='cAge7Message1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage7message2 = models.CharField(db_column='cAge7Message2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_etblterms_ibranchid = models.IntegerField(db_column='_etblTerms_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_dcreateddate = models.DateTimeField(db_column='_etblTerms_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_dmodifieddate = models.DateTimeField(db_column='_etblTerms_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_icreatedbranchid = models.IntegerField(db_column='_etblTerms_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_imodifiedbranchid = models.IntegerField(db_column='_etblTerms_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_icreatedagentid = models.IntegerField(db_column='_etblTerms_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_imodifiedagentid = models.IntegerField(db_column='_etblTerms_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_ichangesetid = models.IntegerField(db_column='_etblTerms_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblterms_checksum = models.TextField(db_column='_etblTerms_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblTerms'


class Etblunitcategory(models.Model):
    idunitcategory = models.AutoField(db_column='idUnitCategory', primary_key=True)  # Field name made lowercase.
    cunitcatdescription = models.CharField(db_column='cUnitCatDescription', max_length=20)  # Field name made lowercase.
    field_etblunitcategory_ibranchid = models.IntegerField(db_column='_etblUnitCategory_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_dcreateddate = models.DateTimeField(db_column='_etblUnitCategory_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_dmodifieddate = models.DateTimeField(db_column='_etblUnitCategory_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_icreatedbranchid = models.IntegerField(db_column='_etblUnitCategory_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_imodifiedbranchid = models.IntegerField(db_column='_etblUnitCategory_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_icreatedagentid = models.IntegerField(db_column='_etblUnitCategory_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_imodifiedagentid = models.IntegerField(db_column='_etblUnitCategory_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_ichangesetid = models.IntegerField(db_column='_etblUnitCategory_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitcategory_checksum = models.TextField(db_column='_etblUnitCategory_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblUnitCategory'


class Etblunitconversion(models.Model):
    idunitconversion = models.AutoField(db_column='idUnitConversion', primary_key=True)  # Field name made lowercase.
    iunitaid = models.IntegerField(db_column='iUnitAID')  # Field name made lowercase.
    funitaqty = models.FloatField(db_column='fUnitAQty')  # Field name made lowercase.
    iunitbid = models.IntegerField(db_column='iUnitBID')  # Field name made lowercase.
    funitbqty = models.FloatField(db_column='fUnitBQty')  # Field name made lowercase.
    fmarkup = models.FloatField(db_column='fMarkup', blank=True, null=True)  # Field name made lowercase.
    field_etblunitconversion_ibranchid = models.IntegerField(db_column='_etblUnitConversion_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_dcreateddate = models.DateTimeField(db_column='_etblUnitConversion_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_dmodifieddate = models.DateTimeField(db_column='_etblUnitConversion_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_icreatedbranchid = models.IntegerField(db_column='_etblUnitConversion_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_imodifiedbranchid = models.IntegerField(db_column='_etblUnitConversion_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_icreatedagentid = models.IntegerField(db_column='_etblUnitConversion_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_imodifiedagentid = models.IntegerField(db_column='_etblUnitConversion_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_ichangesetid = models.IntegerField(db_column='_etblUnitConversion_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunitconversion_checksum = models.TextField(db_column='_etblUnitConversion_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblUnitConversion'


class Etblunits(models.Model):
    idunits = models.AutoField(db_column='idUnits', primary_key=True)  # Field name made lowercase.
    cunitcode = models.CharField(db_column='cUnitCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cunitdescription = models.CharField(db_column='cUnitDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iunitcategoryid = models.IntegerField(db_column='iUnitCategoryID', blank=True, null=True)  # Field name made lowercase.
    bunitroundup = models.BooleanField(db_column='bUnitRoundUp')  # Field name made lowercase.
    field_etblunits_ibranchid = models.IntegerField(db_column='_etblUnits_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_dcreateddate = models.DateTimeField(db_column='_etblUnits_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_dmodifieddate = models.DateTimeField(db_column='_etblUnits_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_icreatedbranchid = models.IntegerField(db_column='_etblUnits_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_imodifiedbranchid = models.IntegerField(db_column='_etblUnits_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_icreatedagentid = models.IntegerField(db_column='_etblUnits_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_imodifiedagentid = models.IntegerField(db_column='_etblUnits_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_ichangesetid = models.IntegerField(db_column='_etblUnits_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblunits_checksum = models.TextField(db_column='_etblUnits_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblUnits'


class Etbluserhistlink(models.Model):
    iduserhistlink = models.BigAutoField(db_column='idUserHistLink', primary_key=True)  # Field name made lowercase.
    userdictid = models.IntegerField(db_column='UserDictID')  # Field name made lowercase.
    tableid = models.BigIntegerField(db_column='TableID', blank=True, null=True)  # Field name made lowercase.
    uservalue = models.CharField(db_column='UserValue', max_length=1024)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate')  # Field name made lowercase.
    field_etbluserhistlink_ibranchid = models.IntegerField(db_column='_etblUserHistLink_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_dcreateddate = models.DateTimeField(db_column='_etblUserHistLink_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_dmodifieddate = models.DateTimeField(db_column='_etblUserHistLink_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_icreatedbranchid = models.IntegerField(db_column='_etblUserHistLink_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_imodifiedbranchid = models.IntegerField(db_column='_etblUserHistLink_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_icreatedagentid = models.IntegerField(db_column='_etblUserHistLink_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_imodifiedagentid = models.IntegerField(db_column='_etblUserHistLink_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_ichangesetid = models.IntegerField(db_column='_etblUserHistLink_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etbluserhistlink_checksum = models.TextField(db_column='_etblUserHistLink_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblUserHistLink'
        unique_together = (('userdictid', 'tableid', 'lastmodifieddate'),)


class Etblvasairtimeitem(models.Model):
    idvasairtimeitem = models.AutoField(db_column='idVASAirtimeItem', primary_key=True)  # Field name made lowercase.
    idvasairtimemaster = models.IntegerField(db_column='idVASAirtimeMaster')  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink')  # Field name made lowercase.
    ddiscountpercentage = models.DecimalField(db_column='dDiscountPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    field_etblvasairtimeitem_ibranchid = models.IntegerField(db_column='_etblVASAirtimeItem_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_dcreateddate = models.DateTimeField(db_column='_etblVASAirtimeItem_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_dmodifieddate = models.DateTimeField(db_column='_etblVASAirtimeItem_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_icreatedbranchid = models.IntegerField(db_column='_etblVASAirtimeItem_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_imodifiedbranchid = models.IntegerField(db_column='_etblVASAirtimeItem_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_icreatedagentid = models.IntegerField(db_column='_etblVASAirtimeItem_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_imodifiedagentid = models.IntegerField(db_column='_etblVASAirtimeItem_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_ichangesetid = models.IntegerField(db_column='_etblVASAirtimeItem_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeitem_checksum = models.TextField(db_column='_etblVASAirtimeItem_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVASAirtimeItem'


class Etblvasairtimemaster(models.Model):
    idvasairtimemaster = models.AutoField(db_column='idVASAirtimeMaster', primary_key=True)  # Field name made lowercase.
    ccontractcode = models.CharField(db_column='cContractCode', max_length=20)  # Field name made lowercase.
    ccontractdescription = models.CharField(db_column='cContractDescription', max_length=100)  # Field name made lowercase.
    isetuptype = models.IntegerField(db_column='iSetupType')  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive', blank=True, null=True)  # Field name made lowercase.
    bdeleted = models.BooleanField(db_column='bDeleted', blank=True, null=True)  # Field name made lowercase.
    field_etblvasairtimemaster_ibranchid = models.IntegerField(db_column='_etblVASAirtimeMaster_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_dcreateddate = models.DateTimeField(db_column='_etblVASAirtimeMaster_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_dmodifieddate = models.DateTimeField(db_column='_etblVASAirtimeMaster_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_icreatedbranchid = models.IntegerField(db_column='_etblVASAirtimeMaster_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_imodifiedbranchid = models.IntegerField(db_column='_etblVASAirtimeMaster_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_icreatedagentid = models.IntegerField(db_column='_etblVASAirtimeMaster_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_imodifiedagentid = models.IntegerField(db_column='_etblVASAirtimeMaster_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_ichangesetid = models.IntegerField(db_column='_etblVASAirtimeMaster_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimemaster_checksum = models.TextField(db_column='_etblVASAirtimeMaster_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVASAirtimeMaster'


class Etblvasairtimenetwork(models.Model):
    idvasairtimenetwork = models.AutoField(db_column='idVASAirtimeNetwork', primary_key=True)  # Field name made lowercase.
    idvasairtimemaster = models.IntegerField(db_column='idVASAirtimeMaster')  # Field name made lowercase.
    cnetworkcode = models.CharField(db_column='cNetworkCode', max_length=20)  # Field name made lowercase.
    cnetworkname = models.CharField(db_column='cNetworkName', max_length=50)  # Field name made lowercase.
    cnetworkdescription = models.CharField(db_column='cNetworkDescription', max_length=100)  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink')  # Field name made lowercase.
    ddiscountpercentage = models.DecimalField(db_column='dDiscountPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    field_etblvasairtimenetwork_ibranchid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_dcreateddate = models.DateTimeField(db_column='_etblVASAirtimeNetwork_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_dmodifieddate = models.DateTimeField(db_column='_etblVASAirtimeNetwork_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_icreatedbranchid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_imodifiedbranchid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_icreatedagentid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_imodifiedagentid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_ichangesetid = models.IntegerField(db_column='_etblVASAirtimeNetwork_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimenetwork_checksum = models.TextField(db_column='_etblVASAirtimeNetwork_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVASAirtimeNetwork'


class Etblvasairtimeproduct(models.Model):
    idvasairtimeproduct = models.AutoField(db_column='idVASAirtimeProduct', primary_key=True)  # Field name made lowercase.
    idvasairtimenetwork = models.IntegerField(db_column='idVASAirtimeNetwork')  # Field name made lowercase.
    cproductcode = models.CharField(db_column='cProductCode', max_length=20)  # Field name made lowercase.
    cproductdescription = models.CharField(db_column='cProductDescription', max_length=100)  # Field name made lowercase.
    dproductprice = models.DecimalField(db_column='dProductPrice', max_digits=18, decimal_places=0)  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink')  # Field name made lowercase.
    ddiscountpercentage = models.DecimalField(db_column='dDiscountPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    field_etblvasairtimeproduct_ibranchid = models.IntegerField(db_column='_etblVASAirtimeProduct_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_dcreateddate = models.DateTimeField(db_column='_etblVASAirtimeProduct_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_dmodifieddate = models.DateTimeField(db_column='_etblVASAirtimeProduct_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_icreatedbranchid = models.IntegerField(db_column='_etblVASAirtimeProduct_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_imodifiedbranchid = models.IntegerField(db_column='_etblVASAirtimeProduct_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_icreatedagentid = models.IntegerField(db_column='_etblVASAirtimeProduct_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_imodifiedagentid = models.IntegerField(db_column='_etblVASAirtimeProduct_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_ichangesetid = models.IntegerField(db_column='_etblVASAirtimeProduct_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvasairtimeproduct_checksum = models.TextField(db_column='_etblVASAirtimeProduct_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVASAirtimeProduct'


class Etblvdap(models.Model):
    idvd = models.AutoField(db_column='IDVD', primary_key=True)  # Field name made lowercase.
    iarapid = models.IntegerField(db_column='iARAPID', blank=True, null=True)  # Field name made lowercase.
    igroupid = models.IntegerField(db_column='iGroupID', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    ccontractname = models.CharField(db_column='cContractName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bonhold = models.BooleanField(db_column='bOnHold')  # Field name made lowercase.
    tdescription = models.TextField(db_column='tDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    barapall = models.BooleanField(db_column='bARAPAll', blank=True, null=True)  # Field name made lowercase.
    bistemplate = models.BooleanField(db_column='bIsTemplate')  # Field name made lowercase.
    field_etblvdap_ibranchid = models.IntegerField(db_column='_etblVDAP_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_dcreateddate = models.DateTimeField(db_column='_etblVDAP_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_dmodifieddate = models.DateTimeField(db_column='_etblVDAP_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_icreatedbranchid = models.IntegerField(db_column='_etblVDAP_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_imodifiedbranchid = models.IntegerField(db_column='_etblVDAP_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_icreatedagentid = models.IntegerField(db_column='_etblVDAP_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_imodifiedagentid = models.IntegerField(db_column='_etblVDAP_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_ichangesetid = models.IntegerField(db_column='_etblVDAP_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdap_checksum = models.TextField(db_column='_etblVDAP_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVDAP'


class Etblvdar(models.Model):
    idvd = models.AutoField(db_column='IDVD', primary_key=True)  # Field name made lowercase.
    iarapid = models.IntegerField(db_column='iARAPID', blank=True, null=True)  # Field name made lowercase.
    igroupid = models.IntegerField(db_column='iGroupID', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    ccontractname = models.CharField(db_column='cContractName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bonhold = models.BooleanField(db_column='bOnHold')  # Field name made lowercase.
    tdescription = models.TextField(db_column='tDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    barapall = models.BooleanField(db_column='bARAPAll', blank=True, null=True)  # Field name made lowercase.
    bistemplate = models.BooleanField(db_column='bIsTemplate')  # Field name made lowercase.
    field_etblvdar_ibranchid = models.IntegerField(db_column='_etblVDAR_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_dcreateddate = models.DateTimeField(db_column='_etblVDAR_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_dmodifieddate = models.DateTimeField(db_column='_etblVDAR_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_icreatedbranchid = models.IntegerField(db_column='_etblVDAR_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_imodifiedbranchid = models.IntegerField(db_column='_etblVDAR_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_icreatedagentid = models.IntegerField(db_column='_etblVDAR_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_imodifiedagentid = models.IntegerField(db_column='_etblVDAR_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_ichangesetid = models.IntegerField(db_column='_etblVDAR_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdar_checksum = models.TextField(db_column='_etblVDAR_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVDAR'


class Etblvdlnap(models.Model):
    idvdln = models.AutoField(db_column='IDVDLn', primary_key=True)  # Field name made lowercase.
    ivdid = models.IntegerField(db_column='iVDID', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    istgroupid = models.IntegerField(db_column='iStGroupID', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    deffdate = models.DateTimeField(db_column='dEffDate', blank=True, null=True)  # Field name made lowercase.
    dexpdate = models.DateTimeField(db_column='dExpDate', blank=True, null=True)  # Field name made lowercase.
    busestockprc = models.BooleanField(db_column='bUseStockPrc')  # Field name made lowercase.
    centerinclexcl = models.CharField(db_column='cEnterInclExcl', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bincremental = models.BooleanField(db_column='bIncremental')  # Field name made lowercase.
    bstockall = models.BooleanField(db_column='bStockAll', blank=True, null=True)  # Field name made lowercase.
    field_etblvdlnap_ibranchid = models.IntegerField(db_column='_etblVDLnAP_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_dcreateddate = models.DateTimeField(db_column='_etblVDLnAP_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_dmodifieddate = models.DateTimeField(db_column='_etblVDLnAP_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_icreatedbranchid = models.IntegerField(db_column='_etblVDLnAP_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_imodifiedbranchid = models.IntegerField(db_column='_etblVDLnAP_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_icreatedagentid = models.IntegerField(db_column='_etblVDLnAP_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_imodifiedagentid = models.IntegerField(db_column='_etblVDLnAP_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_ichangesetid = models.IntegerField(db_column='_etblVDLnAP_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnap_checksum = models.TextField(db_column='_etblVDLnAP_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVDLnAP'


class Etblvdlnar(models.Model):
    idvdln = models.AutoField(db_column='IDVDLn', primary_key=True)  # Field name made lowercase.
    ivdid = models.IntegerField(db_column='iVDID', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    istgroupid = models.IntegerField(db_column='iStGroupID', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    deffdate = models.DateTimeField(db_column='dEffDate', blank=True, null=True)  # Field name made lowercase.
    dexpdate = models.DateTimeField(db_column='dExpDate', blank=True, null=True)  # Field name made lowercase.
    busestockprc = models.BooleanField(db_column='bUseStockPrc')  # Field name made lowercase.
    centerinclexcl = models.CharField(db_column='cEnterInclExcl', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bincremental = models.BooleanField(db_column='bIncremental')  # Field name made lowercase.
    bstockall = models.BooleanField(db_column='bStockAll', blank=True, null=True)  # Field name made lowercase.
    field_etblvdlnar_ibranchid = models.IntegerField(db_column='_etblVDLnAR_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_dcreateddate = models.DateTimeField(db_column='_etblVDLnAR_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_dmodifieddate = models.DateTimeField(db_column='_etblVDLnAR_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_icreatedbranchid = models.IntegerField(db_column='_etblVDLnAR_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_imodifiedbranchid = models.IntegerField(db_column='_etblVDLnAR_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_icreatedagentid = models.IntegerField(db_column='_etblVDLnAR_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_imodifiedagentid = models.IntegerField(db_column='_etblVDLnAR_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_ichangesetid = models.IntegerField(db_column='_etblVDLnAR_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnar_checksum = models.TextField(db_column='_etblVDLnAR_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblVDLnAR'


class Etblvdlnlvlap(models.Model):
    idvdlnlvl = models.AutoField(db_column='IDVDLnLvl', primary_key=True)  # Field name made lowercase.
    ivdlnid = models.IntegerField(db_column='iVDLnID', blank=True, null=True)  # Field name made lowercase.
    ilevel = models.IntegerField(db_column='iLevel', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    fpricedisc = models.FloatField(db_column='fPriceDisc', blank=True, null=True)  # Field name made lowercase.
    field_etblvdlnlvlap_ibranchid = models.IntegerField(db_column='_etblVDLnLvlAP_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_dcreateddate = models.DateTimeField(db_column='_etblVDLnLvlAP_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_dmodifieddate = models.DateTimeField(db_column='_etblVDLnLvlAP_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_icreatedbranchid = models.IntegerField(db_column='_etblVDLnLvlAP_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_imodifiedbranchid = models.IntegerField(db_column='_etblVDLnLvlAP_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_icreatedagentid = models.IntegerField(db_column='_etblVDLnLvlAP_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_imodifiedagentid = models.IntegerField(db_column='_etblVDLnLvlAP_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_ichangesetid = models.IntegerField(db_column='_etblVDLnLvlAP_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlap_checksum = models.TextField(db_column='_etblVDLnLvlAP_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ivduomid = models.IntegerField(db_column='iVDUOMID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblVDLnLvlAP'


class Etblvdlnlvlar(models.Model):
    idvdlnlvl = models.AutoField(db_column='IDVDLnLvl', primary_key=True)  # Field name made lowercase.
    ivdlnid = models.IntegerField(db_column='iVDLnID', blank=True, null=True)  # Field name made lowercase.
    ilevel = models.IntegerField(db_column='iLevel', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    fpricedisc = models.FloatField(db_column='fPriceDisc', blank=True, null=True)  # Field name made lowercase.
    field_etblvdlnlvlar_ibranchid = models.IntegerField(db_column='_etblVDLnLvlAR_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_dcreateddate = models.DateTimeField(db_column='_etblVDLnLvlAR_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_dmodifieddate = models.DateTimeField(db_column='_etblVDLnLvlAR_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_icreatedbranchid = models.IntegerField(db_column='_etblVDLnLvlAR_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_imodifiedbranchid = models.IntegerField(db_column='_etblVDLnLvlAR_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_icreatedagentid = models.IntegerField(db_column='_etblVDLnLvlAR_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_imodifiedagentid = models.IntegerField(db_column='_etblVDLnLvlAR_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_ichangesetid = models.IntegerField(db_column='_etblVDLnLvlAR_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblvdlnlvlar_checksum = models.TextField(db_column='_etblVDLnLvlAR_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ivduomid = models.IntegerField(db_column='iVDUOMID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblVDLnLvlAR'


class Etblwhdefaults(models.Model):
    idwhdefaults = models.AutoField(db_column='IDWhDefaults', primary_key=True)  # Field name made lowercase.
    bwhtfbatchautonum = models.BooleanField(db_column='bWhTfBatchAutoNum')  # Field name made lowercase.
    cwhtfbatchprefix = models.CharField(db_column='cWhTfBatchPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iwhtfbatchpadlength = models.IntegerField(db_column='iWhTfBatchPadLength', blank=True, null=True)  # Field name made lowercase.
    iwhtftrcodeid = models.IntegerField(db_column='iWhTfTrCodeID', blank=True, null=True)  # Field name made lowercase.
    bwhtfrefautonum = models.BooleanField(db_column='bWhTfRefAutoNum')  # Field name made lowercase.
    cwhtfrefprefix = models.CharField(db_column='cWhTfRefPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iwhtfrefpadlength = models.IntegerField(db_column='iWhTfRefPadLength', blank=True, null=True)  # Field name made lowercase.
    bibtnumautonum = models.BooleanField(db_column='bIBTNumAutoNum')  # Field name made lowercase.
    cibtnumprefix = models.CharField(db_column='cIBTNumPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iibtnumpadlength = models.IntegerField(db_column='iIBTNumPadLength', blank=True, null=True)  # Field name made lowercase.
    iibttrcodeid = models.IntegerField(db_column='iIBTTrCodeID', blank=True, null=True)  # Field name made lowercase.
    iibtaddcosttrcodeid = models.IntegerField(db_column='iIBTAddCostTrCodeID', blank=True, null=True)  # Field name made lowercase.
    bibtdelnoteautonum = models.BooleanField(db_column='bIBTDelNoteAutoNum')  # Field name made lowercase.
    cibtdelnoteprefix = models.CharField(db_column='cIBTDelNotePrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iibtdelnotepadlength = models.IntegerField(db_column='iIBTDelNotePadLength')  # Field name made lowercase.
    idefintransitwhid = models.IntegerField(db_column='iDefInTransitWHID', blank=True, null=True)  # Field name made lowercase.
    idefvariancewhid = models.IntegerField(db_column='iDefVarianceWHID', blank=True, null=True)  # Field name made lowercase.
    idefdamagedwhid = models.IntegerField(db_column='iDefDamagedWHID', blank=True, null=True)  # Field name made lowercase.
    bwhseibtactivated = models.BooleanField(db_column='bWhseIBTActivated')  # Field name made lowercase.
    bforceproject = models.BooleanField(db_column='bForceProject')  # Field name made lowercase.
    ibranchloanaccountid = models.IntegerField(db_column='iBranchLoanAccountID', blank=True, null=True)  # Field name made lowercase.
    bibtdefaultcosttoissue = models.BooleanField(db_column='bIBTDefaultCostToIssue')  # Field name made lowercase.
    bibtallowoverdelivery = models.BooleanField(db_column='bIBTAllowOverDelivery')  # Field name made lowercase.
    cibtrequestnumprefix = models.CharField(db_column='cIBTRequestNumPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iibtrequestnumpadlength = models.IntegerField(db_column='iIBTRequestNumPadLength', blank=True, null=True)  # Field name made lowercase.
    bibtrequestnumautonum = models.BooleanField(db_column='bIBTRequestNumAutoNum')  # Field name made lowercase.
    busemultibins = models.BooleanField(db_column='bUseMultiBins')  # Field name made lowercase.
    cbinseperator = models.CharField(db_column='cBinSeperator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    field_etblwhdefaults_ibranchid = models.IntegerField(db_column='_etblWhDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_dcreateddate = models.DateTimeField(db_column='_etblWhDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_dmodifieddate = models.DateTimeField(db_column='_etblWhDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_icreatedbranchid = models.IntegerField(db_column='_etblWhDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_imodifiedbranchid = models.IntegerField(db_column='_etblWhDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_icreatedagentid = models.IntegerField(db_column='_etblWhDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_imodifiedagentid = models.IntegerField(db_column='_etblWhDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_ichangesetid = models.IntegerField(db_column='_etblWhDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhdefaults_checksum = models.TextField(db_column='_etblWhDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    busebinlocationlevels = models.BooleanField(db_column='bUseBinLocationLevels')  # Field name made lowercase.
    bbintfbatchautonum = models.BooleanField(db_column='bBinTfBatchAutoNum')  # Field name made lowercase.
    cbintfbatchprefix = models.CharField(db_column='cBinTfBatchPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ibintfbatchpadlength = models.IntegerField(db_column='iBinTfBatchPadLength', blank=True, null=True)  # Field name made lowercase.
    ibintftrcodeid = models.IntegerField(db_column='iBinTfTrCodeID', blank=True, null=True)  # Field name made lowercase.
    bbintfrefautonum = models.BooleanField(db_column='bBinTfRefAutoNum')  # Field name made lowercase.
    cbintfrefprefix = models.CharField(db_column='cBinTfRefPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ibintfrefpadlength = models.IntegerField(db_column='iBinTfRefPadLength', blank=True, null=True)  # Field name made lowercase.
    bbintfforceproject = models.BooleanField(db_column='bBinTfForceProject')  # Field name made lowercase.
    bupdatetoitemcost = models.BooleanField(db_column='bUpdateToItemCost')  # Field name made lowercase.
    bibtonlysyncprocessed = models.BooleanField(db_column='bIBTOnlySyncProcessed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblWhDefaults'


class Etblwhseibt(models.Model):
    idwhseibt = models.AutoField(db_column='IDWhseIBT', primary_key=True)  # Field name made lowercase.
    cibtnumber = models.CharField(db_column='cIBTNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cibtdescription = models.CharField(db_column='cIBTDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    iwhseidfrom = models.IntegerField(db_column='iWhseIDFrom', blank=True, null=True)  # Field name made lowercase.
    iwhseidto = models.IntegerField(db_column='iWhseIDTo', blank=True, null=True)  # Field name made lowercase.
    iwhseidintransit = models.IntegerField(db_column='iWhseIDIntransit', blank=True, null=True)  # Field name made lowercase.
    iwhseidvariance = models.IntegerField(db_column='iWhseIDVariance', blank=True, null=True)  # Field name made lowercase.
    iwhseiddamaged = models.IntegerField(db_column='iWhseIDDamaged', blank=True, null=True)  # Field name made lowercase.
    iibtstatus = models.IntegerField(db_column='iIBTStatus', blank=True, null=True)  # Field name made lowercase.
    cdelnotenumber = models.CharField(db_column='cDelNoteNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    ddateissued = models.DateTimeField(db_column='dDateIssued', blank=True, null=True)  # Field name made lowercase.
    ddatereceived = models.DateTimeField(db_column='dDateReceived', blank=True, null=True)  # Field name made lowercase.
    cauditnumberissued = models.CharField(db_column='cAuditNumberIssued', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cauditnumberreceived = models.CharField(db_column='cAuditNumberReceived', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buseaddcostperline = models.BooleanField(db_column='bUseAddCostPerLine')  # Field name made lowercase.
    ffixedaddcost = models.FloatField(db_column='fFixedAddCost')  # Field name made lowercase.
    iagentidissue = models.IntegerField(db_column='iAgentIDIssue')  # Field name made lowercase.
    iagentidreceive = models.IntegerField(db_column='iAgentIDReceive')  # Field name made lowercase.
    ibranchidfrom = models.IntegerField(db_column='iBranchIDFrom', blank=True, null=True)  # Field name made lowercase.
    ddaterequired = models.DateTimeField(db_column='dDateRequired', blank=True, null=True)  # Field name made lowercase.
    ddaterequested = models.DateTimeField(db_column='dDateRequested', blank=True, null=True)  # Field name made lowercase.
    ddateapproved = models.DateTimeField(db_column='dDateApproved', blank=True, null=True)  # Field name made lowercase.
    ilinkedreqid = models.IntegerField(db_column='iLinkedReqID', blank=True, null=True)  # Field name made lowercase.
    iibtaction = models.IntegerField(db_column='iIBTAction', blank=True, null=True)  # Field name made lowercase.
    cibtreference1 = models.CharField(db_column='cIBTReference1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cibtreference2 = models.CharField(db_column='cIBTReference2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dactionissuestock = models.DateTimeField(db_column='dActionIssueStock', blank=True, null=True)  # Field name made lowercase.
    dactionshipstock = models.DateTimeField(db_column='dActionShipStock', blank=True, null=True)  # Field name made lowercase.
    dactionackstock = models.DateTimeField(db_column='dActionAckStock', blank=True, null=True)  # Field name made lowercase.
    dactionrecievestock = models.DateTimeField(db_column='dActionRecieveStock', blank=True, null=True)  # Field name made lowercase.
    bvariancecleared = models.BooleanField(db_column='bVarianceCleared')  # Field name made lowercase.
    field_etblwhseibt_ibranchid = models.IntegerField(db_column='_etblWhseIBT_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_dcreateddate = models.DateTimeField(db_column='_etblWhseIBT_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_dmodifieddate = models.DateTimeField(db_column='_etblWhseIBT_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_icreatedbranchid = models.IntegerField(db_column='_etblWhseIBT_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_imodifiedbranchid = models.IntegerField(db_column='_etblWhseIBT_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_icreatedagentid = models.IntegerField(db_column='_etblWhseIBT_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_imodifiedagentid = models.IntegerField(db_column='_etblWhseIBT_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_ichangesetid = models.IntegerField(db_column='_etblWhseIBT_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibt_checksum = models.TextField(db_column='_etblWhseIBT_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ulibtdriver = models.CharField(db_column='ulIBTDriver', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulibtvehiclemake = models.CharField(db_column='ulIBTVehicleMake', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulibtroutes = models.CharField(db_column='ulIBTRoutes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulibtvehiclecapacity = models.CharField(db_column='ulIBTVehicleCapacity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulibtloadingsequence = models.CharField(db_column='ulIBTLoadingSequence', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulibtdispatchtime = models.CharField(db_column='ulIBTDispatchTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ucibtclientaddress = models.CharField(db_column='ucIBTClientAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblWhseIBT'


class Etblwhseibtaddcosts(models.Model):
    idwhseibtaddcosts = models.AutoField(db_column='IDWhseIBTAddCosts', primary_key=True)  # Field name made lowercase.
    iwhseibtid = models.IntegerField(db_column='iWhseIBTID')  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID')  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    flinetotalexcl = models.FloatField(db_column='fLineTotalExcl')  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID')  # Field name made lowercase.
    flinetaxamount = models.FloatField(db_column='fLineTaxAmount')  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate')  # Field name made lowercase.
    flinetotalexclforeign = models.FloatField(db_column='fLineTotalExclForeign')  # Field name made lowercase.
    field_etblwhseibtaddcosts_ibranchid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_dcreateddate = models.DateTimeField(db_column='_etblWhseIBTAddCosts_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_dmodifieddate = models.DateTimeField(db_column='_etblWhseIBTAddCosts_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_icreatedbranchid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_imodifiedbranchid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_icreatedagentid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_imodifiedagentid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_ichangesetid = models.IntegerField(db_column='_etblWhseIBTAddCosts_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtaddcosts_checksum = models.TextField(db_column='_etblWhseIBTAddCosts_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblWhseIBTAddCosts'


class Etblwhseibtlinesn(models.Model):
    idwhseibtlinesn = models.BigAutoField(db_column='IDWhseIBTLineSN', primary_key=True)  # Field name made lowercase.
    iwhseibtid = models.IntegerField(db_column='iWhseIBTID', blank=True, null=True)  # Field name made lowercase.
    isngroupid = models.IntegerField(db_column='iSNGroupID', blank=True, null=True)  # Field name made lowercase.
    iserialmfid = models.IntegerField(db_column='iSerialMFID', blank=True, null=True)  # Field name made lowercase.
    field_etblwhseibtlinesn_ibranchid = models.IntegerField(db_column='_etblWhseIBTLineSN_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_dcreateddate = models.DateTimeField(db_column='_etblWhseIBTLineSN_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_dmodifieddate = models.DateTimeField(db_column='_etblWhseIBTLineSN_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_icreatedbranchid = models.IntegerField(db_column='_etblWhseIBTLineSN_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_imodifiedbranchid = models.IntegerField(db_column='_etblWhseIBTLineSN_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_icreatedagentid = models.IntegerField(db_column='_etblWhseIBTLineSN_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_imodifiedagentid = models.IntegerField(db_column='_etblWhseIBTLineSN_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_ichangesetid = models.IntegerField(db_column='_etblWhseIBTLineSN_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlinesn_checksum = models.TextField(db_column='_etblWhseIBTLineSN_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblWhseIBTLineSN'


class Etblwhseibtlines(models.Model):
    idwhseibtlines = models.BigAutoField(db_column='IDWhseIBTLines', primary_key=True)  # Field name made lowercase.
    iwhseibtid = models.IntegerField(db_column='iWhseIBTID', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem')  # Field name made lowercase.
    bislotitem = models.BooleanField(db_column='bIsLotItem')  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID', blank=True, null=True)  # Field name made lowercase.
    clotnumber = models.CharField(db_column='cLotNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dlotexpirydate = models.DateTimeField(db_column='dLotExpiryDate', blank=True, null=True)  # Field name made lowercase.
    fqtyissued = models.FloatField(db_column='fQtyIssued', blank=True, null=True)  # Field name made lowercase.
    fqtyreceived = models.FloatField(db_column='fQtyReceived', blank=True, null=True)  # Field name made lowercase.
    fqtydamaged = models.FloatField(db_column='fQtyDamaged', blank=True, null=True)  # Field name made lowercase.
    fqtyvariance = models.FloatField(db_column='fQtyVariance', blank=True, null=True)  # Field name made lowercase.
    fqtyoverdelivered = models.FloatField(db_column='fQtyOverDelivered')  # Field name made lowercase.
    fnewreceivecost = models.FloatField(db_column='fNewReceiveCost', blank=True, null=True)  # Field name made lowercase.
    isnissuedgroupid = models.IntegerField(db_column='iSNIssuedGroupID', blank=True, null=True)  # Field name made lowercase.
    isnreceivedgroupid = models.IntegerField(db_column='iSNReceivedGroupID', blank=True, null=True)  # Field name made lowercase.
    isndamagedgroupid = models.IntegerField(db_column='iSNDamagedGroupID', blank=True, null=True)  # Field name made lowercase.
    isnvariancegroupid = models.IntegerField(db_column='iSNVarianceGroupID', blank=True, null=True)  # Field name made lowercase.
    clinenotes = models.CharField(db_column='cLineNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    fadditionalcost = models.FloatField(db_column='fAdditionalCost')  # Field name made lowercase.
    fissuedcost = models.FloatField(db_column='fIssuedCost', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurestockingid = models.IntegerField(db_column='iUnitsOfMeasureStockingID', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurecategoryid = models.IntegerField(db_column='iUnitsOfMeasureCategoryID', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasureid = models.IntegerField(db_column='iUnitsOfMeasureID', blank=True, null=True)  # Field name made lowercase.
    fqtyrequired = models.FloatField(db_column='fQtyRequired')  # Field name made lowercase.
    fqtyapproved = models.FloatField(db_column='fQtyApproved')  # Field name made lowercase.
    ireqlinestatus = models.IntegerField(db_column='iReqLineStatus', blank=True, null=True)  # Field name made lowercase.
    xibtattribute = models.TextField(db_column='xIBTAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fqtyoverdamaged = models.FloatField(db_column='fQtyOverDamaged')  # Field name made lowercase.
    field_etblwhseibtlines_ibranchid = models.IntegerField(db_column='_etblWhseIBTLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_dcreateddate = models.DateTimeField(db_column='_etblWhseIBTLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_dmodifieddate = models.DateTimeField(db_column='_etblWhseIBTLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_icreatedbranchid = models.IntegerField(db_column='_etblWhseIBTLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_imodifiedbranchid = models.IntegerField(db_column='_etblWhseIBTLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_icreatedagentid = models.IntegerField(db_column='_etblWhseIBTLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_imodifiedagentid = models.IntegerField(db_column='_etblWhseIBTLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_ichangesetid = models.IntegerField(db_column='_etblWhseIBTLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhseibtlines_checksum = models.TextField(db_column='_etblWhseIBTLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    bclearlinevariance = models.BooleanField(db_column='bClearLineVariance')  # Field name made lowercase.
    ifromstockbinlocationid = models.IntegerField(db_column='iFromStockBinLocationID')  # Field name made lowercase.
    itostockbinlocationid = models.IntegerField(db_column='iToStockBinLocationID')  # Field name made lowercase.
    idamagestockbinlocationid = models.IntegerField(db_column='iDamageStockBinLocationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblWhseIBTLines'


class Etblwhsetransferbatchlines(models.Model):
    idwhsetransferbatchlines = models.AutoField(db_column='idWhseTransferBatchLines', primary_key=True)  # Field name made lowercase.
    iwhsetransferbatchid = models.IntegerField(db_column='iWhseTransferBatchID', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    ifromwhseid = models.IntegerField(db_column='iFromWhseID', blank=True, null=True)  # Field name made lowercase.
    itowhseid = models.IntegerField(db_column='iToWhseID', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    fcost = models.FloatField(db_column='fCost', blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem')  # Field name made lowercase.
    iserialnumbergroupid = models.IntegerField(db_column='iSerialNumberGroupID', blank=True, null=True)  # Field name made lowercase.
    bislotitem = models.BooleanField(db_column='bIsLotItem')  # Field name made lowercase.
    ilotid = models.IntegerField(db_column='iLotID')  # Field name made lowercase.
    clotnumber = models.CharField(db_column='cLotNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dlotexpirydate = models.DateTimeField(db_column='dLotExpiryDate', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    clinenotes = models.CharField(db_column='cLineNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurestockingid = models.IntegerField(db_column='iUnitsOfMeasureStockingID', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasurecategoryid = models.IntegerField(db_column='iUnitsOfMeasureCategoryID', blank=True, null=True)  # Field name made lowercase.
    iunitsofmeasureid = models.IntegerField(db_column='iUnitsOfMeasureID', blank=True, null=True)  # Field name made lowercase.
    xwtattribute = models.TextField(db_column='xWTAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_etblwhsetransferbatchlines_ibranchid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_dcreateddate = models.DateTimeField(db_column='_etblWhseTransferBatchLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_dmodifieddate = models.DateTimeField(db_column='_etblWhseTransferBatchLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_icreatedbranchid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_imodifiedbranchid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_icreatedagentid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_imodifiedagentid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_ichangesetid = models.IntegerField(db_column='_etblWhseTransferBatchLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatchlines_checksum = models.TextField(db_column='_etblWhseTransferBatchLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ifromstockbinlocationid = models.IntegerField(db_column='iFromStockBinLocationID')  # Field name made lowercase.
    itostockbinlocationid = models.IntegerField(db_column='iToStockBinLocationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_etblWhseTransferBatchLines'


class Etblwhsetransferbatches(models.Model):
    idwhsetransferbatch = models.AutoField(db_column='idWhseTransferBatch', primary_key=True)  # Field name made lowercase.
    cbatchno = models.CharField(db_column='cBatchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbatchdescription = models.CharField(db_column='cBatchDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    itrcodeid = models.IntegerField(db_column='iTrCodeID', blank=True, null=True)  # Field name made lowercase.
    icreateagentid = models.IntegerField(db_column='iCreateAgentID', blank=True, null=True)  # Field name made lowercase.
    bclearbatchafterpost = models.BooleanField(db_column='bClearBatchAfterPost')  # Field name made lowercase.
    ballowduplicateref = models.BooleanField(db_column='bAllowDuplicateRef')  # Field name made lowercase.
    bprintjournal = models.BooleanField(db_column='bPrintJournal')  # Field name made lowercase.
    inewlinerefopt = models.IntegerField(db_column='iNewLineRefOpt', blank=True, null=True)  # Field name made lowercase.
    cnewlinerefdef = models.CharField(db_column='cNewLineRefDef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bnewlinerefincr = models.BooleanField(db_column='bNewLineRefIncr')  # Field name made lowercase.
    inewlinedescopt = models.IntegerField(db_column='iNewLineDescOpt', blank=True, null=True)  # Field name made lowercase.
    cnewlinedescdef = models.CharField(db_column='cNewLineDescDef', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bnewlinedescincr = models.BooleanField(db_column='bNewLineDescIncr')  # Field name made lowercase.
    inewlinewhfromopt = models.IntegerField(db_column='iNewLineWHFromOpt', blank=True, null=True)  # Field name made lowercase.
    inewlinewhfromdefid = models.IntegerField(db_column='iNewLineWHFromDefID', blank=True, null=True)  # Field name made lowercase.
    inewlinewhtoopt = models.IntegerField(db_column='iNewLineWHToOpt', blank=True, null=True)  # Field name made lowercase.
    inewlinewhtodefid = models.IntegerField(db_column='iNewLineWHToDefID', blank=True, null=True)  # Field name made lowercase.
    inewlineprojectopt = models.IntegerField(db_column='iNewLineProjectOpt', blank=True, null=True)  # Field name made lowercase.
    inewlineprojectdefid = models.IntegerField(db_column='iNewLineProjectDefID', blank=True, null=True)  # Field name made lowercase.
    cbatchrefno = models.CharField(db_column='cBatchRefNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_etblwhsetransferbatches_ibranchid = models.IntegerField(db_column='_etblWhseTransferBatches_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_dcreateddate = models.DateTimeField(db_column='_etblWhseTransferBatches_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_dmodifieddate = models.DateTimeField(db_column='_etblWhseTransferBatches_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_icreatedbranchid = models.IntegerField(db_column='_etblWhseTransferBatches_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_imodifiedbranchid = models.IntegerField(db_column='_etblWhseTransferBatches_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_icreatedagentid = models.IntegerField(db_column='_etblWhseTransferBatches_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_imodifiedagentid = models.IntegerField(db_column='_etblWhseTransferBatches_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_ichangesetid = models.IntegerField(db_column='_etblWhseTransferBatches_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblwhsetransferbatches_checksum = models.TextField(db_column='_etblWhseTransferBatches_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblWhseTransferBatches'


class Etblworkers(models.Model):
    idworkers = models.AutoField(db_column='idWorkers', primary_key=True)  # Field name made lowercase.
    cworkercode = models.CharField(db_column='cWorkerCode', max_length=20)  # Field name made lowercase.
    cworkername = models.CharField(db_column='cWorkerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    fworkercost = models.FloatField(db_column='fWorkerCost', blank=True, null=True)  # Field name made lowercase.
    fbillablerate = models.FloatField(db_column='fBillableRate', blank=True, null=True)  # Field name made lowercase.
    field_etblworkers_ibranchid = models.IntegerField(db_column='_etblWorkers_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_dcreateddate = models.DateTimeField(db_column='_etblWorkers_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_dmodifieddate = models.DateTimeField(db_column='_etblWorkers_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_icreatedbranchid = models.IntegerField(db_column='_etblWorkers_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_imodifiedbranchid = models.IntegerField(db_column='_etblWorkers_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_icreatedagentid = models.IntegerField(db_column='_etblWorkers_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_imodifiedagentid = models.IntegerField(db_column='_etblWorkers_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_ichangesetid = models.IntegerField(db_column='_etblWorkers_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_etblworkers_checksum = models.TextField(db_column='_etblWorkers_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_etblWorkers'


class Iotbldefaults(models.Model):
    iddefaults = models.AutoField(db_column='IdDefaults', primary_key=True)  # Field name made lowercase.
    inextautonumib = models.IntegerField(db_column='iNextAutoNumIB')  # Field name made lowercase.
    ipadtoib = models.IntegerField(db_column='iPadToIB')  # Field name made lowercase.
    cprefixib = models.CharField(db_column='cPrefixIB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bautonumib = models.BooleanField(db_column='bAutoNumIB')  # Field name made lowercase.
    buniquenumib = models.BooleanField(db_column='bUniqueNumIB')  # Field name made lowercase.
    inextautonumibr = models.IntegerField(db_column='iNextAutoNumIBR')  # Field name made lowercase.
    ipadtoibr = models.IntegerField(db_column='iPadToIBR')  # Field name made lowercase.
    cprefixibr = models.CharField(db_column='cPrefixIBR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bautonumibr = models.BooleanField(db_column='bAutoNumIBR')  # Field name made lowercase.
    buniquenumibr = models.BooleanField(db_column='bUniqueNumIBR')  # Field name made lowercase.
    bautopo = models.BooleanField(db_column='bAutoPO')  # Field name made lowercase.
    ccategory1 = models.CharField(db_column='cCategory1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory2 = models.CharField(db_column='cCategory2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory3 = models.CharField(db_column='cCategory3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory4 = models.CharField(db_column='cCategory4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory5 = models.CharField(db_column='cCategory5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    binusecat1 = models.BooleanField(db_column='bInUseCat1', blank=True, null=True)  # Field name made lowercase.
    binusecat2 = models.BooleanField(db_column='bInUseCat2', blank=True, null=True)  # Field name made lowercase.
    binusecat3 = models.BooleanField(db_column='bInUseCat3', blank=True, null=True)  # Field name made lowercase.
    binusecat4 = models.BooleanField(db_column='bInUseCat4', blank=True, null=True)  # Field name made lowercase.
    binusecat5 = models.BooleanField(db_column='bInUseCat5', blank=True, null=True)  # Field name made lowercase.
    icat1from = models.IntegerField(db_column='iCat1From', blank=True, null=True)  # Field name made lowercase.
    icat1to = models.IntegerField(db_column='iCat1To', blank=True, null=True)  # Field name made lowercase.
    icat2from = models.IntegerField(db_column='iCat2From', blank=True, null=True)  # Field name made lowercase.
    icat2to = models.IntegerField(db_column='iCat2To', blank=True, null=True)  # Field name made lowercase.
    icat3from = models.IntegerField(db_column='iCat3From', blank=True, null=True)  # Field name made lowercase.
    icat3to = models.IntegerField(db_column='iCat3To', blank=True, null=True)  # Field name made lowercase.
    icat4from = models.IntegerField(db_column='iCat4From', blank=True, null=True)  # Field name made lowercase.
    icat4to = models.IntegerField(db_column='iCat4To', blank=True, null=True)  # Field name made lowercase.
    icat5from = models.IntegerField(db_column='iCat5From', blank=True, null=True)  # Field name made lowercase.
    icat5to = models.IntegerField(db_column='iCat5To', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat1 = models.FloatField(db_column='fNewReOrdLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat2 = models.FloatField(db_column='fNewReOrdLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat3 = models.FloatField(db_column='fNewReOrdLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat4 = models.FloatField(db_column='fNewReOrdLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat5 = models.FloatField(db_column='fNewReOrdLvlCat5', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat1 = models.FloatField(db_column='fNewReOrdQtyCat1', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat2 = models.FloatField(db_column='fNewReOrdQtyCat2', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat3 = models.FloatField(db_column='fNewReOrdQtyCat3', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat4 = models.FloatField(db_column='fNewReOrdQtyCat4', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat5 = models.FloatField(db_column='fNewReOrdQtyCat5', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat1 = models.FloatField(db_column='fNewMinLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat2 = models.FloatField(db_column='fNewMinLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat3 = models.FloatField(db_column='fNewMinLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat4 = models.FloatField(db_column='fNewMinLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat5 = models.FloatField(db_column='fNewMinLvlCat5', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat1 = models.FloatField(db_column='fNewMaxLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat2 = models.FloatField(db_column='fNewMaxLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat3 = models.FloatField(db_column='fNewMaxLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat4 = models.FloatField(db_column='fNewMaxLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat5 = models.FloatField(db_column='fNewMaxLvlCat5', blank=True, null=True)  # Field name made lowercase.
    iusagecalcrnd = models.IntegerField(db_column='iUsageCalcRnd', blank=True, null=True)  # Field name made lowercase.
    fusagecalcpercentage = models.FloatField(db_column='fUsageCalcPercentage', blank=True, null=True)  # Field name made lowercase.
    ilevelupdaternd = models.IntegerField(db_column='iLevelUpdateRnd', blank=True, null=True)  # Field name made lowercase.
    flevelupdatepercentage = models.FloatField(db_column='fLevelUpdatePercentage', blank=True, null=True)  # Field name made lowercase.
    busageperday = models.BooleanField(db_column='bUsagePerDay', blank=True, null=True)  # Field name made lowercase.
    fspikeper = models.FloatField(db_column='fSpikePer', blank=True, null=True)  # Field name made lowercase.
    cspikecolour = models.CharField(db_column='cSpikeColour', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iusageinterval = models.IntegerField(db_column='iUsageInterval', blank=True, null=True)  # Field name made lowercase.
    ilasttransdays = models.IntegerField(db_column='iLastTransDays', blank=True, null=True)  # Field name made lowercase.
    inextautonumtemp = models.IntegerField(db_column='iNextAutoNumTemp')  # Field name made lowercase.
    ipadtotemp = models.IntegerField(db_column='iPadToTemp')  # Field name made lowercase.
    cprefixtemp = models.CharField(db_column='cPrefixTemp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bautonumtemp = models.BooleanField(db_column='bAutoNumTemp')  # Field name made lowercase.
    buniquenumtemp = models.BooleanField(db_column='bUniqueNumTemp')  # Field name made lowercase.
    idecsellprice = models.IntegerField(db_column='iDecSellPrice', blank=True, null=True)  # Field name made lowercase.
    ideccostprice = models.IntegerField(db_column='iDecCostPrice', blank=True, null=True)  # Field name made lowercase.
    idecquantities = models.IntegerField(db_column='iDecQuantities', blank=True, null=True)  # Field name made lowercase.
    field_iotbldefaults_ibranchid = models.IntegerField(db_column='_iotblDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_dcreateddate = models.DateTimeField(db_column='_iotblDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_dmodifieddate = models.DateTimeField(db_column='_iotblDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_icreatedbranchid = models.IntegerField(db_column='_iotblDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_imodifiedbranchid = models.IntegerField(db_column='_iotblDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_icreatedagentid = models.IntegerField(db_column='_iotblDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_imodifiedagentid = models.IntegerField(db_column='_iotblDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_ichangesetid = models.IntegerField(db_column='_iotblDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbldefaults_checksum = models.TextField(db_column='_iotblDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_iotblDefaults'


class Iotblreorderbatch(models.Model):
    idreorderbatch = models.AutoField(db_column='idReorderBatch', primary_key=True)  # Field name made lowercase.
    cbatchnumber = models.CharField(db_column='cBatchNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbatchdate = models.DateTimeField(db_column='dBatchDate', blank=True, null=True)  # Field name made lowercase.
    itemplateid = models.IntegerField(db_column='iTemplateId')  # Field name made lowercase.
    barchived = models.BooleanField(db_column='bArchived', blank=True, null=True)  # Field name made lowercase.
    field_iotblreorderbatch_ibranchid = models.IntegerField(db_column='_iotblReorderBatch_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_dcreateddate = models.DateTimeField(db_column='_iotblReorderBatch_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_dmodifieddate = models.DateTimeField(db_column='_iotblReorderBatch_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_icreatedbranchid = models.IntegerField(db_column='_iotblReorderBatch_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_imodifiedbranchid = models.IntegerField(db_column='_iotblReorderBatch_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_icreatedagentid = models.IntegerField(db_column='_iotblReorderBatch_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_imodifiedagentid = models.IntegerField(db_column='_iotblReorderBatch_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_ichangesetid = models.IntegerField(db_column='_iotblReorderBatch_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatch_checksum = models.TextField(db_column='_iotblReorderBatch_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_iotblReorderBatch'


class Iotblreorderbatchlines(models.Model):
    ireorderbatchlineid = models.AutoField(db_column='iReorderBatchLineId', primary_key=True)  # Field name made lowercase.
    ireorderbatchid = models.IntegerField(db_column='iReorderBatchId')  # Field name made lowercase.
    binclude = models.BooleanField(db_column='bInclude', blank=True, null=True)  # Field name made lowercase.
    citemcode = models.CharField(db_column='cItemCode', max_length=400, blank=True, null=True)  # Field name made lowercase.
    citemdescription = models.CharField(db_column='cItemDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csalesorder = models.CharField(db_column='cSalesOrder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dsalesorderdate = models.DateTimeField(db_column='dSalesOrderDate', blank=True, null=True)  # Field name made lowercase.
    fsalesorderqty = models.FloatField(db_column='fSalesOrderQty', blank=True, null=True)  # Field name made lowercase.
    iusagewarehouseid = models.IntegerField(db_column='iUsageWarehouseId', blank=True, null=True)  # Field name made lowercase.
    ipowarehouseid = models.IntegerField(db_column='iPOWarehouseId', blank=True, null=True)  # Field name made lowercase.
    fusage = models.FloatField(db_column='fUsage', blank=True, null=True)  # Field name made lowercase.
    fusageperday = models.FloatField(db_column='fUsagePerDay', blank=True, null=True)  # Field name made lowercase.
    fqtyonhand = models.FloatField(db_column='fQtyOnHand', blank=True, null=True)  # Field name made lowercase.
    fqtyonstock = models.FloatField(db_column='fQtyOnStock', blank=True, null=True)  # Field name made lowercase.
    fqtyavailable = models.FloatField(db_column='fQtyAvailable', blank=True, null=True)  # Field name made lowercase.
    fqtyonpo = models.FloatField(db_column='fQtyOnPO', blank=True, null=True)  # Field name made lowercase.
    fqtyonso = models.FloatField(db_column='fQtyOnSO', blank=True, null=True)  # Field name made lowercase.
    fqtyreserved = models.FloatField(db_column='fQtyReserved', blank=True, null=True)  # Field name made lowercase.
    fqtyonjob = models.FloatField(db_column='fQtyOnJob', blank=True, null=True)  # Field name made lowercase.
    fqtymf = models.FloatField(db_column='fQtyMF', blank=True, null=True)  # Field name made lowercase.
    freorderlevel = models.FloatField(db_column='fReorderLevel', blank=True, null=True)  # Field name made lowercase.
    freorderqty = models.FloatField(db_column='fReorderQty', blank=True, null=True)  # Field name made lowercase.
    fminlevel = models.FloatField(db_column='fMinLevel', blank=True, null=True)  # Field name made lowercase.
    fmaxlevel = models.FloatField(db_column='fMaxLevel', blank=True, null=True)  # Field name made lowercase.
    ccostingmethod = models.CharField(db_column='cCostingMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faveragecost = models.FloatField(db_column='fAverageCost', blank=True, null=True)  # Field name made lowercase.
    flatestcost = models.FloatField(db_column='fLatestCost', blank=True, null=True)  # Field name made lowercase.
    fhighestcost = models.FloatField(db_column='fHighestCost', blank=True, null=True)  # Field name made lowercase.
    flowestcost = models.FloatField(db_column='fLowestCost', blank=True, null=True)  # Field name made lowercase.
    fmanualcost = models.FloatField(db_column='fManualCost', blank=True, null=True)  # Field name made lowercase.
    flastgrvcost = models.FloatField(db_column='fLastGRVCost', blank=True, null=True)  # Field name made lowercase.
    ipreferredsupplier = models.IntegerField(db_column='iPreferredSupplier', blank=True, null=True)  # Field name made lowercase.
    iposupplier = models.IntegerField(db_column='iPOSupplier', blank=True, null=True)  # Field name made lowercase.
    fleadtimeitem = models.FloatField(db_column='fLeadTimeItem', blank=True, null=True)  # Field name made lowercase.
    fleadtimedemanditem = models.FloatField(db_column='fLeadTimeDemandItem', blank=True, null=True)  # Field name made lowercase.
    fsupplierleadetime = models.FloatField(db_column='fSupplierLeadeTime', blank=True, null=True)  # Field name made lowercase.
    fleadtimedemandsupplier = models.FloatField(db_column='fLeadTimeDemandSupplier', blank=True, null=True)  # Field name made lowercase.
    fwarehouseleadtime = models.FloatField(db_column='fWarehouseLeadTime', blank=True, null=True)  # Field name made lowercase.
    fleadtimedemandwarehouse = models.FloatField(db_column='fLeadTimeDemandWarehouse', blank=True, null=True)  # Field name made lowercase.
    iproject = models.IntegerField(db_column='iProject', blank=True, null=True)  # Field name made lowercase.
    fsuggestedpoqty = models.FloatField(db_column='fSuggestedPOQty', blank=True, null=True)  # Field name made lowercase.
    fprice = models.FloatField(db_column='fPrice', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    fforeignprice = models.FloatField(db_column='fForeignPrice', blank=True, null=True)  # Field name made lowercase.
    flinetotal = models.FloatField(db_column='fLineTotal', blank=True, null=True)  # Field name made lowercase.
    cunit = models.CharField(db_column='cUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ideliverymethodid = models.IntegerField(db_column='iDeliveryMethodId', blank=True, null=True)  # Field name made lowercase.
    ipriorityid = models.IntegerField(db_column='iPriorityId', blank=True, null=True)  # Field name made lowercase.
    istatusid = models.IntegerField(db_column='iStatusId', blank=True, null=True)  # Field name made lowercase.
    corderdescription = models.CharField(db_column='cOrderDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink', blank=True, null=True)  # Field name made lowercase.
    iwhselink = models.IntegerField(db_column='iWhseLink', blank=True, null=True)  # Field name made lowercase.
    bprocessed = models.BooleanField(db_column='bProcessed', blank=True, null=True)  # Field name made lowercase.
    citemgroup = models.CharField(db_column='cItemGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cbinlocationname = models.CharField(db_column='cBinLocationName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cbarcode = models.CharField(db_column='cBarCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cdescription_3 = models.CharField(db_column='cDescription_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpack = models.CharField(db_column='cPack', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpackdescription = models.CharField(db_column='cPackDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fpacksize = models.FloatField(db_column='fPackSize', blank=True, null=True)  # Field name made lowercase.
    fnewreorderlevel = models.FloatField(db_column='fNewReorderLevel', blank=True, null=True)  # Field name made lowercase.
    fnewreorderqty = models.FloatField(db_column='fNewReorderQty', blank=True, null=True)  # Field name made lowercase.
    fnewminlevel = models.FloatField(db_column='fNewMinLevel', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlevel = models.FloatField(db_column='fNewMaxLevel', blank=True, null=True)  # Field name made lowercase.
    ccategory = models.CharField(db_column='cCategory', max_length=20, blank=True, null=True)  # Field name made lowercase.
    field_iotblreorderbatchlines_ibranchid = models.IntegerField(db_column='_iotblReorderBatchLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_dcreateddate = models.DateTimeField(db_column='_iotblReorderBatchLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_dmodifieddate = models.DateTimeField(db_column='_iotblReorderBatchLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_icreatedbranchid = models.IntegerField(db_column='_iotblReorderBatchLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_imodifiedbranchid = models.IntegerField(db_column='_iotblReorderBatchLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_icreatedagentid = models.IntegerField(db_column='_iotblReorderBatchLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_imodifiedagentid = models.IntegerField(db_column='_iotblReorderBatchLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_ichangesetid = models.IntegerField(db_column='_iotblReorderBatchLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblreorderbatchlines_checksum = models.TextField(db_column='_iotblReorderBatchLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_iotblReorderBatchLines'


class Iotblsystemstructure(models.Model):
    autoidx = models.IntegerField(db_column='AutoIdx', primary_key=True)  # Field name made lowercase.
    iparentid = models.IntegerField(db_column='iParentId', blank=True, null=True)  # Field name made lowercase.
    iimageindex = models.IntegerField(db_column='iImageIndex', blank=True, null=True)  # Field name made lowercase.
    cdisplaytext = models.CharField(db_column='cDisplayText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmodulename = models.CharField(db_column='cModuleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iorder = models.IntegerField(db_column='iOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_iotblSystemStructure'


class Iotbltemplatemaster(models.Model):
    idreordertemplate = models.AutoField(db_column='idReorderTemplate', primary_key=True)  # Field name made lowercase.
    ctempname = models.CharField(db_column='cTempName', max_length=50)  # Field name made lowercase.
    ctempdescription = models.CharField(db_column='cTempDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dtempdate = models.DateField(db_column='dTempDate', blank=True, null=True)  # Field name made lowercase.
    itransfromdays = models.IntegerField(db_column='iTransFromDays', blank=True, null=True)  # Field name made lowercase.
    ctranscodes = models.TextField(db_column='cTransCodes', blank=True, null=True)  # Field name made lowercase.
    ctranssource = models.TextField(db_column='cTransSource', blank=True, null=True)  # Field name made lowercase.
    iinvitemfromid = models.IntegerField(db_column='iInvItemFromId', blank=True, null=True)  # Field name made lowercase.
    iinvitemtoid = models.IntegerField(db_column='iInvItemToId', blank=True, null=True)  # Field name made lowercase.
    bignoreinactiveitem = models.BooleanField(db_column='bIgnoreInactiveItem', blank=True, null=True)  # Field name made lowercase.
    cinvgroups = models.TextField(db_column='cInvGroups', blank=True, null=True)  # Field name made lowercase.
    cinvpacks = models.TextField(db_column='cInvPacks', blank=True, null=True)  # Field name made lowercase.
    cinvbinlocations = models.TextField(db_column='cInvBinLocations', blank=True, null=True)  # Field name made lowercase.
    cinvwarehouses = models.TextField(db_column='cInvWarehouses', blank=True, null=True)  # Field name made lowercase.
    cinvfiltercriteria = models.TextField(db_column='cInvFilterCriteria', blank=True, null=True)  # Field name made lowercase.
    isonofromid = models.IntegerField(db_column='iSoNoFromId', blank=True, null=True)  # Field name made lowercase.
    isonotoid = models.IntegerField(db_column='iSoNoToId', blank=True, null=True)  # Field name made lowercase.
    csostatus = models.CharField(db_column='cSoStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsoignoreinactiveproject = models.BooleanField(db_column='bSoIgnoreInactiveProject', blank=True, null=True)  # Field name made lowercase.
    csoprojects = models.TextField(db_column='cSoProjects', blank=True, null=True)  # Field name made lowercase.
    csoforeigncurr = models.TextField(db_column='cSoForeignCurr', blank=True, null=True)  # Field name made lowercase.
    bsounconfirmed = models.BooleanField(db_column='bSoUnconfirmed', blank=True, null=True)  # Field name made lowercase.
    bsopartconfirmed = models.BooleanField(db_column='bSoPartConfirmed', blank=True, null=True)  # Field name made lowercase.
    bsomerged = models.BooleanField(db_column='bSoMerged', blank=True, null=True)  # Field name made lowercase.
    isofromdays = models.IntegerField(db_column='iSoFromDays', blank=True, null=True)  # Field name made lowercase.
    isofilterby = models.IntegerField(db_column='iSoFilterBy', blank=True, null=True)  # Field name made lowercase.
    ibomitemfromid = models.IntegerField(db_column='iBomItemFromId', blank=True, null=True)  # Field name made lowercase.
    ibomitemtoid = models.IntegerField(db_column='iBomItemToId', blank=True, null=True)  # Field name made lowercase.
    cbomreference = models.TextField(db_column='cBomReference', blank=True, null=True)  # Field name made lowercase.
    cbomextreference = models.TextField(db_column='cBomExtReference', blank=True, null=True)  # Field name made lowercase.
    ibomfromdays = models.IntegerField(db_column='iBomFromDays', blank=True, null=True)  # Field name made lowercase.
    cbomprojects = models.TextField(db_column='cBomProjects', blank=True, null=True)  # Field name made lowercase.
    cinvforecastformula = models.TextField(db_column='cInvForecastFormula', blank=True, null=True)  # Field name made lowercase.
    dpodate = models.DateField(db_column='dPoDate', blank=True, null=True)  # Field name made lowercase.
    cpodescription = models.CharField(db_column='cPoDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipodeliverymethodid = models.IntegerField(db_column='iPoDeliveryMethodId', blank=True, null=True)  # Field name made lowercase.
    ipostatusid = models.IntegerField(db_column='iPoStatusId', blank=True, null=True)  # Field name made lowercase.
    ipopriorityid = models.IntegerField(db_column='iPoPriorityId', blank=True, null=True)  # Field name made lowercase.
    ipoprojectid = models.IntegerField(db_column='iPoProjectId', blank=True, null=True)  # Field name made lowercase.
    ipowarehouseid = models.IntegerField(db_column='iPoWarehouseId', blank=True, null=True)  # Field name made lowercase.
    bincludepoqty = models.BooleanField(db_column='bIncludePOQty', blank=True, null=True)  # Field name made lowercase.
    bskipso = models.BooleanField(db_column='bSkipSO', blank=True, null=True)  # Field name made lowercase.
    isupplierfromid = models.IntegerField(db_column='iSupplierFromId', blank=True, null=True)  # Field name made lowercase.
    isuppliertoid = models.IntegerField(db_column='iSupplierToId', blank=True, null=True)  # Field name made lowercase.
    bignoreonholdsuppacc = models.BooleanField(db_column='bIgnoreOnHoldSuppAcc', blank=True, null=True)  # Field name made lowercase.
    csuppgroups = models.TextField(db_column='cSuppGroups', blank=True, null=True)  # Field name made lowercase.
    csuppareas = models.TextField(db_column='cSuppAreas', blank=True, null=True)  # Field name made lowercase.
    bignorebomcompitem = models.BooleanField(db_column='bIgnoreBOMCompItem', blank=True, null=True)  # Field name made lowercase.
    bincludezerousageitem = models.BooleanField(db_column='bIncludeZeroUsageItem')  # Field name made lowercase.
    cinvitemfrom = models.CharField(db_column='cInvItemFrom', max_length=400, blank=True, null=True)  # Field name made lowercase.
    cinvitemto = models.CharField(db_column='cInvItemTo', max_length=400, blank=True, null=True)  # Field name made lowercase.
    cbomitemfrom = models.CharField(db_column='cBomItemFrom', max_length=400, blank=True, null=True)  # Field name made lowercase.
    cbomitemto = models.CharField(db_column='cBomItemTo', max_length=400, blank=True, null=True)  # Field name made lowercase.
    csupplierfrom = models.CharField(db_column='cSupplierFrom', max_length=400, blank=True, null=True)  # Field name made lowercase.
    csupplierto = models.CharField(db_column='cSupplierTo', max_length=400, blank=True, null=True)  # Field name made lowercase.
    busedforreorder = models.BooleanField(db_column='bUsedForReorder', blank=True, null=True)  # Field name made lowercase.
    ccategory1 = models.CharField(db_column='cCategory1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory2 = models.CharField(db_column='cCategory2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory3 = models.CharField(db_column='cCategory3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory4 = models.CharField(db_column='cCategory4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ccategory5 = models.CharField(db_column='cCategory5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    icat1from = models.IntegerField(db_column='iCat1From', blank=True, null=True)  # Field name made lowercase.
    icat1to = models.IntegerField(db_column='iCat1To', blank=True, null=True)  # Field name made lowercase.
    icat2from = models.IntegerField(db_column='iCat2From', blank=True, null=True)  # Field name made lowercase.
    icat2to = models.IntegerField(db_column='iCat2To', blank=True, null=True)  # Field name made lowercase.
    icat3from = models.IntegerField(db_column='iCat3From', blank=True, null=True)  # Field name made lowercase.
    icat3to = models.IntegerField(db_column='iCat3To', blank=True, null=True)  # Field name made lowercase.
    icat4from = models.IntegerField(db_column='iCat4From', blank=True, null=True)  # Field name made lowercase.
    icat4to = models.IntegerField(db_column='iCat4To', blank=True, null=True)  # Field name made lowercase.
    icat5from = models.IntegerField(db_column='iCat5From', blank=True, null=True)  # Field name made lowercase.
    icat5to = models.IntegerField(db_column='iCat5To', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat1 = models.FloatField(db_column='fNewReOrdLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat2 = models.FloatField(db_column='fNewReOrdLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat3 = models.FloatField(db_column='fNewReOrdLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat4 = models.FloatField(db_column='fNewReOrdLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewreordlvlcat5 = models.FloatField(db_column='fNewReOrdLvlCat5', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat1 = models.FloatField(db_column='fNewReOrdQtyCat1', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat2 = models.FloatField(db_column='fNewReOrdQtyCat2', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat3 = models.FloatField(db_column='fNewReOrdQtyCat3', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat4 = models.FloatField(db_column='fNewReOrdQtyCat4', blank=True, null=True)  # Field name made lowercase.
    fnewreordqtycat5 = models.FloatField(db_column='fNewReOrdQtyCat5', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat1 = models.FloatField(db_column='fNewMinLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat2 = models.FloatField(db_column='fNewMinLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat3 = models.FloatField(db_column='fNewMinLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat4 = models.FloatField(db_column='fNewMinLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewminlvlcat5 = models.FloatField(db_column='fNewMinLvlCat5', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat1 = models.FloatField(db_column='fNewMaxLvlCat1', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat2 = models.FloatField(db_column='fNewMaxLvlCat2', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat3 = models.FloatField(db_column='fNewMaxLvlCat3', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat4 = models.FloatField(db_column='fNewMaxLvlCat4', blank=True, null=True)  # Field name made lowercase.
    fnewmaxlvlcat5 = models.FloatField(db_column='fNewMaxLvlCat5', blank=True, null=True)  # Field name made lowercase.
    dtransdatefrom = models.DateTimeField(db_column='dTransDateFrom', blank=True, null=True)  # Field name made lowercase.
    dtransdateto = models.DateTimeField(db_column='dTransDateTo', blank=True, null=True)  # Field name made lowercase.
    busageperday = models.BooleanField(db_column='bUsagePerDay', blank=True, null=True)  # Field name made lowercase.
    dcreateddate = models.DateTimeField(db_column='dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    dmodifieddate = models.DateTimeField(db_column='dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    icreatedagentid = models.IntegerField(db_column='iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    imodifiedagentid = models.IntegerField(db_column='iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    field_iotbltemplatemaster_ibranchid = models.IntegerField(db_column='_iotblTemplateMaster_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_dcreateddate = models.DateTimeField(db_column='_iotblTemplateMaster_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_dmodifieddate = models.DateTimeField(db_column='_iotblTemplateMaster_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_icreatedbranchid = models.IntegerField(db_column='_iotblTemplateMaster_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_imodifiedbranchid = models.IntegerField(db_column='_iotblTemplateMaster_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_icreatedagentid = models.IntegerField(db_column='_iotblTemplateMaster_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_imodifiedagentid = models.IntegerField(db_column='_iotblTemplateMaster_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_ichangesetid = models.IntegerField(db_column='_iotblTemplateMaster_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotbltemplatemaster_checksum = models.TextField(db_column='_iotblTemplateMaster_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_iotblTemplateMaster'


class Iotblworkgrp(models.Model):
    iworkgrpid = models.AutoField(db_column='iWorkGrpId', primary_key=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grplist = models.TextField(db_column='GrpList', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    irecordtype = models.IntegerField(db_column='iRecordType', blank=True, null=True)  # Field name made lowercase.
    field_iotblworkgrp_ibranchid = models.IntegerField(db_column='_iotblWorkGrp_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_dcreateddate = models.DateTimeField(db_column='_iotblWorkGrp_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_dmodifieddate = models.DateTimeField(db_column='_iotblWorkGrp_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_icreatedbranchid = models.IntegerField(db_column='_iotblWorkGrp_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_imodifiedbranchid = models.IntegerField(db_column='_iotblWorkGrp_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_icreatedagentid = models.IntegerField(db_column='_iotblWorkGrp_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_imodifiedagentid = models.IntegerField(db_column='_iotblWorkGrp_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_ichangesetid = models.IntegerField(db_column='_iotblWorkGrp_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_iotblworkgrp_checksum = models.TextField(db_column='_iotblWorkGrp_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_iotblWorkGrp'


class Mtblmbrcategories(models.Model):
    idmbrcategories = models.AutoField(db_column='idMBRCategories', primary_key=True)  # Field name made lowercase.
    cmbrcategory = models.CharField(db_column='cMBRCategory', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cmbrdescription = models.CharField(db_column='cMBRDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imbrtype = models.IntegerField(db_column='iMBRType', blank=True, null=True)  # Field name made lowercase.
    imbrcategorylinkid = models.IntegerField(db_column='iMBRCategoryLinkID', blank=True, null=True)  # Field name made lowercase.
    field_mtblmbrcategories_ibranchid = models.IntegerField(db_column='_mtblMBRCategories_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_dcreateddate = models.DateTimeField(db_column='_mtblMBRCategories_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_dmodifieddate = models.DateTimeField(db_column='_mtblMBRCategories_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_icreatedbranchid = models.IntegerField(db_column='_mtblMBRCategories_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_imodifiedbranchid = models.IntegerField(db_column='_mtblMBRCategories_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_icreatedagentid = models.IntegerField(db_column='_mtblMBRCategories_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_imodifiedagentid = models.IntegerField(db_column='_mtblMBRCategories_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_ichangesetid = models.IntegerField(db_column='_mtblMBRCategories_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_mtblmbrcategories_checksum = models.TextField(db_column='_mtblMBRCategories_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_mtblMBRCategories'


class Retagentsession(models.Model):
    idagentsession = models.AutoField(db_column='idAgentSession', primary_key=True)  # Field name made lowercase.
    itradingsessionid = models.IntegerField(db_column='iTradingSessionID', blank=True, null=True)  # Field name made lowercase.
    bistillsession = models.BooleanField(db_column='bIsTillSession')  # Field name made lowercase.
    itillsessionid = models.IntegerField(db_column='iTillSessionID', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    itillid = models.IntegerField(db_column='iTillID', blank=True, null=True)  # Field name made lowercase.
    fagentfloat = models.FloatField(db_column='fAgentFloat', blank=True, null=True)  # Field name made lowercase.
    dcurrentdate = models.DateTimeField(db_column='dCurrentDate', blank=True, null=True)  # Field name made lowercase.
    bcashedup = models.BooleanField(db_column='bCashedUp', blank=True, null=True)  # Field name made lowercase.
    ccashupreference = models.CharField(db_column='cCashUpReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dcashupdate = models.DateTimeField(db_column='dCashUpDate', blank=True, null=True)  # Field name made lowercase.
    icashuptillid = models.IntegerField(db_column='iCashUpTillID', blank=True, null=True)  # Field name made lowercase.
    bcashupfinalised = models.BooleanField(db_column='bCashUpFinalised')  # Field name made lowercase.
    ifinaliseagentid = models.IntegerField(db_column='iFinaliseAgentID', blank=True, null=True)  # Field name made lowercase.
    dfinaliseddate = models.DateTimeField(db_column='dFinalisedDate', blank=True, null=True)  # Field name made lowercase.
    fagentfloatcounted = models.FloatField(db_column='fAgentFloatCounted', blank=True, null=True)  # Field name made lowercase.
    fagentfloatfinalised = models.FloatField(db_column='fAgentFloatFinalised', blank=True, null=True)  # Field name made lowercase.
    ifloatinitialiseagentid = models.IntegerField(db_column='iFloatInitialiseAgentID', blank=True, null=True)  # Field name made lowercase.
    icashupagentid = models.IntegerField(db_column='iCashUpAgentID', blank=True, null=True)  # Field name made lowercase.
    field_retagentsession_ibranchid = models.IntegerField(db_column='_retAgentSession_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_dcreateddate = models.DateTimeField(db_column='_retAgentSession_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_dmodifieddate = models.DateTimeField(db_column='_retAgentSession_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_icreatedbranchid = models.IntegerField(db_column='_retAgentSession_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_imodifiedbranchid = models.IntegerField(db_column='_retAgentSession_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_icreatedagentid = models.IntegerField(db_column='_retAgentSession_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_imodifiedagentid = models.IntegerField(db_column='_retAgentSession_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_ichangesetid = models.IntegerField(db_column='_retAgentSession_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsession_checksum = models.TextField(db_column='_retAgentSession_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retAgentSession'


class Retagentsessioncashpickuptotals(models.Model):
    idagentsessioncashpickuptotals = models.AutoField(db_column='idAgentSessionCashPickupTotals', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    fcashpickuptotalsystem = models.FloatField(db_column='fCashPickupTotalSystem', blank=True, null=True)  # Field name made lowercase.
    fcashpickuptotalcounted = models.FloatField(db_column='fCashPickupTotalCounted', blank=True, null=True)  # Field name made lowercase.
    fcashpickuptotalfinalised = models.FloatField(db_column='fCashPickupTotalFinalised', blank=True, null=True)  # Field name made lowercase.
    field_retagentsessioncashpickuptotals_ibranchid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_dcreateddate = models.DateTimeField(db_column='_retAgentSessionCashPickupTotals_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_dmodifieddate = models.DateTimeField(db_column='_retAgentSessionCashPickupTotals_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_icreatedbranchid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_imodifiedbranchid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_icreatedagentid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_imodifiedagentid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_ichangesetid = models.IntegerField(db_column='_retAgentSessionCashPickupTotals_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessioncashpickuptotals_checksum = models.TextField(db_column='_retAgentSessionCashPickupTotals_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retAgentSessionCashPickupTotals'


class Retagentsessiondenomination(models.Model):
    idagentsessiondenomination = models.AutoField(db_column='idAgentSessionDenomination', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    idenominationid = models.IntegerField(db_column='iDenominationID', blank=True, null=True)  # Field name made lowercase.
    ifloatcount = models.IntegerField(db_column='iFloatCount', blank=True, null=True)  # Field name made lowercase.
    icashcount = models.IntegerField(db_column='iCashCount', blank=True, null=True)  # Field name made lowercase.
    ifloatcountfinalised = models.IntegerField(db_column='iFloatCountFinalised', blank=True, null=True)  # Field name made lowercase.
    icashcountfinalised = models.IntegerField(db_column='iCashCountFinalised', blank=True, null=True)  # Field name made lowercase.
    field_retagentsessiondenomination_ibranchid = models.IntegerField(db_column='_retAgentSessionDenomination_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_dcreateddate = models.DateTimeField(db_column='_retAgentSessionDenomination_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_dmodifieddate = models.DateTimeField(db_column='_retAgentSessionDenomination_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_icreatedbranchid = models.IntegerField(db_column='_retAgentSessionDenomination_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_imodifiedbranchid = models.IntegerField(db_column='_retAgentSessionDenomination_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_icreatedagentid = models.IntegerField(db_column='_retAgentSessionDenomination_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_imodifiedagentid = models.IntegerField(db_column='_retAgentSessionDenomination_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_ichangesetid = models.IntegerField(db_column='_retAgentSessionDenomination_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiondenomination_checksum = models.TextField(db_column='_retAgentSessionDenomination_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ffloatcountfinalisedforeign = models.FloatField(db_column='fFloatCountFinalisedForeign')  # Field name made lowercase.
    fcashcountfinalised = models.FloatField(db_column='fCashCountFinalised')  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retAgentSessionDenomination'


class Retagentsessionforeign(models.Model):
    idagentsessionforeign = models.BigAutoField(db_column='idAgentSessionForeign', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.BigIntegerField(db_column='iAgentSessionID')  # Field name made lowercase.
    fagentfloatforeign = models.FloatField(db_column='fAgentFloatForeign', blank=True, null=True)  # Field name made lowercase.
    fagentfloathome = models.FloatField(db_column='fAgentFloatHome', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    field_retagentsessionforeign_ibranchid = models.IntegerField(db_column='_retAgentSessionForeign_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_dcreateddate = models.DateTimeField(db_column='_retAgentSessionForeign_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_dmodifieddate = models.DateTimeField(db_column='_retAgentSessionForeign_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_icreatedbranchid = models.IntegerField(db_column='_retAgentSessionForeign_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_imodifiedbranchid = models.IntegerField(db_column='_retAgentSessionForeign_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_icreatedagentid = models.IntegerField(db_column='_retAgentSessionForeign_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_imodifiedagentid = models.IntegerField(db_column='_retAgentSessionForeign_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_ichangesetid = models.IntegerField(db_column='_retAgentSessionForeign_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionforeign_checksum = models.TextField(db_column='_retAgentSessionForeign_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    fagentfloatcountedforeign = models.FloatField(db_column='fAgentFloatCountedForeign')  # Field name made lowercase.
    fagentfloatfinalisedforeign = models.FloatField(db_column='fAgentFloatFinalisedForeign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retAgentSessionForeign'


class Retagentsessionpettycashtotals(models.Model):
    idagentsessionpettycashtotals = models.AutoField(db_column='idAgentSessionPettyCashTotals', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    fadvancedtotalsystem = models.FloatField(db_column='fAdvancedTotalSystem', blank=True, null=True)  # Field name made lowercase.
    fadvancedtotalcounted = models.FloatField(db_column='fAdvancedTotalCounted', blank=True, null=True)  # Field name made lowercase.
    fadvancedtotalfinalised = models.FloatField(db_column='fAdvancedTotalFinalised', blank=True, null=True)  # Field name made lowercase.
    fchangetotalsystem = models.FloatField(db_column='fChangeTotalSystem', blank=True, null=True)  # Field name made lowercase.
    fchangetotalcounted = models.FloatField(db_column='fChangeTotalCounted', blank=True, null=True)  # Field name made lowercase.
    fchangetotalfinalised = models.FloatField(db_column='fChangeTotalFinalised', blank=True, null=True)  # Field name made lowercase.
    field_retagentsessionpettycashtotals_ibranchid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_dcreateddate = models.DateTimeField(db_column='_retAgentSessionPettyCashTotals_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_dmodifieddate = models.DateTimeField(db_column='_retAgentSessionPettyCashTotals_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_icreatedbranchid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_imodifiedbranchid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_icreatedagentid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_imodifiedagentid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_ichangesetid = models.IntegerField(db_column='_retAgentSessionPettyCashTotals_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessionpettycashtotals_checksum = models.TextField(db_column='_retAgentSessionPettyCashTotals_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retAgentSessionPettyCashTotals'


class Retagentsessiontendertotals(models.Model):
    idagentsessiontendertotals = models.AutoField(db_column='idAgentSessionTenderTotals', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    itendertypeid = models.IntegerField(db_column='iTenderTypeID', blank=True, null=True)  # Field name made lowercase.
    bcashtendertype = models.BooleanField(db_column='bCashTenderType')  # Field name made lowercase.
    itendercount = models.IntegerField(db_column='iTenderCount', blank=True, null=True)  # Field name made lowercase.
    ftenderamountsystem = models.FloatField(db_column='fTenderAmountSystem', blank=True, null=True)  # Field name made lowercase.
    ftenderamountadjusted = models.FloatField(db_column='fTenderAmountAdjusted', blank=True, null=True)  # Field name made lowercase.
    ftenderamountcounted = models.FloatField(db_column='fTenderAmountCounted', blank=True, null=True)  # Field name made lowercase.
    ftenderamountfinalised = models.FloatField(db_column='fTenderAmountFinalised', blank=True, null=True)  # Field name made lowercase.
    field_retagentsessiontendertotals_ibranchid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_dcreateddate = models.DateTimeField(db_column='_retAgentSessionTenderTotals_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_dmodifieddate = models.DateTimeField(db_column='_retAgentSessionTenderTotals_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_icreatedbranchid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_imodifiedbranchid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_icreatedagentid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_imodifiedagentid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_ichangesetid = models.IntegerField(db_column='_retAgentSessionTenderTotals_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retagentsessiontendertotals_checksum = models.TextField(db_column='_retAgentSessionTenderTotals_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    icurrencyid = models.IntegerField(db_column='iCurrencyID')  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retAgentSessionTenderTotals'


class Retcashpickup(models.Model):
    idcashpickup = models.AutoField(db_column='idCashPickup', primary_key=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    itillid = models.IntegerField(db_column='iTillID', blank=True, null=True)  # Field name made lowercase.
    dpickupdate = models.DateTimeField(db_column='dPickupDate', blank=True, null=True)  # Field name made lowercase.
    ccashpickupreference = models.CharField(db_column='cCashPickupReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_retcashpickup_ibranchid = models.IntegerField(db_column='_retCashPickup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_dcreateddate = models.DateTimeField(db_column='_retCashPickup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_dmodifieddate = models.DateTimeField(db_column='_retCashPickup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_icreatedbranchid = models.IntegerField(db_column='_retCashPickup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_imodifiedbranchid = models.IntegerField(db_column='_retCashPickup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_icreatedagentid = models.IntegerField(db_column='_retCashPickup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_imodifiedagentid = models.IntegerField(db_column='_retCashPickup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_ichangesetid = models.IntegerField(db_column='_retCashPickup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickup_checksum = models.TextField(db_column='_retCashPickup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retCashPickup'


class Retcashpickupcurrency(models.Model):
    idcashpickupcurrency = models.AutoField(db_column='idCashPickupCurrency', primary_key=True)  # Field name made lowercase.
    icashpickupid = models.IntegerField(db_column='iCashPickupID')  # Field name made lowercase.
    fpickupamount = models.FloatField(db_column='fPickupAmount', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    field_retcashpickupcurrency_ibranchid = models.IntegerField(db_column='_retCashPickupCurrency_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_dcreateddate = models.DateTimeField(db_column='_retCashPickupCurrency_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_dmodifieddate = models.DateTimeField(db_column='_retCashPickupCurrency_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_icreatedbranchid = models.IntegerField(db_column='_retCashPickupCurrency_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_imodifiedbranchid = models.IntegerField(db_column='_retCashPickupCurrency_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_icreatedagentid = models.IntegerField(db_column='_retCashPickupCurrency_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_imodifiedagentid = models.IntegerField(db_column='_retCashPickupCurrency_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_ichangesetid = models.IntegerField(db_column='_retCashPickupCurrency_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupcurrency_checksum = models.TextField(db_column='_retCashPickupCurrency_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retCashPickupCurrency'


class Retcashpickupdenomination(models.Model):
    idcashpickupdenomination = models.AutoField(db_column='idCashPickupDenomination', primary_key=True)  # Field name made lowercase.
    icashpickupid = models.IntegerField(db_column='iCashPickupID', blank=True, null=True)  # Field name made lowercase.
    idenominationid = models.IntegerField(db_column='iDenominationID', blank=True, null=True)  # Field name made lowercase.
    icashcount = models.IntegerField(db_column='iCashCount', blank=True, null=True)  # Field name made lowercase.
    field_retcashpickupdenomination_ibranchid = models.IntegerField(db_column='_retCashPickupDenomination_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_dcreateddate = models.DateTimeField(db_column='_retCashPickupDenomination_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_dmodifieddate = models.DateTimeField(db_column='_retCashPickupDenomination_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_icreatedbranchid = models.IntegerField(db_column='_retCashPickupDenomination_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_imodifiedbranchid = models.IntegerField(db_column='_retCashPickupDenomination_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_icreatedagentid = models.IntegerField(db_column='_retCashPickupDenomination_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_imodifiedagentid = models.IntegerField(db_column='_retCashPickupDenomination_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_ichangesetid = models.IntegerField(db_column='_retCashPickupDenomination_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retcashpickupdenomination_checksum = models.TextField(db_column='_retCashPickupDenomination_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    icashpickupcurrencyid = models.IntegerField(db_column='iCashPickupCurrencyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retCashPickupDenomination'


class Retdefaults(models.Model):
    idretaildefaults = models.AutoField(db_column='idRetailDefaults', primary_key=True)  # Field name made lowercase.
    fdefaultfloatamount = models.FloatField(db_column='fDefaultFloatAmount', blank=True, null=True)  # Field name made lowercase.
    fdefaultcashpickupamount = models.FloatField(db_column='fDefaultCashPickupAmount', blank=True, null=True)  # Field name made lowercase.
    idefaultcustomerid = models.IntegerField(db_column='iDefaultCustomerID', blank=True, null=True)  # Field name made lowercase.
    imodelcustomerid = models.IntegerField(db_column='iModelCustomerID', blank=True, null=True)  # Field name made lowercase.
    cautonumbranchprefix = models.CharField(db_column='cAutoNumBranchPrefix', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idockettrcodeid = models.IntegerField(db_column='iDocketTrCodeID', blank=True, null=True)  # Field name made lowercase.
    idocketadjtrcodeid = models.IntegerField(db_column='iDocketAdjTrCodeID', blank=True, null=True)  # Field name made lowercase.
    icashupbanktrcodeid = models.IntegerField(db_column='iCashUpBankTrCodeID', blank=True, null=True)  # Field name made lowercase.
    icashupexcesstrcodeid = models.IntegerField(db_column='iCashUpExcessTrCodeID', blank=True, null=True)  # Field name made lowercase.
    icashupshortagetrcodeid = models.IntegerField(db_column='iCashUpShortageTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ipettycashadvancedtrcodeid = models.IntegerField(db_column='iPettyCashAdvancedTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ipettycashprocessedtrcodeid = models.IntegerField(db_column='iPettyCashProcessedTrCodeID', blank=True, null=True)  # Field name made lowercase.
    cpoledisplaydef1 = models.CharField(db_column='cPoleDisplayDef1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpoledisplaydef2 = models.CharField(db_column='cPoleDisplayDef2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ireceiptdiscounttrcodeid = models.IntegerField(db_column='iReceiptDiscountTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ballocationprompt = models.BooleanField(db_column='bAllocationPrompt')  # Field name made lowercase.
    bvariablebarcodesenabled = models.BooleanField(db_column='bVariableBarcodesEnabled')  # Field name made lowercase.
    ivariablebarcodepricelistid = models.IntegerField(db_column='iVariableBarcodePriceListID', blank=True, null=True)  # Field name made lowercase.
    ideliverymethoddefaultid = models.IntegerField(db_column='iDeliveryMethodDefaultID', blank=True, null=True)  # Field name made lowercase.
    bdocketforcereps = models.BooleanField(db_column='bDocketForceReps')  # Field name made lowercase.
    bdocketpromptforcustomeraccount = models.BooleanField(db_column='bDocketPromptForCustomerAccount')  # Field name made lowercase.
    bpettycashadvanceauthorisation = models.BooleanField(db_column='bPettyCashAdvanceAuthorisation')  # Field name made lowercase.
    fpettycashadvancelimit = models.FloatField(db_column='fPettyCashAdvanceLimit', blank=True, null=True)  # Field name made lowercase.
    brestrictpettycashadvance = models.BooleanField(db_column='bRestrictPettyCashAdvance')  # Field name made lowercase.
    bcashpickupwarning = models.BooleanField(db_column='bCashPickupWarning')  # Field name made lowercase.
    ccashpickupwarningmessage = models.CharField(db_column='cCashPickupWarningMessage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fcashpickupmaxcashintilllimit = models.FloatField(db_column='fCashPickupMaxCashInTillLimit', blank=True, null=True)  # Field name made lowercase.
    bdeposituse = models.BooleanField(db_column='bDepositUse')  # Field name made lowercase.
    bdepositforce = models.BooleanField(db_column='bDepositForce')  # Field name made lowercase.
    ideposittrcodeid = models.IntegerField(db_column='iDepositTrCodeID', blank=True, null=True)  # Field name made lowercase.
    fdepositminperc = models.FloatField(db_column='fDepositMinPerc', blank=True, null=True)  # Field name made lowercase.
    fdepositminamnt = models.FloatField(db_column='fDepositMinAmnt', blank=True, null=True)  # Field name made lowercase.
    bdepositallow = models.BooleanField(db_column='bDepositAllow')  # Field name made lowercase.
    fdepositgreaterthan = models.FloatField(db_column='fDepositGreaterThan', blank=True, null=True)  # Field name made lowercase.
    iinactivitytimeout = models.IntegerField(db_column='iInactivityTimeout', blank=True, null=True)  # Field name made lowercase.
    ireversalinvjrbatchid = models.IntegerField(db_column='iReversalInvJrBatchID', blank=True, null=True)  # Field name made lowercase.
    ireversaladjtrcodeid = models.IntegerField(db_column='iReversalAdjTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ilaybymodelcustomerid = models.IntegerField(db_column='iLayByModelCustomerID', blank=True, null=True)  # Field name made lowercase.
    ireversalagentid = models.IntegerField(db_column='iReversalAgentID', blank=True, null=True)  # Field name made lowercase.
    ilaybypaymenttermcount = models.IntegerField(db_column='iLayByPaymentTermCount', blank=True, null=True)  # Field name made lowercase.
    ilaybypaymenttermonday = models.IntegerField(db_column='iLayByPaymentTermOnDay', blank=True, null=True)  # Field name made lowercase.
    ilaybypaymenttermofevery = models.IntegerField(db_column='iLayByPaymentTermOfEvery', blank=True, null=True)  # Field name made lowercase.
    flaybydepositminperc = models.FloatField(db_column='fLayByDepositMinPerc', blank=True, null=True)  # Field name made lowercase.
    flaybydepositminamnt = models.FloatField(db_column='fLayByDepositMinAmnt', blank=True, null=True)  # Field name made lowercase.
    flaybycancellationperc = models.FloatField(db_column='fLayByCancellationPerc', blank=True, null=True)  # Field name made lowercase.
    flaybycancellationamnt = models.FloatField(db_column='fLayByCancellationAmnt', blank=True, null=True)  # Field name made lowercase.
    ilaybycancellationtrcodeid = models.IntegerField(db_column='iLayByCancellationTrCodeID', blank=True, null=True)  # Field name made lowercase.
    breservestockorders = models.BooleanField(db_column='bReserveStockOrders')  # Field name made lowercase.
    breservestocklaybys = models.BooleanField(db_column='bReserveStockLayBys')  # Field name made lowercase.
    bpromoautoyn = models.BooleanField(db_column='bPromoAutoYN')  # Field name made lowercase.
    ipromoautolength = models.IntegerField(db_column='iPromoAutoLength')  # Field name made lowercase.
    ipromoautoalphalength = models.IntegerField(db_column='iPromoAutoAlphaLength')  # Field name made lowercase.
    bupperpromono = models.BooleanField(db_column='bUpperPromoNo')  # Field name made lowercase.
    ikeepasidedaystoexpiry = models.IntegerField(db_column='iKeepAsideDaysToExpiry')  # Field name made lowercase.
    idisplaydocketpromptfields = models.IntegerField(db_column='iDisplayDocketPromptFields')  # Field name made lowercase.
    iforcedocketpromptfields = models.IntegerField(db_column='iForceDocketPromptFields')  # Field name made lowercase.
    blaybyfirstpaymentincurrentperiod = models.BooleanField(db_column='bLayByFirstPaymentInCurrentPeriod')  # Field name made lowercase.
    bautoadjust = models.BooleanField(db_column='bAutoAdjust')  # Field name made lowercase.
    cdocketmodedocketpromptfields = models.CharField(db_column='cDocketModeDocketPromptFields', max_length=400, blank=True, null=True)  # Field name made lowercase.
    ctillconfigpassword = models.CharField(db_column='cTillConfigPassword', max_length=160, blank=True, null=True)  # Field name made lowercase.
    bdisplaydocketpromotioncode = models.BooleanField(db_column='bDisplayDocketPromotionCode')  # Field name made lowercase.
    bdisplaydocketpromotiondescription = models.BooleanField(db_column='bDisplayDocketPromotionDescription')  # Field name made lowercase.
    freturnlimit = models.FloatField(db_column='fReturnLimit', blank=True, null=True)  # Field name made lowercase.
    breturnauthorisation = models.BooleanField(db_column='bReturnAuthorisation')  # Field name made lowercase.
    brestrictreturn = models.BooleanField(db_column='bRestrictReturn')  # Field name made lowercase.
    bpromoitemlistautoyn = models.BooleanField(db_column='bPromoItemListAutoYN')  # Field name made lowercase.
    bupperpromoitemlistno = models.BooleanField(db_column='bUpperPromoItemListNo')  # Field name made lowercase.
    ipromoitemlistautolength = models.IntegerField(db_column='iPromoItemListAutoLength')  # Field name made lowercase.
    ipromoitemlistautoalphalength = models.IntegerField(db_column='iPromoItemListAutoAlphaLength')  # Field name made lowercase.
    blaybyedit = models.BooleanField(db_column='bLayByEdit')  # Field name made lowercase.
    blineforcereps = models.BooleanField(db_column='bLineForceReps')  # Field name made lowercase.
    bfloatperagentortill = models.BooleanField(db_column='bFloatPerAgentOrTill')  # Field name made lowercase.
    itradingsessionduration = models.IntegerField(db_column='iTradingSessionDuration', blank=True, null=True)  # Field name made lowercase.
    bdisabletradeonexpiry = models.BooleanField(db_column='bDisableTradeOnExpiry')  # Field name made lowercase.
    bforceserialnumbers = models.BooleanField(db_column='bForceSerialNumbers')  # Field name made lowercase.
    busedocketroundingontender = models.BooleanField(db_column='bUseDocketRoundingOnTender', blank=True, null=True)  # Field name made lowercase.
    broundingoncashtenderonly = models.BooleanField(db_column='bRoundingOnCashTenderOnly', blank=True, null=True)  # Field name made lowercase.
    iroundingglaccount = models.IntegerField(db_column='iRoundingGLAccount', blank=True, null=True)  # Field name made lowercase.
    ballowcashdrawerhandover = models.BooleanField(db_column='bAllowCashDrawerHandover', blank=True, null=True)  # Field name made lowercase.
    iinvsplitprocessoption = models.IntegerField(db_column='iInvSplitProcessOption')  # Field name made lowercase.
    busevasairtime = models.BooleanField(db_column='bUseVASAirtime', blank=True, null=True)  # Field name made lowercase.
    cvasairtimemerchantid = models.CharField(db_column='cVASAirtimeMerchantID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cvasairtimehosturi = models.CharField(db_column='cVASAirtimeHostURI', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bautoreservestocklaybys = models.BooleanField(db_column='bAutoReserveStockLayBys')  # Field name made lowercase.
    bforceorigtendertypeonreturn = models.BooleanField(db_column='bForceOrigTenderTypeonReturn')  # Field name made lowercase.
    blaybysautocalculatepayments = models.BooleanField(db_column='bLayBysAutoCalculatePayments', blank=True, null=True)  # Field name made lowercase.
    bsetlaybyonpromotionon = models.BooleanField(db_column='bSetLaybyOnPromotionOn', blank=True, null=True)  # Field name made lowercase.
    field_retdefaults_ibranchid = models.IntegerField(db_column='_retDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_dcreateddate = models.DateTimeField(db_column='_retDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_dmodifieddate = models.DateTimeField(db_column='_retDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_icreatedbranchid = models.IntegerField(db_column='_retDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_imodifiedbranchid = models.IntegerField(db_column='_retDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_icreatedagentid = models.IntegerField(db_column='_retDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_imodifiedagentid = models.IntegerField(db_column='_retDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_ichangesetid = models.IntegerField(db_column='_retDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdefaults_checksum = models.TextField(db_column='_retDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    bautoadjustreserved = models.BooleanField(db_column='bAutoAdjustReserved', blank=True, null=True)  # Field name made lowercase.
    busecurrency = models.BooleanField(db_column='bUseCurrency')  # Field name made lowercase.
    busesellingrate = models.BooleanField(db_column='bUseSellingRate')  # Field name made lowercase.
    fmulticurrencyvariance = models.FloatField(db_column='fMultiCurrencyVariance', blank=True, null=True)  # Field name made lowercase.
    broundingonmulticurrencycashtenderonly = models.BooleanField(db_column='bRoundingOnMultiCurrencyCashTenderOnly')  # Field name made lowercase.
    buseuomvolumediscount = models.BooleanField(db_column='bUseUOMVolumeDiscount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retDefaults'


class Retdenomination(models.Model):
    iddenomination = models.AutoField(db_column='idDenomination', primary_key=True)  # Field name made lowercase.
    cdenominationcode = models.CharField(db_column='cDenominationCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mmultiple = models.DecimalField(db_column='mMultiple', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    biscoin = models.BooleanField(db_column='bIsCoin', blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_retdenomination_ibranchid = models.IntegerField(db_column='_retDenomination_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_dcreateddate = models.DateTimeField(db_column='_retDenomination_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_dmodifieddate = models.DateTimeField(db_column='_retDenomination_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_icreatedbranchid = models.IntegerField(db_column='_retDenomination_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_imodifiedbranchid = models.IntegerField(db_column='_retDenomination_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_icreatedagentid = models.IntegerField(db_column='_retDenomination_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_imodifiedagentid = models.IntegerField(db_column='_retDenomination_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_ichangesetid = models.IntegerField(db_column='_retDenomination_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdenomination_checksum = models.TextField(db_column='_retDenomination_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retDenomination'


class Retdiscountreason(models.Model):
    iddiscountreason = models.AutoField(db_column='idDiscountReason', primary_key=True)  # Field name made lowercase.
    cdiscountreasoncode = models.CharField(db_column='cDiscountReasonCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cdiscountreasondesc = models.CharField(db_column='cDiscountReasonDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_retdiscountreason_ibranchid = models.IntegerField(db_column='_retDiscountReason_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_dcreateddate = models.DateTimeField(db_column='_retDiscountReason_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_dmodifieddate = models.DateTimeField(db_column='_retDiscountReason_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_icreatedbranchid = models.IntegerField(db_column='_retDiscountReason_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_imodifiedbranchid = models.IntegerField(db_column='_retDiscountReason_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_icreatedagentid = models.IntegerField(db_column='_retDiscountReason_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_imodifiedagentid = models.IntegerField(db_column='_retDiscountReason_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_ichangesetid = models.IntegerField(db_column='_retDiscountReason_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retdiscountreason_checksum = models.TextField(db_column='_retDiscountReason_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retDiscountReason'


class Retdocketlock(models.Model):
    iddocketlock = models.AutoField(db_column='idDocketLock', primary_key=True)  # Field name made lowercase.
    idocketid = models.BigIntegerField(db_column='iDocketID')  # Field name made lowercase.
    itillid = models.IntegerField(db_column='iTillID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retDocketLock'


class Retlaybys(models.Model):
    idlaybys = models.AutoField(db_column='idLayBys', primary_key=True)  # Field name made lowercase.
    iinvoiceid = models.BigIntegerField(db_column='iInvoiceID', blank=True, null=True)  # Field name made lowercase.
    itermcount = models.IntegerField(db_column='iTermCount', blank=True, null=True)  # Field name made lowercase.
    itermonday = models.IntegerField(db_column='iTermOnDay', blank=True, null=True)  # Field name made lowercase.
    itermofevery = models.IntegerField(db_column='iTermOfEvery', blank=True, null=True)  # Field name made lowercase.
    flaybytotal = models.FloatField(db_column='fLayByTotal', blank=True, null=True)  # Field name made lowercase.
    dinceptiondate = models.DateTimeField(db_column='dInceptionDate', blank=True, null=True)  # Field name made lowercase.
    itermselapsed = models.IntegerField(db_column='iTermsElapsed', blank=True, null=True)  # Field name made lowercase.
    fpaidtodate = models.FloatField(db_column='fPaidToDate', blank=True, null=True)  # Field name made lowercase.
    dlastpaymentdate = models.DateTimeField(db_column='dLastPaymentDate', blank=True, null=True)  # Field name made lowercase.
    dnextpaymentdate = models.DateTimeField(db_column='dNextPaymentDate', blank=True, null=True)  # Field name made lowercase.
    dfinalpaymentdate = models.DateTimeField(db_column='dFinalPaymentDate', blank=True, null=True)  # Field name made lowercase.
    flaybydeposit = models.FloatField(db_column='fLayByDeposit', blank=True, null=True)  # Field name made lowercase.
    finstallmentamount = models.FloatField(db_column='fInstallmentAmount', blank=True, null=True)  # Field name made lowercase.
    dlastupdated = models.DateTimeField(db_column='dLastUpdated', blank=True, null=True)  # Field name made lowercase.
    fpaymentdue = models.FloatField(db_column='fPaymentDue', blank=True, null=True)  # Field name made lowercase.
    iinvoiceidfinalised = models.BigIntegerField(db_column='iInvoiceIDFinalised', blank=True, null=True)  # Field name made lowercase.
    fcancellationfee = models.FloatField(db_column='fCancellationFee', blank=True, null=True)  # Field name made lowercase.
    fcancellationfeetax = models.FloatField(db_column='fCancellationFeeTax', blank=True, null=True)  # Field name made lowercase.
    field_retlaybys_ibranchid = models.IntegerField(db_column='_retLayBys_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_dcreateddate = models.DateTimeField(db_column='_retLayBys_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_dmodifieddate = models.DateTimeField(db_column='_retLayBys_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_icreatedbranchid = models.IntegerField(db_column='_retLayBys_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_imodifiedbranchid = models.IntegerField(db_column='_retLayBys_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_icreatedagentid = models.IntegerField(db_column='_retLayBys_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_imodifiedagentid = models.IntegerField(db_column='_retLayBys_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_ichangesetid = models.IntegerField(db_column='_retLayBys_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retlaybys_checksum = models.TextField(db_column='_retLayBys_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retLayBys'


class Retposlogfile(models.Model):
    idposlogfile = models.AutoField(db_column='idPOSLogFile', primary_key=True)  # Field name made lowercase.
    isystemfunctionid = models.IntegerField(db_column='iSystemFunctionID', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    itillid = models.IntegerField(db_column='iTillID')  # Field name made lowercase.
    isupervisoragentid = models.IntegerField(db_column='iSupervisorAgentID', blank=True, null=True)  # Field name made lowercase.
    dcurrentdate = models.DateTimeField(db_column='dCurrentDate', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    itradingsessionid = models.IntegerField(db_column='iTradingSessionID', blank=True, null=True)  # Field name made lowercase.
    field_retposlogfile_ibranchid = models.IntegerField(db_column='_retPOSLogFile_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_dcreateddate = models.DateTimeField(db_column='_retPOSLogFile_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_dmodifieddate = models.DateTimeField(db_column='_retPOSLogFile_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_icreatedbranchid = models.IntegerField(db_column='_retPOSLogFile_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_imodifiedbranchid = models.IntegerField(db_column='_retPOSLogFile_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_icreatedagentid = models.IntegerField(db_column='_retPOSLogFile_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_imodifiedagentid = models.IntegerField(db_column='_retPOSLogFile_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_ichangesetid = models.IntegerField(db_column='_retPOSLogFile_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposlogfile_checksum = models.TextField(db_column='_retPOSLogFile_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPOSLogFile'


class Retposloglinks(models.Model):
    idposloglinks = models.BigAutoField(db_column='idPOSLogLinks', primary_key=True)  # Field name made lowercase.
    iinvnumid = models.BigIntegerField(db_column='iInvNumID')  # Field name made lowercase.
    iinvlineid = models.BigIntegerField(db_column='iInvLineID', blank=True, null=True)  # Field name made lowercase.
    ilogid = models.IntegerField(db_column='iLogID', blank=True, null=True)  # Field name made lowercase.
    field_retposloglinks_ibranchid = models.IntegerField(db_column='_retPOSLogLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_dcreateddate = models.DateTimeField(db_column='_retPOSLogLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_dmodifieddate = models.DateTimeField(db_column='_retPOSLogLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_icreatedbranchid = models.IntegerField(db_column='_retPOSLogLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_imodifiedbranchid = models.IntegerField(db_column='_retPOSLogLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_icreatedagentid = models.IntegerField(db_column='_retPOSLogLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_imodifiedagentid = models.IntegerField(db_column='_retPOSLogLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_ichangesetid = models.IntegerField(db_column='_retPOSLogLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposloglinks_checksum = models.TextField(db_column='_retPOSLogLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPOSLogLinks'


class Retposmenusetup(models.Model):
    idposmenusetup = models.BigAutoField(db_column='idPOSMenuSetup', primary_key=True)  # Field name made lowercase.
    cposmenucode = models.CharField(db_column='cPOSMenuCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cposmenudescription = models.CharField(db_column='cPOSMenuDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ibackgroundcolour = models.IntegerField(db_column='iBackgroundColour', blank=True, null=True)  # Field name made lowercase.
    btransparentdisabledbuttons = models.BooleanField(db_column='bTransparentDisabledButtons', blank=True, null=True)  # Field name made lowercase.
    field_retposmenusetup_ibranchid = models.IntegerField(db_column='_retPOSMenuSetup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_dcreateddate = models.DateTimeField(db_column='_retPOSMenuSetup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_dmodifieddate = models.DateTimeField(db_column='_retPOSMenuSetup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_icreatedbranchid = models.IntegerField(db_column='_retPOSMenuSetup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_imodifiedbranchid = models.IntegerField(db_column='_retPOSMenuSetup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_icreatedagentid = models.IntegerField(db_column='_retPOSMenuSetup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_imodifiedagentid = models.IntegerField(db_column='_retPOSMenuSetup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_ichangesetid = models.IntegerField(db_column='_retPOSMenuSetup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenusetup_checksum = models.TextField(db_column='_retPOSMenuSetup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPOSMenuSetup'


class Retpostender(models.Model):
    idpostender = models.BigAutoField(db_column='idPOSTender', primary_key=True)  # Field name made lowercase.
    ipostransactionid = models.BigIntegerField(db_column='iPOSTransactionID', blank=True, null=True)  # Field name made lowercase.
    itendertypeid = models.IntegerField(db_column='iTenderTypeID', blank=True, null=True)  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount', blank=True, null=True)  # Field name made lowercase.
    cnarrative = models.CharField(db_column='cNarrative', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ccardnumber = models.CharField(db_column='cCardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccardholder = models.CharField(db_column='cCardHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dexpirydate = models.DateTimeField(db_column='dExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cemvapplicationid = models.CharField(db_column='cEMVApplicationID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cemvverification = models.CharField(db_column='cEMVVerification', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cemvtrcertificate = models.CharField(db_column='cEMVTrCertificate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cemvappllabel = models.CharField(db_column='cEMVApplLabel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccardtype = models.CharField(db_column='cCardType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cauthcode = models.CharField(db_column='cAuthCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    deftdatetime = models.DateTimeField(db_column='dEFTDateTime', blank=True, null=True)  # Field name made lowercase.
    cemvtsi = models.CharField(db_column='cEMVTSI', max_length=4, blank=True, null=True)  # Field name made lowercase.
    idinvoicedeposits = models.IntegerField(db_column='idInvoiceDeposits', blank=True, null=True)  # Field name made lowercase.
    ceftbudgetperiod = models.CharField(db_column='cEFTBudgetPeriod', max_length=2)  # Field name made lowercase.
    cauthorisationid = models.CharField(db_column='cAuthorisationID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cinstitutionid = models.CharField(db_column='cInstitutionID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ctransactiontype = models.CharField(db_column='cTransactionType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    caccounttype = models.CharField(db_column='cAccountType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ce0210respcode = models.CharField(db_column='cE0210RespCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ce0202respcode = models.CharField(db_column='cE0202RespCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bchipcard = models.BooleanField(db_column='bChipCard')  # Field name made lowercase.
    ceftreferencenumber = models.CharField(db_column='cEFTReferenceNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bmanualeft = models.BooleanField(db_column='bManualEFT')  # Field name made lowercase.
    field_retpostender_ibranchid = models.IntegerField(db_column='_retPOSTender_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_dcreateddate = models.DateTimeField(db_column='_retPOSTender_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_dmodifieddate = models.DateTimeField(db_column='_retPOSTender_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_icreatedbranchid = models.IntegerField(db_column='_retPOSTender_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_imodifiedbranchid = models.IntegerField(db_column='_retPOSTender_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_icreatedagentid = models.IntegerField(db_column='_retPOSTender_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_imodifiedagentid = models.IntegerField(db_column='_retPOSTender_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_ichangesetid = models.IntegerField(db_column='_retPOSTender_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostender_checksum = models.TextField(db_column='_retPOSTender_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    icurrencyid = models.IntegerField(db_column='iCurrencyID', blank=True, null=True)  # Field name made lowercase.
    famountforeign = models.FloatField(db_column='fAmountForeign', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retPOSTender'


class Retpostransaction(models.Model):
    idpostransaction = models.BigAutoField(db_column='idPOSTransaction', primary_key=True)  # Field name made lowercase.
    itillid = models.IntegerField(db_column='iTillID', blank=True, null=True)  # Field name made lowercase.
    dtransactiondate = models.DateTimeField(db_column='dTransactionDate', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    itrcodesid = models.IntegerField(db_column='iTrCodesID', blank=True, null=True)  # Field name made lowercase.
    iaccountid = models.IntegerField(db_column='iAccountID', blank=True, null=True)  # Field name made lowercase.
    itilltxtype = models.IntegerField(db_column='iTillTxType', blank=True, null=True)  # Field name made lowercase.
    cauditnumber = models.CharField(db_column='cAuditNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount', blank=True, null=True)  # Field name made lowercase.
    famounttendered = models.FloatField(db_column='fAmountTendered', blank=True, null=True)  # Field name made lowercase.
    famountchange = models.FloatField(db_column='fAmountChange', blank=True, null=True)  # Field name made lowercase.
    iagentsessionid = models.IntegerField(db_column='iAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    iinvnumid = models.BigIntegerField(db_column='iInvNumID', blank=True, null=True)  # Field name made lowercase.
    field_retpostransaction_ibranchid = models.IntegerField(db_column='_retPOSTransaction_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_dcreateddate = models.DateTimeField(db_column='_retPOSTransaction_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_dmodifieddate = models.DateTimeField(db_column='_retPOSTransaction_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_icreatedbranchid = models.IntegerField(db_column='_retPOSTransaction_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_imodifiedbranchid = models.IntegerField(db_column='_retPOSTransaction_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_icreatedagentid = models.IntegerField(db_column='_retPOSTransaction_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_imodifiedagentid = models.IntegerField(db_column='_retPOSTransaction_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_ichangesetid = models.IntegerField(db_column='_retPOSTransaction_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpostransaction_checksum = models.TextField(db_column='_retPOSTransaction_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ctendercurrencylist = models.TextField(db_column='cTenderCurrencyList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retPOSTransaction'


class Retpettycash(models.Model):
    idpettycash = models.AutoField(db_column='idPettyCash', primary_key=True)  # Field name made lowercase.
    ipettycashtypeid = models.IntegerField(db_column='iPettyCashTypeID', blank=True, null=True)  # Field name made lowercase.
    ccomment = models.CharField(db_column='cComment', max_length=128, blank=True, null=True)  # Field name made lowercase.
    iadvancedagentsessionid = models.IntegerField(db_column='iAdvancedAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    dadvanceddate = models.DateTimeField(db_column='dAdvancedDate', blank=True, null=True)  # Field name made lowercase.
    fadvancedamount = models.FloatField(db_column='fAdvancedAmount', blank=True, null=True)  # Field name made lowercase.
    bprocessed = models.BooleanField(db_column='bProcessed')  # Field name made lowercase.
    iprocessedagentsessionid = models.IntegerField(db_column='iProcessedAgentSessionID', blank=True, null=True)  # Field name made lowercase.
    dprocesseddate = models.DateTimeField(db_column='dProcessedDate', blank=True, null=True)  # Field name made lowercase.
    fchangeamount = models.FloatField(db_column='fChangeAmount', blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iadvancedtillid = models.IntegerField(db_column='iAdvancedTillID', blank=True, null=True)  # Field name made lowercase.
    iprocessedtillid = models.IntegerField(db_column='iProcessedTillID', blank=True, null=True)  # Field name made lowercase.
    field_retpettycash_ibranchid = models.IntegerField(db_column='_retPettyCash_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_dcreateddate = models.DateTimeField(db_column='_retPettyCash_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_dmodifieddate = models.DateTimeField(db_column='_retPettyCash_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_icreatedbranchid = models.IntegerField(db_column='_retPettyCash_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_imodifiedbranchid = models.IntegerField(db_column='_retPettyCash_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_icreatedagentid = models.IntegerField(db_column='_retPettyCash_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_imodifiedagentid = models.IntegerField(db_column='_retPettyCash_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_ichangesetid = models.IntegerField(db_column='_retPettyCash_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycash_checksum = models.TextField(db_column='_retPettyCash_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPettyCash'


class Retpettycashline(models.Model):
    idpettycashline = models.AutoField(db_column='idPettyCashLine', primary_key=True)  # Field name made lowercase.
    ipettycashid = models.IntegerField(db_column='iPettyCashID', blank=True, null=True)  # Field name made lowercase.
    creference = models.CharField(db_column='cReference', max_length=128, blank=True, null=True)  # Field name made lowercase.
    fexclamount = models.FloatField(db_column='fExclAmount', blank=True, null=True)  # Field name made lowercase.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID', blank=True, null=True)  # Field name made lowercase.
    ftaxrate = models.FloatField(db_column='fTaxRate', blank=True, null=True)  # Field name made lowercase.
    finclamount = models.FloatField(db_column='fInclAmount', blank=True, null=True)  # Field name made lowercase.
    field_retpettycashline_ibranchid = models.IntegerField(db_column='_retPettyCashLine_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_dcreateddate = models.DateTimeField(db_column='_retPettyCashLine_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_dmodifieddate = models.DateTimeField(db_column='_retPettyCashLine_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_icreatedbranchid = models.IntegerField(db_column='_retPettyCashLine_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_imodifiedbranchid = models.IntegerField(db_column='_retPettyCashLine_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_icreatedagentid = models.IntegerField(db_column='_retPettyCashLine_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_imodifiedagentid = models.IntegerField(db_column='_retPettyCashLine_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_ichangesetid = models.IntegerField(db_column='_retPettyCashLine_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashline_checksum = models.TextField(db_column='_retPettyCashLine_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPettyCashLine'


class Retpettycashtype(models.Model):
    idpettycashtype = models.AutoField(db_column='idPettyCashType', primary_key=True)  # Field name made lowercase.
    cpettycashtypecode = models.CharField(db_column='cPettyCashTypeCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cpettycashtypedesc = models.CharField(db_column='cPettyCashTypeDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    ipettycashledgerid = models.IntegerField(db_column='iPettyCashLedgerID', blank=True, null=True)  # Field name made lowercase.
    ipettycashtaxtypeid = models.IntegerField(db_column='iPettyCashTaxTypeID', blank=True, null=True)  # Field name made lowercase.
    ipettycashtaxledgerid = models.IntegerField(db_column='iPettyCashTaxLedgerID', blank=True, null=True)  # Field name made lowercase.
    field_retpettycashtype_ibranchid = models.IntegerField(db_column='_retPettyCashType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_dcreateddate = models.DateTimeField(db_column='_retPettyCashType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_dmodifieddate = models.DateTimeField(db_column='_retPettyCashType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_icreatedbranchid = models.IntegerField(db_column='_retPettyCashType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_imodifiedbranchid = models.IntegerField(db_column='_retPettyCashType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_icreatedagentid = models.IntegerField(db_column='_retPettyCashType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_imodifiedagentid = models.IntegerField(db_column='_retPettyCashType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_ichangesetid = models.IntegerField(db_column='_retPettyCashType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpettycashtype_checksum = models.TextField(db_column='_retPettyCashType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPettyCashType'


class Retposmenu(models.Model):
    idposmenu = models.BigAutoField(db_column='idPOSMenu', primary_key=True)  # Field name made lowercase.
    iposkeyindex = models.IntegerField(db_column='iPOSKeyIndex', blank=True, null=True)  # Field name made lowercase.
    cposkeycaption = models.CharField(db_column='cPOSKeyCaption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iposkeycolor = models.IntegerField(db_column='iPOSKeyColor', blank=True, null=True)  # Field name made lowercase.
    iposkeyfontcolor = models.IntegerField(db_column='iPOSKeyFontColor', blank=True, null=True)  # Field name made lowercase.
    icustomindex = models.IntegerField(db_column='iCustomIndex', blank=True, null=True)  # Field name made lowercase.
    idposmenusetup = models.BigIntegerField(db_column='idPOSMenuSetup', blank=True, null=True)  # Field name made lowercase.
    cskinname = models.CharField(db_column='cSkinName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busedesigncolour = models.BooleanField(db_column='bUseDesignColour', blank=True, null=True)  # Field name made lowercase.
    istocklink = models.IntegerField(db_column='iStockLink', blank=True, null=True)  # Field name made lowercase.
    imid = models.IntegerField(db_column='iMID', blank=True, null=True)  # Field name made lowercase.
    field_retposmenu_ibranchid = models.IntegerField(db_column='_retPOSMenu_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_dcreateddate = models.DateTimeField(db_column='_retPOSMenu_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_dmodifieddate = models.DateTimeField(db_column='_retPOSMenu_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_icreatedbranchid = models.IntegerField(db_column='_retPOSMenu_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_imodifiedbranchid = models.IntegerField(db_column='_retPOSMenu_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_icreatedagentid = models.IntegerField(db_column='_retPOSMenu_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_imodifiedagentid = models.IntegerField(db_column='_retPOSMenu_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_ichangesetid = models.IntegerField(db_column='_retPOSMenu_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retposmenu_checksum = models.TextField(db_column='_retPOSMenu_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPosMenu'


class Retpriceoverridereason(models.Model):
    idpriceoverridereason = models.AutoField(db_column='idPriceOverrideReason', primary_key=True)  # Field name made lowercase.
    cpriceoverridereasoncode = models.CharField(db_column='cPriceOverrideReasonCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cpriceoverridereasondesc = models.CharField(db_column='cPriceOverrideReasonDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_retpriceoverridereason_ibranchid = models.IntegerField(db_column='_retPriceOverrideReason_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_dcreateddate = models.DateTimeField(db_column='_retPriceOverrideReason_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_dmodifieddate = models.DateTimeField(db_column='_retPriceOverrideReason_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_icreatedbranchid = models.IntegerField(db_column='_retPriceOverrideReason_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_imodifiedbranchid = models.IntegerField(db_column='_retPriceOverrideReason_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_icreatedagentid = models.IntegerField(db_column='_retPriceOverrideReason_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_imodifiedagentid = models.IntegerField(db_column='_retPriceOverrideReason_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_ichangesetid = models.IntegerField(db_column='_retPriceOverrideReason_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retpriceoverridereason_checksum = models.TextField(db_column='_retPriceOverrideReason_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retPriceOverrideReason'


class Retreturnreason(models.Model):
    idreturnreason = models.AutoField(db_column='idReturnReason', primary_key=True)  # Field name made lowercase.
    creturnreasoncode = models.CharField(db_column='cReturnReasonCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    creturnreasondesc = models.CharField(db_column='cReturnReasonDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_retreturnreason_ibranchid = models.IntegerField(db_column='_retReturnReason_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_dcreateddate = models.DateTimeField(db_column='_retReturnReason_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_dmodifieddate = models.DateTimeField(db_column='_retReturnReason_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_icreatedbranchid = models.IntegerField(db_column='_retReturnReason_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_imodifiedbranchid = models.IntegerField(db_column='_retReturnReason_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_icreatedagentid = models.IntegerField(db_column='_retReturnReason_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_imodifiedagentid = models.IntegerField(db_column='_retReturnReason_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_ichangesetid = models.IntegerField(db_column='_retReturnReason_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retreturnreason_checksum = models.TextField(db_column='_retReturnReason_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retReturnReason'


class Rettendertype(models.Model):
    idtendertype = models.AutoField(db_column='idTenderType', primary_key=True)  # Field name made lowercase.
    ctendertypecode = models.CharField(db_column='cTenderTypeCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ctendertypedesc = models.CharField(db_column='cTenderTypeDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    idisplayorder = models.IntegerField(db_column='iDisplayOrder', blank=True, null=True)  # Field name made lowercase.
    ballowovertender = models.BooleanField(db_column='bAllowOverTender')  # Field name made lowercase.
    bopendrawer = models.BooleanField(db_column='bOpenDrawer')  # Field name made lowercase.
    fhouselimit = models.FloatField(db_column='fHouseLimit', blank=True, null=True)  # Field name made lowercase.
    brequirenarration = models.BooleanField(db_column='bRequireNarration')  # Field name made lowercase.
    ireceipttrcodeid = models.IntegerField(db_column='iReceiptTrCodeID', blank=True, null=True)  # Field name made lowercase.
    irefundtrcodeid = models.IntegerField(db_column='iRefundTrCodeID', blank=True, null=True)  # Field name made lowercase.
    ideposittrcodeid = models.FloatField(db_column='iDepositTrCodeID', blank=True, null=True)  # Field name made lowercase.
    itypeoftender = models.IntegerField(db_column='iTypeOfTender', blank=True, null=True)  # Field name made lowercase.
    icarddisplayfirst = models.IntegerField(db_column='iCardDisplayFirst', blank=True, null=True)  # Field name made lowercase.
    icarddisplaylast = models.IntegerField(db_column='iCardDisplayLast', blank=True, null=True)  # Field name made lowercase.
    bforcecardnumber = models.BooleanField(db_column='bForceCardNumber')  # Field name made lowercase.
    bforcecardholder = models.BooleanField(db_column='bForceCardHolder')  # Field name made lowercase.
    cexpiryformat = models.CharField(db_column='cExpiryFormat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bforceexpiry = models.BooleanField(db_column='bForceExpiry')  # Field name made lowercase.
    busepinpad = models.BooleanField(db_column='bUsePinPad', blank=True, null=True)  # Field name made lowercase.
    bapplydocketrounding = models.BooleanField(db_column='bApplyDocketRounding', blank=True, null=True)  # Field name made lowercase.
    field_rettendertype_ibranchid = models.IntegerField(db_column='_retTenderType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_dcreateddate = models.DateTimeField(db_column='_retTenderType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_dmodifieddate = models.DateTimeField(db_column='_retTenderType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_icreatedbranchid = models.IntegerField(db_column='_retTenderType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_imodifiedbranchid = models.IntegerField(db_column='_retTenderType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_icreatedagentid = models.IntegerField(db_column='_retTenderType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_imodifiedagentid = models.IntegerField(db_column='_retTenderType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_ichangesetid = models.IntegerField(db_column='_retTenderType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettendertype_checksum = models.TextField(db_column='_retTenderType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retTenderType'


class Rettill(models.Model):
    idtill = models.AutoField(db_column='idTill', primary_key=True)  # Field name made lowercase.
    ctillcode = models.CharField(db_column='cTillCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    icurrentagentid = models.IntegerField(db_column='iCurrentAgentID', blank=True, null=True)  # Field name made lowercase.
    bautonumprependbranch = models.BooleanField(db_column='bAutoNumPrependBranch')  # Field name made lowercase.
    iautonuminvnext = models.IntegerField(db_column='iAutoNumInvNext', blank=True, null=True)  # Field name made lowercase.
    iautonuminvpad = models.IntegerField(db_column='iAutoNumInvPad', blank=True, null=True)  # Field name made lowercase.
    cautonuminvprefix = models.CharField(db_column='cAutoNumInvPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumordnext = models.IntegerField(db_column='iAutoNumOrdNext', blank=True, null=True)  # Field name made lowercase.
    iautonumordpad = models.IntegerField(db_column='iAutoNumOrdPad', blank=True, null=True)  # Field name made lowercase.
    cautonumordprefix = models.CharField(db_column='cAutoNumOrdPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumcrnnext = models.IntegerField(db_column='iAutoNumCrnNext', blank=True, null=True)  # Field name made lowercase.
    iautonumcrnpad = models.IntegerField(db_column='iAutoNumCrnPad', blank=True, null=True)  # Field name made lowercase.
    cautonumcrnprefix = models.CharField(db_column='cAutoNumCrnPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumquonext = models.IntegerField(db_column='iAutoNumQuoNext', blank=True, null=True)  # Field name made lowercase.
    iautonumquopad = models.IntegerField(db_column='iAutoNumQuoPad', blank=True, null=True)  # Field name made lowercase.
    cautonumquoprefix = models.CharField(db_column='cAutoNumQuoPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseID', blank=True, null=True)  # Field name made lowercase.
    iautonumcashupnext = models.IntegerField(db_column='iAutoNumCashUpNext', blank=True, null=True)  # Field name made lowercase.
    iautonumcashuppad = models.IntegerField(db_column='iAutoNumCashUpPad', blank=True, null=True)  # Field name made lowercase.
    cautonumcashupprefix = models.CharField(db_column='cAutoNumCashUpPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumpettycashnext = models.IntegerField(db_column='iAutoNumPettyCashNext', blank=True, null=True)  # Field name made lowercase.
    iautonumpettycashpad = models.IntegerField(db_column='iAutoNumPettyCashPad', blank=True, null=True)  # Field name made lowercase.
    cautonumpettycashprefix = models.CharField(db_column='cAutoNumPettyCashPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumcashpickupnext = models.IntegerField(db_column='iAutoNumCashPickupNext', blank=True, null=True)  # Field name made lowercase.
    iautonumcashpickuppad = models.IntegerField(db_column='iAutoNumCashPickupPad', blank=True, null=True)  # Field name made lowercase.
    cautonumcashpickupprefix = models.CharField(db_column='cAutoNumCashPickupPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumreceiptnext = models.IntegerField(db_column='iAutoNumReceiptNext', blank=True, null=True)  # Field name made lowercase.
    iautonumreceiptpad = models.IntegerField(db_column='iAutoNumReceiptPad', blank=True, null=True)  # Field name made lowercase.
    cautonumreceiptprefix = models.CharField(db_column='cAutoNumReceiptPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumrefundnext = models.IntegerField(db_column='iAutoNumRefundNext', blank=True, null=True)  # Field name made lowercase.
    iautonumrefundpad = models.IntegerField(db_column='iAutoNumRefundPad', blank=True, null=True)  # Field name made lowercase.
    cautonumrefundprefix = models.CharField(db_column='cAutoNumRefundPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumlaybyreceiptnext = models.IntegerField(db_column='iAutoNumLayByReceiptNext', blank=True, null=True)  # Field name made lowercase.
    iautonumlaybyreceiptpad = models.IntegerField(db_column='iAutoNumLayByReceiptPad', blank=True, null=True)  # Field name made lowercase.
    cautonumlaybyreceiptprefix = models.CharField(db_column='cAutoNumLayByReceiptPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumlaybyrefundnext = models.IntegerField(db_column='iAutoNumLayByRefundNext', blank=True, null=True)  # Field name made lowercase.
    iautonumlaybyrefundpad = models.IntegerField(db_column='iAutoNumLayByRefundPad', blank=True, null=True)  # Field name made lowercase.
    cautonumlaybyrefundprefix = models.CharField(db_column='cAutoNumLayByRefundPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumdelivnotenext = models.IntegerField(db_column='iAutoNumDelivNoteNext', blank=True, null=True)  # Field name made lowercase.
    iautonumdelivnotepad = models.IntegerField(db_column='iAutoNumDelivNotePad', blank=True, null=True)  # Field name made lowercase.
    cautonumdelivnoteprefix = models.CharField(db_column='cAutoNumDelivNotePrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumlaybynext = models.IntegerField(db_column='iAutoNumLayByNext', blank=True, null=True)  # Field name made lowercase.
    iautonumlaybypad = models.IntegerField(db_column='iAutoNumLayByPad', blank=True, null=True)  # Field name made lowercase.
    cautonumlaybyprefix = models.CharField(db_column='cAutoNumLayByPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumkeepasidenext = models.IntegerField(db_column='iAutoNumKeepAsideNext', blank=True, null=True)  # Field name made lowercase.
    iautonumkeepasidepad = models.IntegerField(db_column='iAutoNumKeepAsidePad', blank=True, null=True)  # Field name made lowercase.
    iautonumkeepasideprefix = models.CharField(db_column='iAutoNumKeepAsidePrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idocketinputmode = models.IntegerField(db_column='iDocketInputMode')  # Field name made lowercase.
    iautonumcashdrawerhandovernext = models.IntegerField(db_column='iAutoNumCashDrawerHandoverNext', blank=True, null=True)  # Field name made lowercase.
    iautonumcashdrawerhandoverpad = models.IntegerField(db_column='iAutoNumCashDrawerHandoverPad', blank=True, null=True)  # Field name made lowercase.
    cautonumcashdrawerhandoverprefix = models.CharField(db_column='cAutoNumCashDrawerHandoverPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    buseonscreenkeyboard = models.BooleanField(db_column='bUseOnScreenKeyboard', blank=True, null=True)  # Field name made lowercase.
    idposmenusetup = models.BigIntegerField(db_column='idPOSMenuSetup', blank=True, null=True)  # Field name made lowercase.
    iautonumgivnext = models.IntegerField(db_column='iAutoNumGIVNext', blank=True, null=True)  # Field name made lowercase.
    iautonumgivpad = models.IntegerField(db_column='iAutoNumGIVPad', blank=True, null=True)  # Field name made lowercase.
    cautonumgivprefix = models.CharField(db_column='cAutoNumGIVPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumcgrnext = models.IntegerField(db_column='iAutoNumCGRNext', blank=True, null=True)  # Field name made lowercase.
    iautonumcgrpad = models.IntegerField(db_column='iAutoNumCGRPad', blank=True, null=True)  # Field name made lowercase.
    cautonumcgrprefix = models.CharField(db_column='cAutoNumCGRPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iautonumattrqtyadjustmentnext = models.IntegerField(db_column='iAutoNumAttrQtyAdjustmentNext', blank=True, null=True)  # Field name made lowercase.
    iautonumattrqtyadjustmentpad = models.IntegerField(db_column='iAutoNumAttrQtyAdjustmentPad', blank=True, null=True)  # Field name made lowercase.
    cautonumattrqtyadjustmentprefix = models.CharField(db_column='cAutoNumAttrQtyAdjustmentPrefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    field_rettill_ibranchid = models.IntegerField(db_column='_retTill_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_dcreateddate = models.DateTimeField(db_column='_retTill_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_dmodifieddate = models.DateTimeField(db_column='_retTill_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_icreatedbranchid = models.IntegerField(db_column='_retTill_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_imodifiedbranchid = models.IntegerField(db_column='_retTill_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_icreatedagentid = models.IntegerField(db_column='_retTill_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_imodifiedagentid = models.IntegerField(db_column='_retTill_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_ichangesetid = models.IntegerField(db_column='_retTill_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettill_checksum = models.TextField(db_column='_retTill_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    itillloginscreen = models.IntegerField(db_column='iTillLoginScreen')  # Field name made lowercase.
    bautologout = models.BooleanField(db_column='bAutoLogout')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_retTill'


class Rettillsecurity(models.Model):
    idtillsecurity = models.AutoField(db_column='idTillSecurity', primary_key=True)  # Field name made lowercase.
    isystemfunction = models.IntegerField(db_column='iSystemFunction')  # Field name made lowercase.
    ipermission = models.IntegerField(db_column='iPermission', blank=True, null=True)  # Field name made lowercase.
    field_rettillsecurity_ibranchid = models.IntegerField(db_column='_retTillSecurity_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_dcreateddate = models.DateTimeField(db_column='_retTillSecurity_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_dmodifieddate = models.DateTimeField(db_column='_retTillSecurity_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_icreatedbranchid = models.IntegerField(db_column='_retTillSecurity_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_imodifiedbranchid = models.IntegerField(db_column='_retTillSecurity_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_icreatedagentid = models.IntegerField(db_column='_retTillSecurity_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_imodifiedagentid = models.IntegerField(db_column='_retTillSecurity_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_ichangesetid = models.IntegerField(db_column='_retTillSecurity_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillsecurity_checksum = models.TextField(db_column='_retTillSecurity_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retTillSecurity'


class Rettillstationery(models.Model):
    idtillstationery = models.AutoField(db_column='idTillStationery', primary_key=True)  # Field name made lowercase.
    islotypeid = models.IntegerField(db_column='iSloTypeID', blank=True, null=True)  # Field name made lowercase.
    islosource = models.IntegerField(db_column='iSloSource', blank=True, null=True)  # Field name made lowercase.
    islolayoutid = models.IntegerField(db_column='iSloLayoutID', blank=True, null=True)  # Field name made lowercase.
    iprinterpapersize = models.IntegerField(db_column='iPrinterPaperSize', blank=True, null=True)  # Field name made lowercase.
    iprintercopies = models.IntegerField(db_column='iPrinterCopies', blank=True, null=True)  # Field name made lowercase.
    iprintercollate = models.IntegerField(db_column='iPrinterCollate', blank=True, null=True)  # Field name made lowercase.
    iprinterduplex = models.IntegerField(db_column='iPrinterDuplex', blank=True, null=True)  # Field name made lowercase.
    iemailformatindex = models.IntegerField(db_column='iEmailFormatIndex', blank=True, null=True)  # Field name made lowercase.
    bzip = models.BooleanField(db_column='bZip', blank=True, null=True)  # Field name made lowercase.
    cemaildefaultsubject = models.CharField(db_column='cEmailDefaultSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cemaildefaultbody = models.CharField(db_column='cEmailDefaultBody', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    bemaildifferentlayout = models.BooleanField(db_column='bEmailDifferentLayout', blank=True, null=True)  # Field name made lowercase.
    iemaillayoutindex = models.IntegerField(db_column='iEmailLayoutIndex', blank=True, null=True)  # Field name made lowercase.
    field_rettillstationery_ibranchid = models.IntegerField(db_column='_retTillStationery_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_dcreateddate = models.DateTimeField(db_column='_retTillStationery_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_dmodifieddate = models.DateTimeField(db_column='_retTillStationery_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_icreatedbranchid = models.IntegerField(db_column='_retTillStationery_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_imodifiedbranchid = models.IntegerField(db_column='_retTillStationery_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_icreatedagentid = models.IntegerField(db_column='_retTillStationery_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_imodifiedagentid = models.IntegerField(db_column='_retTillStationery_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_ichangesetid = models.IntegerField(db_column='_retTillStationery_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettillstationery_checksum = models.TextField(db_column='_retTillStationery_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retTillStationery'


class Rettradingsession(models.Model):
    idtradingsession = models.AutoField(db_column='idTradingSession', primary_key=True)  # Field name made lowercase.
    isessionstatus = models.IntegerField(db_column='iSessionStatus', blank=True, null=True)  # Field name made lowercase.
    dtradingdate = models.DateTimeField(db_column='dTradingDate', blank=True, null=True)  # Field name made lowercase.
    csessiondescription = models.CharField(db_column='cSessionDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dstarttime = models.DateTimeField(db_column='dStartTime', blank=True, null=True)  # Field name made lowercase.
    istartagentid = models.IntegerField(db_column='iStartAgentID', blank=True, null=True)  # Field name made lowercase.
    dendtime = models.DateTimeField(db_column='dEndTime', blank=True, null=True)  # Field name made lowercase.
    iendagentid = models.IntegerField(db_column='iEndAgentID', blank=True, null=True)  # Field name made lowercase.
    ifinaliseagentid = models.IntegerField(db_column='iFinaliseAgentID', blank=True, null=True)  # Field name made lowercase.
    iexpectedduration = models.IntegerField(db_column='iExpectedDuration', blank=True, null=True)  # Field name made lowercase.
    bdisabletradingonexpiry = models.BooleanField(db_column='bDisableTradingOnExpiry')  # Field name made lowercase.
    field_rettradingsession_ibranchid = models.IntegerField(db_column='_retTradingSession_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_dcreateddate = models.DateTimeField(db_column='_retTradingSession_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_dmodifieddate = models.DateTimeField(db_column='_retTradingSession_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_icreatedbranchid = models.IntegerField(db_column='_retTradingSession_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_imodifiedbranchid = models.IntegerField(db_column='_retTradingSession_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_icreatedagentid = models.IntegerField(db_column='_retTradingSession_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_imodifiedagentid = models.IntegerField(db_column='_retTradingSession_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_ichangesetid = models.IntegerField(db_column='_retTradingSession_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rettradingsession_checksum = models.TextField(db_column='_retTradingSession_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retTradingSession'


class Retvariablebarcode(models.Model):
    idvariablebarcode = models.AutoField(db_column='idVariableBarcode', primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cdesc = models.CharField(db_column='cDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cprefix = models.CharField(db_column='cPrefix', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ifulllength = models.IntegerField(db_column='iFullLength', blank=True, null=True)  # Field name made lowercase.
    iitemstart = models.IntegerField(db_column='iItemStart', blank=True, null=True)  # Field name made lowercase.
    iitemlength = models.IntegerField(db_column='iItemLength', blank=True, null=True)  # Field name made lowercase.
    ivaluestart = models.IntegerField(db_column='iValueStart', blank=True, null=True)  # Field name made lowercase.
    ivaluelength = models.IntegerField(db_column='iValueLength', blank=True, null=True)  # Field name made lowercase.
    ivaluedecimals = models.IntegerField(db_column='iValueDecimals', blank=True, null=True)  # Field name made lowercase.
    ivaluetype = models.IntegerField(db_column='iValueType')  # Field name made lowercase.
    field_retvariablebarcode_ibranchid = models.IntegerField(db_column='_retVariableBarcode_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_dcreateddate = models.DateTimeField(db_column='_retVariableBarcode_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_dmodifieddate = models.DateTimeField(db_column='_retVariableBarcode_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_icreatedbranchid = models.IntegerField(db_column='_retVariableBarcode_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_imodifiedbranchid = models.IntegerField(db_column='_retVariableBarcode_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_icreatedagentid = models.IntegerField(db_column='_retVariableBarcode_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_imodifiedagentid = models.IntegerField(db_column='_retVariableBarcode_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_ichangesetid = models.IntegerField(db_column='_retVariableBarcode_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcode_checksum = models.TextField(db_column='_retVariableBarcode_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retVariableBarcode'


class Retvariablebarcodeagroups(models.Model):
    idvariablebarcodeagroups = models.AutoField(db_column='idVariableBarcodeAGroups', primary_key=True)  # Field name made lowercase.
    ivariablebarcodeid = models.IntegerField(db_column='iVariableBarcodeID')  # Field name made lowercase.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID', blank=True, null=True)  # Field name made lowercase.
    field_retvariablebarcodeagroups_ibranchid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_dcreateddate = models.DateTimeField(db_column='_retVariableBarcodeAGroups_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_dmodifieddate = models.DateTimeField(db_column='_retVariableBarcodeAGroups_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_icreatedbranchid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_imodifiedbranchid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_icreatedagentid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_imodifiedagentid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_ichangesetid = models.IntegerField(db_column='_retVariableBarcodeAGroups_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeagroups_checksum = models.TextField(db_column='_retVariableBarcodeAGroups_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retVariableBarcodeAGroups'


class Retvariablebarcodeatypes(models.Model):
    idvariablebarcodeatypes = models.AutoField(db_column='idVariableBarcodeATypes', primary_key=True)  # Field name made lowercase.
    ivariablebarcodeid = models.IntegerField(db_column='iVariableBarcodeID')  # Field name made lowercase.
    iattributetypeid = models.IntegerField(db_column='iAttributeTypeID', blank=True, null=True)  # Field name made lowercase.
    iattributestart = models.IntegerField(db_column='iAttributeStart', blank=True, null=True)  # Field name made lowercase.
    iattributelength = models.IntegerField(db_column='iAttributeLength', blank=True, null=True)  # Field name made lowercase.
    field_retvariablebarcodeatypes_ibranchid = models.IntegerField(db_column='_retVariableBarcodeATypes_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_dcreateddate = models.DateTimeField(db_column='_retVariableBarcodeATypes_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_dmodifieddate = models.DateTimeField(db_column='_retVariableBarcodeATypes_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_icreatedbranchid = models.IntegerField(db_column='_retVariableBarcodeATypes_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_imodifiedbranchid = models.IntegerField(db_column='_retVariableBarcodeATypes_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_icreatedagentid = models.IntegerField(db_column='_retVariableBarcodeATypes_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_imodifiedagentid = models.IntegerField(db_column='_retVariableBarcodeATypes_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_ichangesetid = models.IntegerField(db_column='_retVariableBarcodeATypes_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_retvariablebarcodeatypes_checksum = models.TextField(db_column='_retVariableBarcodeATypes_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_retVariableBarcodeATypes'


class Rtblactivedirectoryusers(models.Model):
    iadprofileid = models.AutoField(db_column='iADProfileID', primary_key=True)  # Field name made lowercase.
    iagentsid = models.IntegerField(db_column='iAgentsID')  # Field name made lowercase.
    cadprofileusername = models.CharField(db_column='cADProfileUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cadprofiledomainname = models.CharField(db_column='cADProfileDomainName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblactivedirectoryusers_ibranchid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_dcreateddate = models.DateTimeField(db_column='_rtblActiveDirectoryUsers_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_dmodifieddate = models.DateTimeField(db_column='_rtblActiveDirectoryUsers_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_icreatedbranchid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_imodifiedbranchid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_icreatedagentid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_imodifiedagentid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_ichangesetid = models.IntegerField(db_column='_rtblActiveDirectoryUsers_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblactivedirectoryusers_checksum = models.TextField(db_column='_rtblActiveDirectoryUsers_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblActiveDirectoryUsers'


class Rtblagentgroupmembers(models.Model):
    igroupid = models.IntegerField(db_column='iGroupID', primary_key=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    bsysgroupmember = models.BooleanField(db_column='bSysGroupMember')  # Field name made lowercase.
    field_rtblagentgroupmembers_ibranchid = models.IntegerField(db_column='_rtblAgentGroupMembers_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_dcreateddate = models.DateTimeField(db_column='_rtblAgentGroupMembers_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_dmodifieddate = models.DateTimeField(db_column='_rtblAgentGroupMembers_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_icreatedbranchid = models.IntegerField(db_column='_rtblAgentGroupMembers_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_imodifiedbranchid = models.IntegerField(db_column='_rtblAgentGroupMembers_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_icreatedagentid = models.IntegerField(db_column='_rtblAgentGroupMembers_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_imodifiedagentid = models.IntegerField(db_column='_rtblAgentGroupMembers_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_ichangesetid = models.IntegerField(db_column='_rtblAgentGroupMembers_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroupmembers_checksum = models.TextField(db_column='_rtblAgentGroupMembers_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblAgentGroupMembers'
        unique_together = (('igroupid', 'iagentid'),)


class Rtblagentgroups(models.Model):
    idagentgroups = models.AutoField(db_column='idAgentGroups', primary_key=True)  # Field name made lowercase.
    bsysgroup = models.BooleanField(db_column='bSysGroup')  # Field name made lowercase.
    cgroupname = models.CharField(db_column='cGroupName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccomments = models.CharField(db_column='cComments', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    bcanassign = models.BooleanField(db_column='bCanAssign')  # Field name made lowercase.
    iassignrule = models.IntegerField(db_column='iAssignRule')  # Field name made lowercase.
    iassignagent = models.IntegerField(db_column='iAssignAgent', blank=True, null=True)  # Field name made lowercase.
    busedefaulttree = models.BooleanField(db_column='bUseDefaultTree')  # Field name made lowercase.
    bcbgrpallvisible = models.BooleanField(db_column='bCBGrpAllVisible')  # Field name made lowercase.
    bcbgrpnonevisible = models.BooleanField(db_column='bCBGrpNoneVisible')  # Field name made lowercase.
    bjrgrpallvisible = models.BooleanField(db_column='bJRGrpAllVisible')  # Field name made lowercase.
    bjrgrpnonevisible = models.BooleanField(db_column='bJRGrpNoneVisible')  # Field name made lowercase.
    bcbgrpagentvisible = models.BooleanField(db_column='bCBGrpAgentVisible')  # Field name made lowercase.
    bjrgrpagentvisible = models.BooleanField(db_column='bJRGrpAgentVisible')  # Field name made lowercase.
    ipoauthtype = models.IntegerField(db_column='iPOAuthType')  # Field name made lowercase.
    ipoincidenttypeid = models.IntegerField(db_column='iPOIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    bpoexclusive = models.BooleanField(db_column='bPOExclusive')  # Field name made lowercase.
    fpolimit = models.FloatField(db_column='fPOLimit', blank=True, null=True)  # Field name made lowercase.
    bpousedefaults = models.BooleanField(db_column='bPOUseDefaults')  # Field name made lowercase.
    idposmenusetup = models.IntegerField(db_column='idPOSMenuSetup', blank=True, null=True)  # Field name made lowercase.
    field_rtblagentgroups_ibranchid = models.IntegerField(db_column='_rtblAgentGroups_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_dcreateddate = models.DateTimeField(db_column='_rtblAgentGroups_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_dmodifieddate = models.DateTimeField(db_column='_rtblAgentGroups_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_icreatedbranchid = models.IntegerField(db_column='_rtblAgentGroups_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_imodifiedbranchid = models.IntegerField(db_column='_rtblAgentGroups_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_icreatedagentid = models.IntegerField(db_column='_rtblAgentGroups_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_imodifiedagentid = models.IntegerField(db_column='_rtblAgentGroups_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_ichangesetid = models.IntegerField(db_column='_rtblAgentGroups_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentgroups_checksum = models.TextField(db_column='_rtblAgentGroups_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    caccessprocessflowidlst = models.CharField(db_column='cAccessProcessFlowIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessprocessflowchklstind = models.CharField(db_column='cAccessProcessFlowChkLstInd', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblAgentGroups'


class Rtblagentlockedout(models.Model):
    idagentlockedout = models.AutoField(db_column='IDAgentLockedOut', primary_key=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    dlockedoutdate = models.DateTimeField(db_column='dLockedOutDate')  # Field name made lowercase.
    dunlockedoutdate = models.DateTimeField(db_column='dUnlockedOutDate', blank=True, null=True)  # Field name made lowercase.
    iunlockoutagentid = models.IntegerField(db_column='iUnlockOutAgentID', blank=True, null=True)  # Field name made lowercase.
    field_rtblagentlockedout_ibranchid = models.IntegerField(db_column='_rtblAgentLockedOut_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_dcreateddate = models.DateTimeField(db_column='_rtblAgentLockedOut_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_dmodifieddate = models.DateTimeField(db_column='_rtblAgentLockedOut_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_icreatedbranchid = models.IntegerField(db_column='_rtblAgentLockedOut_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_imodifiedbranchid = models.IntegerField(db_column='_rtblAgentLockedOut_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_icreatedagentid = models.IntegerField(db_column='_rtblAgentLockedOut_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_imodifiedagentid = models.IntegerField(db_column='_rtblAgentLockedOut_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_ichangesetid = models.IntegerField(db_column='_rtblAgentLockedOut_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagentlockedout_checksum = models.TextField(db_column='_rtblAgentLockedOut_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblAgentLockedOut'


class Rtblagents(models.Model):
    idagents = models.AutoField(db_column='idAgents', primary_key=True)  # Field name made lowercase.
    bsysaccount = models.BooleanField(db_column='bSysAccount')  # Field name made lowercase.
    cagentname = models.CharField(db_column='cAgentName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpassword = models.CharField(db_column='cPassword', max_length=160, blank=True, null=True)  # Field name made lowercase.
    cfirstname = models.CharField(db_column='cFirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cinitials = models.CharField(db_column='cInitials', max_length=5, blank=True, null=True)  # Field name made lowercase.
    clastname = models.CharField(db_column='cLastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ctitle = models.CharField(db_column='cTitle', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cdisplayname = models.CharField(db_column='cDisplayName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctelwork = models.CharField(db_column='cTelWork', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelfax = models.CharField(db_column='cTelFax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelmobile = models.CharField(db_column='cTelMobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelhome = models.CharField(db_column='cTelHome', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cwebpage = models.CharField(db_column='cWebPage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccomments = models.CharField(db_column='cComments', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caddressstreet = models.CharField(db_column='cAddressStreet', max_length=512, blank=True, null=True)  # Field name made lowercase.
    caddresspobox = models.CharField(db_column='cAddressPOBox', max_length=30, blank=True, null=True)  # Field name made lowercase.
    caddresscity = models.CharField(db_column='cAddressCity', max_length=30, blank=True, null=True)  # Field name made lowercase.
    caddressstate = models.CharField(db_column='cAddressState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    caddresszip = models.CharField(db_column='cAddressZip', max_length=15, blank=True, null=True)  # Field name made lowercase.
    caddresscountry = models.CharField(db_column='cAddressCountry', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bcanassign = models.BooleanField(db_column='bCanAssign')  # Field name made lowercase.
    bpwdcanchange = models.BooleanField(db_column='bPwdCanChange')  # Field name made lowercase.
    bpwdmustchange = models.BooleanField(db_column='bPwdMustChange')  # Field name made lowercase.
    bpwdchangeevery = models.BooleanField(db_column='bPwdChangeEvery')  # Field name made lowercase.
    ipwdchangedays = models.IntegerField(db_column='iPwdChangeDays', blank=True, null=True)  # Field name made lowercase.
    dpwdlastchange = models.DateTimeField(db_column='dPwdLastChange', blank=True, null=True)  # Field name made lowercase.
    cpwdremind = models.CharField(db_column='cPwdRemind', max_length=160, blank=True, null=True)  # Field name made lowercase.
    bagentoutoffice = models.BooleanField(db_column='bAgentOutOffice')  # Field name made lowercase.
    bexitwarning = models.BooleanField(db_column='bExitWarning')  # Field name made lowercase.
    bcansetoutofoffice = models.BooleanField(db_column='bCanSetOutOfOffice')  # Field name made lowercase.
    bknowledgebasewarning = models.BooleanField(db_column='bKnowledgeBaseWarning')  # Field name made lowercase.
    bnewincidentnotification = models.BooleanField(db_column='bNewIncidentNotification')  # Field name made lowercase.
    busedefaulttree = models.BooleanField(db_column='bUseDefaultTree')  # Field name made lowercase.
    bautospellcheck = models.BooleanField(db_column='bAutoSpellCheck')  # Field name made lowercase.
    idefincidenttypegroupid = models.IntegerField(db_column='iDefIncidentTypeGroupID', blank=True, null=True)  # Field name made lowercase.
    ideftillid = models.IntegerField(db_column='iDefTillId', blank=True, null=True)  # Field name made lowercase.
    idefcashaccount = models.IntegerField(db_column='iDefCashAccount', blank=True, null=True)  # Field name made lowercase.
    idefwhseid = models.IntegerField(db_column='iDefWhseId', blank=True, null=True)  # Field name made lowercase.
    inotifyescalateminutes = models.IntegerField(db_column='iNotifyEscalateMinutes', blank=True, null=True)  # Field name made lowercase.
    inotifydueminutes = models.IntegerField(db_column='iNotifyDueMinutes', blank=True, null=True)  # Field name made lowercase.
    bforcethiswarehouse = models.BooleanField(db_column='bForceThisWarehouse')  # Field name made lowercase.
    bagentactive = models.BooleanField(db_column='bAgentActive')  # Field name made lowercase.
    bcbagnonevisible = models.BooleanField(db_column='bCBAgNoneVisible')  # Field name made lowercase.
    bcbagallvisible = models.BooleanField(db_column='bCBAgAllVisible')  # Field name made lowercase.
    bjragnonevisible = models.BooleanField(db_column='bJRAgNoneVisible')  # Field name made lowercase.
    bjragallvisible = models.BooleanField(db_column='bJRAgAllVisible')  # Field name made lowercase.
    bcbusegrpdefaults = models.BooleanField(db_column='bCBUseGrpDefaults')  # Field name made lowercase.
    bjrusegrpdefaults = models.BooleanField(db_column='bJRUseGrpDefaults')  # Field name made lowercase.
    bcbagownvisible = models.BooleanField(db_column='bCBAgOwnVisible')  # Field name made lowercase.
    bjragownvisible = models.BooleanField(db_column='bJRAgOwnVisible')  # Field name made lowercase.
    ipoauthtype = models.IntegerField(db_column='iPOAuthType')  # Field name made lowercase.
    ipoincidenttypeid = models.IntegerField(db_column='iPOIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    bpoexclusive = models.BooleanField(db_column='bPOExclusive')  # Field name made lowercase.
    fpolimit = models.FloatField(db_column='fPOLimit', blank=True, null=True)  # Field name made lowercase.
    bpousegrpdefaults = models.BooleanField(db_column='bPOUseGrpDefaults')  # Field name made lowercase.
    caccesspurchasewhidlst = models.CharField(db_column='cAccessPurchaseWhIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccesssaleswhidlst = models.CharField(db_column='cAccessSalesWhIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessothertxwhidlist = models.CharField(db_column='cAccessOtherTxWhIDList', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccesspurchasewhchklstind = models.CharField(db_column='cAccessPurchaseWhChkLstInd', max_length=1)  # Field name made lowercase.
    caccesssaleswhchklstind = models.CharField(db_column='cAccessSalesWhChkLstInd', max_length=1)  # Field name made lowercase.
    caccessothertxwhchklstind = models.CharField(db_column='cAccessOtherTxWhChkLstInd', max_length=1)  # Field name made lowercase.
    idefprojectid = models.IntegerField(db_column='iDefProjectID', blank=True, null=True)  # Field name made lowercase.
    caccessprojectidlst = models.CharField(db_column='cAccessProjectIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessprojectchklstind = models.CharField(db_column='cAccessProjectChkLstInd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idefrepid = models.IntegerField(db_column='iDefRepID', blank=True, null=True)  # Field name made lowercase.
    caccessrepidlst = models.CharField(db_column='cAccessRepIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessrepchklstind = models.CharField(db_column='cAccessRepChkLstInd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    max_ldisc = models.FloatField(db_column='Max_LDisc')  # Field name made lowercase.
    max_disc = models.FloatField(db_column='Max_Disc')  # Field name made lowercase.
    coperatorcode = models.CharField(db_column='cOperatorCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coperatorpassword = models.CharField(db_column='cOperatorPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coperatornewpassword = models.CharField(db_column='cOperatorNewPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caccessbranchidlst = models.CharField(db_column='cAccessBranchIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessbranchchklstind = models.CharField(db_column='cAccessBranchChkLstInd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idocketinputmode = models.IntegerField(db_column='iDocketInputMode')  # Field name made lowercase.
    coperatorcodepos = models.CharField(db_column='cOperatorCodePOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coperatorpasswordpos = models.CharField(db_column='cOperatorPasswordPOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coperatornewpasswordpos = models.CharField(db_column='cOperatorNewPasswordPOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bcanchangesessiondate = models.BooleanField(db_column='bCanChangeSessionDate')  # Field name made lowercase.
    ceftoperatorcode = models.CharField(db_column='cEFTOperatorCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    bsupervisoragent = models.BooleanField(db_column='bSupervisorAgent', blank=True, null=True)  # Field name made lowercase.
    blockedout = models.BooleanField(db_column='bLockedOut')  # Field name made lowercase.
    caccessargroupidlst = models.CharField(db_column='cAccessARGroupIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessargroupchklstind = models.CharField(db_column='cAccessARGroupChkLstInd', max_length=1)  # Field name made lowercase.
    bincludearnogroups = models.BooleanField(db_column='bIncludeARNoGroups')  # Field name made lowercase.
    bapplyargroupstoenqrep = models.BooleanField(db_column='bApplyARGroupsToEnqRep', blank=True, null=True)  # Field name made lowercase.
    caccessapgroupidlst = models.CharField(db_column='cAccessAPGroupIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessapgroupchklstind = models.CharField(db_column='cAccessAPGroupChkLstInd', max_length=1)  # Field name made lowercase.
    bincludeapnogroups = models.BooleanField(db_column='bIncludeAPNoGroups')  # Field name made lowercase.
    bapplyapgroupstoenqrep = models.BooleanField(db_column='bApplyAPGroupsToEnqRep', blank=True, null=True)  # Field name made lowercase.
    vbbiometric = models.TextField(db_column='vbBiometric', blank=True, null=True)  # Field name made lowercase.
    fdefmax_ldisc = models.FloatField(db_column='fDefMax_LDisc', blank=True, null=True)  # Field name made lowercase.
    fdefmax_disc = models.FloatField(db_column='fDefMax_Disc', blank=True, null=True)  # Field name made lowercase.
    bapplyaccessrepstoreports = models.BooleanField(db_column='bApplyAccessRepsToReports', blank=True, null=True)  # Field name made lowercase.
    bapplyaccessprojectstoreports = models.BooleanField(db_column='bApplyAccessProjectsToReports', blank=True, null=True)  # Field name made lowercase.
    idposmenusetup = models.IntegerField(db_column='idPOSMenuSetup', blank=True, null=True)  # Field name made lowercase.
    bagentisbuyer = models.BooleanField(db_column='bAgentIsBuyer')  # Field name made lowercase.
    busebiometric = models.BooleanField(db_column='bUseBiometric')  # Field name made lowercase.
    fiscalprinterid = models.IntegerField(db_column='FiscalPrinterId')  # Field name made lowercase.
    fiscaldeviceid = models.IntegerField(db_column='FiscalDeviceId')  # Field name made lowercase.
    csagepayusername = models.CharField(db_column='cSagePayUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csagepaypassword = models.CharField(db_column='cSagePayPassword', max_length=160, blank=True, null=True)  # Field name made lowercase.
    csagepaypin = models.CharField(db_column='cSagePayPIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cvisiblebrancheslst = models.CharField(db_column='cVisibleBranchesLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cvisiblebrancheslstind = models.CharField(db_column='cVisibleBranchesLstInd', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cvisiblewarehouseslst = models.CharField(db_column='cVisibleWarehousesLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cvisiblewarehouseslstind = models.CharField(db_column='cVisibleWarehousesLstInd', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    field_rtblagents_ibranchid = models.IntegerField(db_column='_rtblAgents_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_dcreateddate = models.DateTimeField(db_column='_rtblAgents_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_dmodifieddate = models.DateTimeField(db_column='_rtblAgents_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_icreatedbranchid = models.IntegerField(db_column='_rtblAgents_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_imodifiedbranchid = models.IntegerField(db_column='_rtblAgents_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_icreatedagentid = models.IntegerField(db_column='_rtblAgents_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_imodifiedagentid = models.IntegerField(db_column='_rtblAgents_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_ichangesetid = models.IntegerField(db_column='_rtblAgents_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblagents_checksum = models.TextField(db_column='_rtblAgents_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    caccessdoccatgroupidlst = models.CharField(db_column='cAccessDocCatGroupIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessdoccatgroupchklstind = models.CharField(db_column='cAccessDocCatGroupChkLstInd', max_length=1)  # Field name made lowercase.
    idefdoccatid = models.IntegerField(db_column='iDefDocCatID', blank=True, null=True)  # Field name made lowercase.
    caccessdoccatidlst = models.CharField(db_column='cAccessDocCatIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessdoccatchklstind = models.CharField(db_column='cAccessDocCatChkLstInd', max_length=1)  # Field name made lowercase.
    caccessincidenttypegroupidlst = models.CharField(db_column='cAccessIncidentTypeGroupIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessincidenttypegroupchklstind = models.CharField(db_column='cAccessIncidentTypeGroupChkLstInd', max_length=1)  # Field name made lowercase.
    caccessincidenttypeidlst = models.CharField(db_column='cAccessIncidentTypeIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessincidenttypechklstind = models.CharField(db_column='cAccessIncidentTypeChkLstInd', max_length=1)  # Field name made lowercase.
    iagentloginscreen = models.IntegerField(db_column='iAgentLoginScreen')  # Field name made lowercase.
    caccessprocessflowidlst = models.CharField(db_column='cAccessProcessFlowIDLst', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caccessprocessflowchklstind = models.CharField(db_column='cAccessProcessFlowChkLstInd', max_length=1)  # Field name made lowercase.
    cemailsignature = models.TextField(db_column='cEmailSignature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblAgents'


class Rtblbusclass(models.Model):
    idbusclass = models.AutoField(db_column='idBusClass', primary_key=True)  # Field name made lowercase.
    cbusclass = models.CharField(db_column='cBusClass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblbusclass_ibranchid = models.IntegerField(db_column='_rtblBusClass_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_dcreateddate = models.DateTimeField(db_column='_rtblBusClass_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_dmodifieddate = models.DateTimeField(db_column='_rtblBusClass_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_icreatedbranchid = models.IntegerField(db_column='_rtblBusClass_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_imodifiedbranchid = models.IntegerField(db_column='_rtblBusClass_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_icreatedagentid = models.IntegerField(db_column='_rtblBusClass_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_imodifiedagentid = models.IntegerField(db_column='_rtblBusClass_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_ichangesetid = models.IntegerField(db_column='_rtblBusClass_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusclass_checksum = models.TextField(db_column='_rtblBusClass_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblBusClass'


class Rtblbusdept(models.Model):
    idbusdept = models.AutoField(db_column='idBusDept', primary_key=True)  # Field name made lowercase.
    cbusdept = models.CharField(db_column='cBusDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblbusdept_ibranchid = models.IntegerField(db_column='_rtblBusDept_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_dcreateddate = models.DateTimeField(db_column='_rtblBusDept_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_dmodifieddate = models.DateTimeField(db_column='_rtblBusDept_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_icreatedbranchid = models.IntegerField(db_column='_rtblBusDept_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_imodifiedbranchid = models.IntegerField(db_column='_rtblBusDept_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_icreatedagentid = models.IntegerField(db_column='_rtblBusDept_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_imodifiedagentid = models.IntegerField(db_column='_rtblBusDept_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_ichangesetid = models.IntegerField(db_column='_rtblBusDept_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdept_checksum = models.TextField(db_column='_rtblBusDept_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblBusDept'


class Rtblbusdesig(models.Model):
    idbusdesig = models.AutoField(db_column='idBusDesig', primary_key=True)  # Field name made lowercase.
    cbusdesig = models.CharField(db_column='cBusDesig', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblbusdesig_ibranchid = models.IntegerField(db_column='_rtblBusDesig_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_dcreateddate = models.DateTimeField(db_column='_rtblBusDesig_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_dmodifieddate = models.DateTimeField(db_column='_rtblBusDesig_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_icreatedbranchid = models.IntegerField(db_column='_rtblBusDesig_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_imodifiedbranchid = models.IntegerField(db_column='_rtblBusDesig_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_icreatedagentid = models.IntegerField(db_column='_rtblBusDesig_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_imodifiedagentid = models.IntegerField(db_column='_rtblBusDesig_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_ichangesetid = models.IntegerField(db_column='_rtblBusDesig_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbusdesig_checksum = models.TextField(db_column='_rtblBusDesig_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblBusDesig'


class Rtblbustype(models.Model):
    idbustype = models.AutoField(db_column='idBusType', primary_key=True)  # Field name made lowercase.
    cbustype = models.CharField(db_column='cBusType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblbustype_ibranchid = models.IntegerField(db_column='_rtblBusType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_dcreateddate = models.DateTimeField(db_column='_rtblBusType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_dmodifieddate = models.DateTimeField(db_column='_rtblBusType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_icreatedbranchid = models.IntegerField(db_column='_rtblBusType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_imodifiedbranchid = models.IntegerField(db_column='_rtblBusType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_icreatedagentid = models.IntegerField(db_column='_rtblBusType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_imodifiedagentid = models.IntegerField(db_column='_rtblBusType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_ichangesetid = models.IntegerField(db_column='_rtblBusType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblbustype_checksum = models.TextField(db_column='_rtblBusType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblBusType'


class Rtblcmdefaults(models.Model):
    idcmdefaults = models.AutoField(db_column='idCMDefaults', primary_key=True)  # Field name made lowercase.
    ipeoplefilterstlength = models.IntegerField(db_column='iPeopleFilterStLength', blank=True, null=True)  # Field name made lowercase.
    bautocontracts = models.BooleanField(db_column='bAutoContracts')  # Field name made lowercase.
    vcontractprefix = models.CharField(db_column='vContractPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    icontractpadlength = models.IntegerField(db_column='iContractPadLength', blank=True, null=True)  # Field name made lowercase.
    icontractfilterstlength = models.IntegerField(db_column='iContractFilterStLength', blank=True, null=True)  # Field name made lowercase.
    vkbprefix = models.CharField(db_column='vKBPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ikbpadlength = models.IntegerField(db_column='iKBPadLength', blank=True, null=True)  # Field name made lowercase.
    vincidentprefix = models.CharField(db_column='vIncidentPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iincidentpadlength = models.IntegerField(db_column='iIncidentPadLength', blank=True, null=True)  # Field name made lowercase.
    bincdefagentname = models.BooleanField(db_column='bIncDefAgentName')  # Field name made lowercase.
    bincdispcustnotes = models.BooleanField(db_column='bIncDispCustNotes')  # Field name made lowercase.
    vdocstorepath = models.CharField(db_column='vDocStorePath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    brestrictagents = models.BooleanField(db_column='bRestrictAgents', blank=True, null=True)  # Field name made lowercase.
    brestrictinactiveagents = models.BooleanField(db_column='bRestrictInActiveAgents', blank=True, null=True)  # Field name made lowercase.
    bcolorcodeoverduedate = models.BooleanField(db_column='bColorCodeOverDueDate', blank=True, null=True)  # Field name made lowercase.
    ioverduecolor = models.IntegerField(db_column='iOverDueColor', blank=True, null=True)  # Field name made lowercase.
    bspellcheck = models.BooleanField(db_column='bSpellCheck')  # Field name made lowercase.
    bautoincidents = models.BooleanField(db_column='bAutoIncidents')  # Field name made lowercase.
    bautokb = models.BooleanField(db_column='bAutoKB')  # Field name made lowercase.
    iduedateincrement = models.IntegerField(db_column='iDueDateIncrement', blank=True, null=True)  # Field name made lowercase.
    iduetimeincrement = models.IntegerField(db_column='iDueTimeIncrement', blank=True, null=True)  # Field name made lowercase.
    buseexpcontracts = models.BooleanField(db_column='bUseExpContracts')  # Field name made lowercase.
    buseblockedcontracts = models.BooleanField(db_column='bUseBlockedContracts')  # Field name made lowercase.
    bpostincidentonholdcust = models.BooleanField(db_column='bPostIncidentOnHoldCust')  # Field name made lowercase.
    bsfaopportunityautonum = models.BooleanField(db_column='bSFAOpportunityAutoNum')  # Field name made lowercase.
    csfaopportunitynextnum = models.CharField(db_column='cSFAOpportunityNextNum', max_length=15, blank=True, null=True)  # Field name made lowercase.
    isfaopportunitypadto = models.IntegerField(db_column='iSFAOpportunityPadTo', blank=True, null=True)  # Field name made lowercase.
    csfaopportunityprefix = models.CharField(db_column='cSFAOpportunityPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ideftopportunityincidenttypeid = models.IntegerField(db_column='iDeftOpportunityIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    bsfaapplyagentfilter = models.BooleanField(db_column='bSFAApplyAgentFilter')  # Field name made lowercase.
    bsfausesalesorders = models.BooleanField(db_column='bSFAUseSalesOrders')  # Field name made lowercase.
    isfareopenoppstatusid = models.IntegerField(db_column='iSFAReopenOppStatusID')  # Field name made lowercase.
    isfafilterstlength = models.IntegerField(db_column='iSFAFilterStLength')  # Field name made lowercase.
    bautoemailassignedagent = models.BooleanField(db_column='bAutoEmailAssignedAgent')  # Field name made lowercase.
    idocumentfilterstlength = models.IntegerField(db_column='iDocumentFilterStLength')  # Field name made lowercase.
    bsourcedoclinked = models.BooleanField(db_column='bSourceDocLinked')  # Field name made lowercase.
    isourcedoclinkdisplay = models.IntegerField(db_column='iSourceDocLinkDisplay')  # Field name made lowercase.
    field_rtblcmdefaults_ibranchid = models.IntegerField(db_column='_rtblCMDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_dcreateddate = models.DateTimeField(db_column='_rtblCMDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_dmodifieddate = models.DateTimeField(db_column='_rtblCMDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_icreatedbranchid = models.IntegerField(db_column='_rtblCMDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_imodifiedbranchid = models.IntegerField(db_column='_rtblCMDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_icreatedagentid = models.IntegerField(db_column='_rtblCMDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_imodifiedagentid = models.IntegerField(db_column='_rtblCMDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_ichangesetid = models.IntegerField(db_column='_rtblCMDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcmdefaults_checksum = models.TextField(db_column='_rtblCMDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblCMDefaults'


class Rtblclass(models.Model):
    idclass = models.IntegerField(db_column='idClass', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bavailable = models.BooleanField(db_column='bAvailable')  # Field name made lowercase.
    field_rtblclass_ibranchid = models.IntegerField(db_column='_rtblClass_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_dcreateddate = models.DateTimeField(db_column='_rtblClass_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_dmodifieddate = models.DateTimeField(db_column='_rtblClass_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_icreatedbranchid = models.IntegerField(db_column='_rtblClass_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_imodifiedbranchid = models.IntegerField(db_column='_rtblClass_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_icreatedagentid = models.IntegerField(db_column='_rtblClass_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_imodifiedagentid = models.IntegerField(db_column='_rtblClass_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_ichangesetid = models.IntegerField(db_column='_rtblClass_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblclass_checksum = models.TextField(db_column='_rtblClass_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblClass'


class Rtblcompetitor(models.Model):
    idcompetitor = models.AutoField(db_column='idCompetitor', primary_key=True)  # Field name made lowercase.
    ccompanyname = models.CharField(db_column='cCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field_rtblcompetitor_ibranchid = models.IntegerField(db_column='_rtblCompetitor_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_dcreateddate = models.DateTimeField(db_column='_rtblCompetitor_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_dmodifieddate = models.DateTimeField(db_column='_rtblCompetitor_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_icreatedbranchid = models.IntegerField(db_column='_rtblCompetitor_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_imodifiedbranchid = models.IntegerField(db_column='_rtblCompetitor_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_icreatedagentid = models.IntegerField(db_column='_rtblCompetitor_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_imodifiedagentid = models.IntegerField(db_column='_rtblCompetitor_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_ichangesetid = models.IntegerField(db_column='_rtblCompetitor_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitor_checksum = models.TextField(db_column='_rtblCompetitor_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblCompetitor'


class Rtblcompetitorproduct(models.Model):
    idcompetitorproduct = models.AutoField(db_column='IDCompetitorProduct', primary_key=True)  # Field name made lowercase.
    cproductname = models.CharField(db_column='cProductName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cdetaileddescription = models.CharField(db_column='cDetailedDescription', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    field_rtblcompetitorproduct_ibranchid = models.IntegerField(db_column='_rtblCompetitorProduct_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_dcreateddate = models.DateTimeField(db_column='_rtblCompetitorProduct_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_dmodifieddate = models.DateTimeField(db_column='_rtblCompetitorProduct_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_icreatedbranchid = models.IntegerField(db_column='_rtblCompetitorProduct_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_imodifiedbranchid = models.IntegerField(db_column='_rtblCompetitorProduct_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_icreatedagentid = models.IntegerField(db_column='_rtblCompetitorProduct_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_imodifiedagentid = models.IntegerField(db_column='_rtblCompetitorProduct_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_ichangesetid = models.IntegerField(db_column='_rtblCompetitorProduct_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproduct_checksum = models.TextField(db_column='_rtblCompetitorProduct_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblCompetitorProduct'


class Rtblcompetitorproductlink(models.Model):
    idcompetitorproductlink = models.AutoField(db_column='idCompetitorProductLink', primary_key=True)  # Field name made lowercase.
    icompetitorid = models.IntegerField(db_column='iCompetitorID')  # Field name made lowercase.
    icompetitorproductid = models.IntegerField(db_column='iCompetitorProductID')  # Field name made lowercase.
    fproductprice = models.FloatField(db_column='fProductPrice', blank=True, null=True)  # Field name made lowercase.
    ddtpriceupdated = models.DateTimeField(db_column='dDtPriceUpdated', blank=True, null=True)  # Field name made lowercase.
    field_rtblcompetitorproductlink_ibranchid = models.IntegerField(db_column='_rtblCompetitorProductLink_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_dcreateddate = models.DateTimeField(db_column='_rtblCompetitorProductLink_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_dmodifieddate = models.DateTimeField(db_column='_rtblCompetitorProductLink_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_icreatedbranchid = models.IntegerField(db_column='_rtblCompetitorProductLink_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_imodifiedbranchid = models.IntegerField(db_column='_rtblCompetitorProductLink_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_icreatedagentid = models.IntegerField(db_column='_rtblCompetitorProductLink_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_imodifiedagentid = models.IntegerField(db_column='_rtblCompetitorProductLink_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_ichangesetid = models.IntegerField(db_column='_rtblCompetitorProductLink_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcompetitorproductlink_checksum = models.TextField(db_column='_rtblCompetitorProductLink_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblCompetitorProductLink'


class Rtblcontractdoclinks(models.Model):
    iddoclinks = models.AutoField(db_column='idDocLinks', primary_key=True)  # Field name made lowercase.
    idocstoreid = models.IntegerField(db_column='iDocStoreID', blank=True, null=True)  # Field name made lowercase.
    ilinksource = models.IntegerField(db_column='iLinkSource', blank=True, null=True)  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID', blank=True, null=True)  # Field name made lowercase.
    field_rtblcontractdoclinks_ibranchid = models.IntegerField(db_column='_rtblContractDocLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_dcreateddate = models.DateTimeField(db_column='_rtblContractDocLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_dmodifieddate = models.DateTimeField(db_column='_rtblContractDocLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_icreatedbranchid = models.IntegerField(db_column='_rtblContractDocLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_imodifiedbranchid = models.IntegerField(db_column='_rtblContractDocLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_icreatedagentid = models.IntegerField(db_column='_rtblContractDocLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_imodifiedagentid = models.IntegerField(db_column='_rtblContractDocLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_ichangesetid = models.IntegerField(db_column='_rtblContractDocLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontractdoclinks_checksum = models.TextField(db_column='_rtblContractDocLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblContractDocLinks'


class Rtblcontracttemplates(models.Model):
    idcontracttemplates = models.AutoField(db_column='idContractTemplates', primary_key=True)  # Field name made lowercase.
    ctemplatename = models.CharField(db_column='cTemplateName', max_length=50)  # Field name made lowercase.
    idefyears = models.IntegerField(db_column='iDefYears')  # Field name made lowercase.
    idefmonths = models.IntegerField(db_column='iDefMonths')  # Field name made lowercase.
    idefdays = models.IntegerField(db_column='iDefDays')  # Field name made lowercase.
    ibilltype = models.IntegerField(db_column='iBillType')  # Field name made lowercase.
    itimeunit = models.IntegerField(db_column='iTimeUnit')  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount')  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    ballowoverride = models.BooleanField(db_column='bAllowOverride')  # Field name made lowercase.
    icinvtemplateid = models.IntegerField(db_column='iCInvTemplateID', blank=True, null=True)  # Field name made lowercase.
    irrconfigurationid = models.IntegerField(db_column='iRRConfigurationID', blank=True, null=True)  # Field name made lowercase.
    field_rtblcontracttemplates_ibranchid = models.IntegerField(db_column='_rtblContractTemplates_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_dcreateddate = models.DateTimeField(db_column='_rtblContractTemplates_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_dmodifieddate = models.DateTimeField(db_column='_rtblContractTemplates_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_icreatedbranchid = models.IntegerField(db_column='_rtblContractTemplates_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_imodifiedbranchid = models.IntegerField(db_column='_rtblContractTemplates_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_icreatedagentid = models.IntegerField(db_column='_rtblContractTemplates_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_imodifiedagentid = models.IntegerField(db_column='_rtblContractTemplates_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_ichangesetid = models.IntegerField(db_column='_rtblContractTemplates_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttemplates_checksum = models.TextField(db_column='_rtblContractTemplates_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblContractTemplates'


class Rtblcontracttx(models.Model):
    idcontracttx = models.AutoField(db_column='idContractTx', primary_key=True)  # Field name made lowercase.
    ddate = models.DateTimeField(db_column='dDate')  # Field name made lowercase.
    icontractid = models.IntegerField(db_column='iContractID')  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount')  # Field name made lowercase.
    idurationmins = models.IntegerField(db_column='iDurationMins')  # Field name made lowercase.
    dtimestamp = models.DateTimeField(db_column='dTimeStamp', blank=True, null=True)  # Field name made lowercase.
    ctxinvoice = models.CharField(db_column='cTxInvoice', max_length=30, blank=True, null=True)  # Field name made lowercase.
    field_rtblcontracttx_ibranchid = models.IntegerField(db_column='_rtblContractTx_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_dcreateddate = models.DateTimeField(db_column='_rtblContractTx_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_dmodifieddate = models.DateTimeField(db_column='_rtblContractTx_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_icreatedbranchid = models.IntegerField(db_column='_rtblContractTx_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_imodifiedbranchid = models.IntegerField(db_column='_rtblContractTx_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_icreatedagentid = models.IntegerField(db_column='_rtblContractTx_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_imodifiedagentid = models.IntegerField(db_column='_rtblContractTx_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_ichangesetid = models.IntegerField(db_column='_rtblContractTx_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracttx_checksum = models.TextField(db_column='_rtblContractTx_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblContractTx'


class Rtblcontracts(models.Model):
    idcontracts = models.AutoField(db_column='idContracts', primary_key=True)  # Field name made lowercase.
    ccontractnumber = models.CharField(db_column='cContractNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idebtorid = models.IntegerField(db_column='iDebtorID')  # Field name made lowercase.
    ccontractname = models.CharField(db_column='cContractName', max_length=50)  # Field name made lowercase.
    ccontractreference = models.CharField(db_column='cContractReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dcreated = models.DateTimeField(db_column='dCreated', blank=True, null=True)  # Field name made lowercase.
    dstartdate = models.DateTimeField(db_column='dStartDate')  # Field name made lowercase.
    denddate = models.DateTimeField(db_column='dEndDate')  # Field name made lowercase.
    ibilltype = models.IntegerField(db_column='iBillType')  # Field name made lowercase.
    itimeunit = models.IntegerField(db_column='iTimeUnit')  # Field name made lowercase.
    famount = models.FloatField(db_column='fAmount')  # Field name made lowercase.
    bblock = models.BooleanField(db_column='bBlock')  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    ballowoverride = models.BooleanField(db_column='bAllowOverride')  # Field name made lowercase.
    cinvoice = models.CharField(db_column='cInvoice', max_length=30, blank=True, null=True)  # Field name made lowercase.
    iunitsused = models.IntegerField(db_column='iUnitsUsed')  # Field name made lowercase.
    irecurrtransid = models.IntegerField(db_column='iRecurrTransID', blank=True, null=True)  # Field name made lowercase.
    bextendenddate = models.BooleanField(db_column='bExtendEndDate')  # Field name made lowercase.
    field_rtblcontracts_ibranchid = models.IntegerField(db_column='_rtblContracts_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_dcreateddate = models.DateTimeField(db_column='_rtblContracts_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_dmodifieddate = models.DateTimeField(db_column='_rtblContracts_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_icreatedbranchid = models.IntegerField(db_column='_rtblContracts_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_imodifiedbranchid = models.IntegerField(db_column='_rtblContracts_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_icreatedagentid = models.IntegerField(db_column='_rtblContracts_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_imodifiedagentid = models.IntegerField(db_column='_rtblContracts_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_ichangesetid = models.IntegerField(db_column='_rtblContracts_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcontracts_checksum = models.TextField(db_column='_rtblContracts_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblContracts'


class Rtblcountry(models.Model):
    idcountry = models.AutoField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    ccountryname = models.CharField(db_column='cCountryName', max_length=30)  # Field name made lowercase.
    field_rtblcountry_ibranchid = models.IntegerField(db_column='_rtblCountry_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_dcreateddate = models.DateTimeField(db_column='_rtblCountry_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_dmodifieddate = models.DateTimeField(db_column='_rtblCountry_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_icreatedbranchid = models.IntegerField(db_column='_rtblCountry_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_imodifiedbranchid = models.IntegerField(db_column='_rtblCountry_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_icreatedagentid = models.IntegerField(db_column='_rtblCountry_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_imodifiedagentid = models.IntegerField(db_column='_rtblCountry_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_ichangesetid = models.IntegerField(db_column='_rtblCountry_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblcountry_checksum = models.TextField(db_column='_rtblCountry_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblCountry'


class Rtbldoccat(models.Model):
    iddoccat = models.AutoField(db_column='idDocCat', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=64)  # Field name made lowercase.
    field_rtbldoccat_ibranchid = models.IntegerField(db_column='_rtblDocCat_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_dcreateddate = models.DateTimeField(db_column='_rtblDocCat_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_dmodifieddate = models.DateTimeField(db_column='_rtblDocCat_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_icreatedbranchid = models.IntegerField(db_column='_rtblDocCat_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_imodifiedbranchid = models.IntegerField(db_column='_rtblDocCat_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_icreatedagentid = models.IntegerField(db_column='_rtblDocCat_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_imodifiedagentid = models.IntegerField(db_column='_rtblDocCat_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_ichangesetid = models.IntegerField(db_column='_rtblDocCat_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoccat_checksum = models.TextField(db_column='_rtblDocCat_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblDocCat'


class Rtbldoclinks(models.Model):
    iddoclinks = models.AutoField(db_column='idDocLinks', primary_key=True)  # Field name made lowercase.
    idocstoreid = models.IntegerField(db_column='iDocStoreID')  # Field name made lowercase.
    ilinksource = models.IntegerField(db_column='iLinkSource')  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID')  # Field name made lowercase.
    field_rtbldoclinks_ibranchid = models.IntegerField(db_column='_rtblDocLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_dcreateddate = models.DateTimeField(db_column='_rtblDocLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_dmodifieddate = models.DateTimeField(db_column='_rtblDocLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_icreatedbranchid = models.IntegerField(db_column='_rtblDocLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_imodifiedbranchid = models.IntegerField(db_column='_rtblDocLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_icreatedagentid = models.IntegerField(db_column='_rtblDocLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_imodifiedagentid = models.IntegerField(db_column='_rtblDocLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_ichangesetid = models.IntegerField(db_column='_rtblDocLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldoclinks_checksum = models.TextField(db_column='_rtblDocLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblDocLinks'


class Rtbldocstore(models.Model):
    iddocstore = models.AutoField(db_column='idDocStore', primary_key=True)  # Field name made lowercase.
    cdocstorename = models.CharField(db_column='cDocStoreName', max_length=20)  # Field name made lowercase.
    cdocname = models.CharField(db_column='cDocName', max_length=255)  # Field name made lowercase.
    idoccatid = models.IntegerField(db_column='iDocCatID', blank=True, null=True)  # Field name made lowercase.
    cdocdescription = models.CharField(db_column='cDocDescription', max_length=255)  # Field name made lowercase.
    dmodified = models.DateTimeField(db_column='dModified')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    nicon = models.BinaryField(db_column='nIcon', blank=True, null=True)  # Field name made lowercase.
    bisactive = models.BooleanField(db_column='bIsActive')  # Field name made lowercase.
    field_rtbldocstore_ibranchid = models.IntegerField(db_column='_rtblDocStore_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_dcreateddate = models.DateTimeField(db_column='_rtblDocStore_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_dmodifieddate = models.DateTimeField(db_column='_rtblDocStore_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_icreatedbranchid = models.IntegerField(db_column='_rtblDocStore_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_imodifiedbranchid = models.IntegerField(db_column='_rtblDocStore_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_icreatedagentid = models.IntegerField(db_column='_rtblDocStore_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_imodifiedagentid = models.IntegerField(db_column='_rtblDocStore_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_ichangesetid = models.IntegerField(db_column='_rtblDocStore_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbldocstore_checksum = models.TextField(db_column='_rtblDocStore_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblDocStore'


class Rtblescalategrp(models.Model):
    idescalategrp = models.AutoField(db_column='idEscalateGrp', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=30)  # Field name made lowercase.
    field_rtblescalategrp_ibranchid = models.IntegerField(db_column='_rtblEscalateGrp_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_dcreateddate = models.DateTimeField(db_column='_rtblEscalateGrp_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_dmodifieddate = models.DateTimeField(db_column='_rtblEscalateGrp_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_icreatedbranchid = models.IntegerField(db_column='_rtblEscalateGrp_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_imodifiedbranchid = models.IntegerField(db_column='_rtblEscalateGrp_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_icreatedagentid = models.IntegerField(db_column='_rtblEscalateGrp_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_imodifiedagentid = models.IntegerField(db_column='_rtblEscalateGrp_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_ichangesetid = models.IntegerField(db_column='_rtblEscalateGrp_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrp_checksum = models.TextField(db_column='_rtblEscalateGrp_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblEscalateGrp'


class Rtblescalategrpmembers(models.Model):
    idescalategrpmembers = models.AutoField(db_column='idEscalateGrpMembers', primary_key=True)  # Field name made lowercase.
    iescalategrpid = models.IntegerField(db_column='iEscalateGrpID')  # Field name made lowercase.
    iagentgroupid = models.IntegerField(db_column='iAgentGroupID')  # Field name made lowercase.
    isequence = models.IntegerField(db_column='iSequence')  # Field name made lowercase.
    iescalatemins = models.IntegerField(db_column='iEscalateMins')  # Field name made lowercase.
    field_rtblescalategrpmembers_ibranchid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_dcreateddate = models.DateTimeField(db_column='_rtblEscalateGrpMembers_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_dmodifieddate = models.DateTimeField(db_column='_rtblEscalateGrpMembers_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_icreatedbranchid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_imodifiedbranchid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_icreatedagentid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_imodifiedagentid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_ichangesetid = models.IntegerField(db_column='_rtblEscalateGrpMembers_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblescalategrpmembers_checksum = models.TextField(db_column='_rtblEscalateGrpMembers_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblEscalateGrpMembers'


class Rtblincidentaction(models.Model):
    idincidentaction = models.IntegerField(db_column='idIncidentAction', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cpdescription = models.CharField(db_column='cPDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentaction_ibranchid = models.IntegerField(db_column='_rtblIncidentAction_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_dcreateddate = models.DateTimeField(db_column='_rtblIncidentAction_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentAction_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentAction_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentAction_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_icreatedagentid = models.IntegerField(db_column='_rtblIncidentAction_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentAction_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_ichangesetid = models.IntegerField(db_column='_rtblIncidentAction_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentaction_checksum = models.TextField(db_column='_rtblIncidentAction_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentAction'


class Rtblincidentcat(models.Model):
    idincidentcat = models.AutoField(db_column='idIncidentCat', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentcat_ibranchid = models.IntegerField(db_column='_rtblIncidentCat_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_dcreateddate = models.DateTimeField(db_column='_rtblIncidentCat_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentCat_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentCat_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentCat_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_icreatedagentid = models.IntegerField(db_column='_rtblIncidentCat_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentCat_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_ichangesetid = models.IntegerField(db_column='_rtblIncidentCat_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentcat_checksum = models.TextField(db_column='_rtblIncidentCat_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentCat'


class Rtblincidentlog(models.Model):
    idincidentlog = models.AutoField(db_column='idIncidentLog', primary_key=True)  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    dactiondate = models.DateTimeField(db_column='dActionDate')  # Field name made lowercase.
    iincidentactionid = models.IntegerField(db_column='iIncidentActionID')  # Field name made lowercase.
    cresolution = models.TextField(db_column='cResolution', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    bproxy = models.BooleanField(db_column='bProxy')  # Field name made lowercase.
    inewagentid = models.IntegerField(db_column='iNewAgentID', blank=True, null=True)  # Field name made lowercase.
    csourcecontent = models.TextField(db_column='cSourceContent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csourceid = models.CharField(db_column='cSourceID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    irejectreasonid = models.IntegerField(db_column='iRejectReasonID', blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentlog_ibranchid = models.IntegerField(db_column='_rtblIncidentLog_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_dcreateddate = models.DateTimeField(db_column='_rtblIncidentLog_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentLog_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentLog_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentLog_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_icreatedagentid = models.IntegerField(db_column='_rtblIncidentLog_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentLog_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_ichangesetid = models.IntegerField(db_column='_rtblIncidentLog_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_checksum = models.TextField(db_column='_rtblIncidentLog_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentLog'


class RtblincidentlogArchive(models.Model):
    idincidentlog = models.IntegerField(db_column='idIncidentLog', primary_key=True)  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    dactiondate = models.DateTimeField(db_column='dActionDate')  # Field name made lowercase.
    iincidentactionid = models.IntegerField(db_column='iIncidentActionID')  # Field name made lowercase.
    cresolution = models.TextField(db_column='cResolution', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    bproxy = models.BooleanField(db_column='bProxy')  # Field name made lowercase.
    inewagentid = models.IntegerField(db_column='iNewAgentID', blank=True, null=True)  # Field name made lowercase.
    csourcecontent = models.TextField(db_column='cSourceContent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csourceid = models.CharField(db_column='cSourceID', max_length=128)  # Field name made lowercase.
    irejectreasonid = models.IntegerField(db_column='iRejectReasonID', blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentlog_archive_ibranchid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_dcreateddate = models.DateTimeField(db_column='_rtblIncidentLog_Archive_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentLog_Archive_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_icreatedagentid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_ichangesetid = models.IntegerField(db_column='_rtblIncidentLog_Archive_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentlog_archive_checksum = models.TextField(db_column='_rtblIncidentLog_Archive_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentLog_Archive'


class Rtblincidentpriority(models.Model):
    idincidentpriority = models.IntegerField(db_column='idIncidentPriority', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    icolor = models.IntegerField(db_column='iColor', blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault', blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentpriority_ibranchid = models.IntegerField(db_column='_rtblIncidentPriority_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_dcreateddate = models.DateTimeField(db_column='_rtblIncidentPriority_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentPriority_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentPriority_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentPriority_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_icreatedagentid = models.IntegerField(db_column='_rtblIncidentPriority_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentPriority_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_ichangesetid = models.IntegerField(db_column='_rtblIncidentPriority_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentpriority_checksum = models.TextField(db_column='_rtblIncidentPriority_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentPriority'


class Rtblincidentstatus(models.Model):
    idincidentstatus = models.IntegerField(db_column='idIncidentStatus', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=32, blank=True, null=True)  # Field name made lowercase.
    field_rtblincidentstatus_ibranchid = models.IntegerField(db_column='_rtblIncidentStatus_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_dcreateddate = models.DateTimeField(db_column='_rtblIncidentStatus_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentStatus_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentStatus_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentStatus_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_icreatedagentid = models.IntegerField(db_column='_rtblIncidentStatus_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentStatus_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_ichangesetid = models.IntegerField(db_column='_rtblIncidentStatus_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidentstatus_checksum = models.TextField(db_column='_rtblIncidentStatus_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentStatus'


class Rtblincidenttemplates(models.Model):
    idincidenttemplates = models.AutoField(db_column='idIncidentTemplates', primary_key=True)  # Field name made lowercase.
    ctemplatename = models.CharField(db_column='cTemplateName', max_length=32)  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    field_rtblincidenttemplates_ibranchid = models.IntegerField(db_column='_rtblIncidentTemplates_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_dcreateddate = models.DateTimeField(db_column='_rtblIncidentTemplates_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentTemplates_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentTemplates_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentTemplates_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_icreatedagentid = models.IntegerField(db_column='_rtblIncidentTemplates_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentTemplates_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_ichangesetid = models.IntegerField(db_column='_rtblIncidentTemplates_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttemplates_checksum = models.TextField(db_column='_rtblIncidentTemplates_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentTemplates'


class Rtblincidenttype(models.Model):
    idincidenttype = models.AutoField(db_column='idIncidentType', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50)  # Field name made lowercase.
    iescgroupid = models.IntegerField(db_column='iEscGroupID', blank=True, null=True)  # Field name made lowercase.
    ballowoverride = models.BooleanField(db_column='bAllowOverride')  # Field name made lowercase.
    brequirecontract = models.BooleanField(db_column='bRequireContract')  # Field name made lowercase.
    iincidenttypegroupid = models.IntegerField(db_column='iIncidentTypeGroupID', blank=True, null=True)  # Field name made lowercase.
    iworkflowid = models.IntegerField(db_column='iWorkflowID', blank=True, null=True)  # Field name made lowercase.
    ballowoverrideincidenttype = models.BooleanField(db_column='bAllowOverrideIncidentType')  # Field name made lowercase.
    bpoincidenttype = models.BooleanField(db_column='bPOIncidentType')  # Field name made lowercase.
    cdefaultoutline = models.CharField(db_column='cDefaultOutline', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    bactive = models.BooleanField(db_column='bActive')  # Field name made lowercase.
    field_rtblincidenttype_ibranchid = models.IntegerField(db_column='_rtblIncidentType_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_dcreateddate = models.DateTimeField(db_column='_rtblIncidentType_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_dmodifieddate = models.DateTimeField(db_column='_rtblIncidentType_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_icreatedbranchid = models.IntegerField(db_column='_rtblIncidentType_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidentType_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_icreatedagentid = models.IntegerField(db_column='_rtblIncidentType_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_imodifiedagentid = models.IntegerField(db_column='_rtblIncidentType_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_ichangesetid = models.IntegerField(db_column='_rtblIncidentType_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidenttype_checksum = models.TextField(db_column='_rtblIncidentType_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblIncidentType'


class Rtblincidents(models.Model):
    idincidents = models.AutoField(db_column='idIncidents', primary_key=True)  # Field name made lowercase.
    dcreated = models.DateTimeField(db_column='dCreated')  # Field name made lowercase.
    dlastmodified = models.DateTimeField(db_column='dLastModified')  # Field name made lowercase.
    iclassid = models.IntegerField(db_column='iClassID')  # Field name made lowercase.
    iincidentstatusid = models.IntegerField(db_column='iIncidentStatusID')  # Field name made lowercase.
    brequireack = models.BooleanField(db_column='bRequireAck')  # Field name made lowercase.
    idebtorid = models.IntegerField(db_column='iDebtorID')  # Field name made lowercase.
    ipersonid = models.IntegerField(db_column='iPersonID')  # Field name made lowercase.
    iincidentcatid = models.IntegerField(db_column='iIncidentCatID', blank=True, null=True)  # Field name made lowercase.
    courref = models.CharField(db_column='cOurRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyourref = models.CharField(db_column='cYourRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coutline = models.CharField(db_column='cOutline', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ipriorityid = models.IntegerField(db_column='iPriorityID')  # Field name made lowercase.
    iescalategrpid = models.IntegerField(db_column='iEscalateGrpID')  # Field name made lowercase.
    iagentgroupid = models.IntegerField(db_column='iAgentGroupID')  # Field name made lowercase.
    icurrentagentid = models.IntegerField(db_column='iCurrentAgentID')  # Field name made lowercase.
    icontracttxid = models.IntegerField(db_column='iContractTxID')  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iprivnode = models.IntegerField(db_column='iPrivNode', blank=True, null=True)  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID')  # Field name made lowercase.
    ddueby = models.DateTimeField(db_column='dDueBy', blank=True, null=True)  # Field name made lowercase.
    iduration = models.IntegerField(db_column='iDuration', blank=True, null=True)  # Field name made lowercase.
    icontractid = models.IntegerField(db_column='iContractID', blank=True, null=True)  # Field name made lowercase.
    cchangelog = models.TextField(db_column='cChangeLog', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iincidenttypegroupid = models.IntegerField(db_column='iIncidentTypeGroupID', blank=True, null=True)  # Field name made lowercase.
    iworkflowid = models.IntegerField(db_column='iWorkflowID', blank=True, null=True)  # Field name made lowercase.
    iworkflowstatusid = models.IntegerField(db_column='iWorkflowStatusID', blank=True, null=True)  # Field name made lowercase.
    bhasbeenrejected = models.BooleanField(db_column='bHasBeenRejected')  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID', blank=True, null=True)  # Field name made lowercase.
    ifixedassetid = models.IntegerField(db_column='iFixedAssetID', blank=True, null=True)  # Field name made lowercase.
    iemployeeid = models.IntegerField(db_column='iEmployeeID', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.
    ijobcostingid = models.IntegerField(db_column='iJobCostingID', blank=True, null=True)  # Field name made lowercase.
    iprospectid = models.IntegerField(db_column='iProspectID')  # Field name made lowercase.
    iopportunityid = models.IntegerField(db_column='iOpportunityID')  # Field name made lowercase.
    ipoinvoiceid = models.BigIntegerField(db_column='iPOInvoiceID')  # Field name made lowercase.
    bpoviewed = models.BooleanField(db_column='bPOViewed')  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionID')  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID', blank=True, null=True)  # Field name made lowercase.
    irfqid = models.IntegerField(db_column='iRfqID', blank=True, null=True)  # Field name made lowercase.
    isimreqid = models.IntegerField(db_column='iSIMReqID', blank=True, null=True)  # Field name made lowercase.
    field_rtblincidents_ibranchid = models.IntegerField(db_column='_rtblIncidents_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_dcreateddate = models.DateTimeField(db_column='_rtblIncidents_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_dmodifieddate = models.DateTimeField(db_column='_rtblIncidents_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_icreatedbranchid = models.IntegerField(db_column='_rtblIncidents_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidents_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_icreatedagentid = models.IntegerField(db_column='_rtblIncidents_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_imodifiedagentid = models.IntegerField(db_column='_rtblIncidents_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_ichangesetid = models.IntegerField(db_column='_rtblIncidents_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_checksum = models.TextField(db_column='_rtblIncidents_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ipmtrecid = models.IntegerField(db_column='iPmtRecId')  # Field name made lowercase.
    ijrbatchid = models.IntegerField(db_column='iJrBatchId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblIncidents'


class RtblincidentsArchive(models.Model):
    idincidents = models.AutoField(db_column='idIncidents', primary_key=True)  # Field name made lowercase.
    dcreated = models.DateTimeField(db_column='dCreated')  # Field name made lowercase.
    dlastmodified = models.DateTimeField(db_column='dLastModified')  # Field name made lowercase.
    iclassid = models.IntegerField(db_column='iClassID')  # Field name made lowercase.
    iincidentstatusid = models.IntegerField(db_column='iIncidentStatusID')  # Field name made lowercase.
    brequireack = models.BooleanField(db_column='bRequireAck')  # Field name made lowercase.
    idebtorid = models.IntegerField(db_column='iDebtorID')  # Field name made lowercase.
    ipersonid = models.IntegerField(db_column='iPersonID')  # Field name made lowercase.
    iincidentcatid = models.IntegerField(db_column='iIncidentCatID', blank=True, null=True)  # Field name made lowercase.
    courref = models.CharField(db_column='cOurRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyourref = models.CharField(db_column='cYourRef', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coutline = models.CharField(db_column='cOutline', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ipriorityid = models.IntegerField(db_column='iPriorityID')  # Field name made lowercase.
    iescalategrpid = models.IntegerField(db_column='iEscalateGrpID')  # Field name made lowercase.
    iagentgroupid = models.IntegerField(db_column='iAgentGroupID')  # Field name made lowercase.
    icurrentagentid = models.IntegerField(db_column='iCurrentAgentID')  # Field name made lowercase.
    icontracttxid = models.IntegerField(db_column='iContractTxID')  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    iprivnode = models.IntegerField(db_column='iPrivNode', blank=True, null=True)  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID')  # Field name made lowercase.
    ddueby = models.DateTimeField(db_column='dDueBy', blank=True, null=True)  # Field name made lowercase.
    iduration = models.IntegerField(db_column='iDuration', blank=True, null=True)  # Field name made lowercase.
    icontractid = models.IntegerField(db_column='iContractID', blank=True, null=True)  # Field name made lowercase.
    cchangelog = models.TextField(db_column='cChangeLog', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iincidenttypegroupid = models.IntegerField(db_column='iIncidentTypeGroupID', blank=True, null=True)  # Field name made lowercase.
    iworkflowid = models.IntegerField(db_column='iWorkflowID', blank=True, null=True)  # Field name made lowercase.
    iworkflowstatusid = models.IntegerField(db_column='iWorkflowStatusID', blank=True, null=True)  # Field name made lowercase.
    bhasbeenrejected = models.BooleanField(db_column='bHasBeenRejected')  # Field name made lowercase.
    isupplierid = models.IntegerField(db_column='iSupplierID', blank=True, null=True)  # Field name made lowercase.
    ifixedassetid = models.IntegerField(db_column='iFixedAssetID', blank=True, null=True)  # Field name made lowercase.
    iemployeeid = models.IntegerField(db_column='iEmployeeID', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.
    ijobcostingid = models.IntegerField(db_column='iJobCostingID', blank=True, null=True)  # Field name made lowercase.
    iprospectid = models.IntegerField(db_column='iProspectID')  # Field name made lowercase.
    iopportunityid = models.IntegerField(db_column='iOpportunityID')  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionID')  # Field name made lowercase.
    bpoviewed = models.BooleanField(db_column='bPOViewed', blank=True, null=True)  # Field name made lowercase.
    ipoinvoiceid = models.BigIntegerField(db_column='iPOInvoiceID')  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID', blank=True, null=True)  # Field name made lowercase.
    irfqid = models.IntegerField(db_column='iRfqID', blank=True, null=True)  # Field name made lowercase.
    isimreqid = models.IntegerField(db_column='iSIMReqID', blank=True, null=True)  # Field name made lowercase.
    field_rtblincidents_archive_ibranchid = models.IntegerField(db_column='_rtblIncidents_Archive_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_dcreateddate = models.DateTimeField(db_column='_rtblIncidents_Archive_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_dmodifieddate = models.DateTimeField(db_column='_rtblIncidents_Archive_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_icreatedbranchid = models.IntegerField(db_column='_rtblIncidents_Archive_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_imodifiedbranchid = models.IntegerField(db_column='_rtblIncidents_Archive_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_icreatedagentid = models.IntegerField(db_column='_rtblIncidents_Archive_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_imodifiedagentid = models.IntegerField(db_column='_rtblIncidents_Archive_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_ichangesetid = models.IntegerField(db_column='_rtblIncidents_Archive_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblincidents_archive_checksum = models.TextField(db_column='_rtblIncidents_Archive_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    ipmtrecid = models.IntegerField(db_column='iPmtRecId')  # Field name made lowercase.
    ijrbatchid = models.IntegerField(db_column='iJrBatchId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblIncidents_Archive'


class Rtblkbadoclinks(models.Model):
    iddoclinks = models.AutoField(db_column='idDocLinks', primary_key=True)  # Field name made lowercase.
    idocstoreid = models.IntegerField(db_column='iDocStoreID', blank=True, null=True)  # Field name made lowercase.
    ilinksource = models.IntegerField(db_column='iLinkSource', blank=True, null=True)  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID', blank=True, null=True)  # Field name made lowercase.
    field_rtblkbadoclinks_ibranchid = models.IntegerField(db_column='_rtblKBADocLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_dcreateddate = models.DateTimeField(db_column='_rtblKBADocLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_dmodifieddate = models.DateTimeField(db_column='_rtblKBADocLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_icreatedbranchid = models.IntegerField(db_column='_rtblKBADocLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_imodifiedbranchid = models.IntegerField(db_column='_rtblKBADocLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_icreatedagentid = models.IntegerField(db_column='_rtblKBADocLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_imodifiedagentid = models.IntegerField(db_column='_rtblKBADocLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_ichangesetid = models.IntegerField(db_column='_rtblKBADocLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbadoclinks_checksum = models.TextField(db_column='_rtblKBADocLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKBADocLinks'


class Rtblkbcategorylinks(models.Model):
    idcategorylinks = models.AutoField(db_column='idCategoryLinks', primary_key=True)  # Field name made lowercase.
    iknowledgebaseid = models.IntegerField(db_column='iKnowledgeBaseID')  # Field name made lowercase.
    iknowledgebasecatvalueid = models.IntegerField(db_column='iKnowledgeBaseCatValueID')  # Field name made lowercase.
    bselected = models.BooleanField(db_column='bSelected')  # Field name made lowercase.
    field_rtblkbcategorylinks_ibranchid = models.IntegerField(db_column='_rtblKBCategoryLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_dcreateddate = models.DateTimeField(db_column='_rtblKBCategoryLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_dmodifieddate = models.DateTimeField(db_column='_rtblKBCategoryLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_icreatedbranchid = models.IntegerField(db_column='_rtblKBCategoryLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_imodifiedbranchid = models.IntegerField(db_column='_rtblKBCategoryLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_icreatedagentid = models.IntegerField(db_column='_rtblKBCategoryLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_imodifiedagentid = models.IntegerField(db_column='_rtblKBCategoryLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_ichangesetid = models.IntegerField(db_column='_rtblKBCategoryLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbcategorylinks_checksum = models.TextField(db_column='_rtblKBCategoryLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKBCategoryLinks'


class Rtblkbdescriptionlinks(models.Model):
    iddescriptionlinks = models.AutoField(db_column='idDescriptionLinks', primary_key=True)  # Field name made lowercase.
    iknowledgebaseid = models.IntegerField(db_column='iKnowledgeBaseID')  # Field name made lowercase.
    idescriptionid = models.IntegerField(db_column='iDescriptionID')  # Field name made lowercase.
    cdescription = models.TextField(db_column='cDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_rtblkbdescriptionlinks_ibranchid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_dcreateddate = models.DateTimeField(db_column='_rtblKBDescriptionLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_dmodifieddate = models.DateTimeField(db_column='_rtblKBDescriptionLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_icreatedbranchid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_imodifiedbranchid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_icreatedagentid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_imodifiedagentid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_ichangesetid = models.IntegerField(db_column='_rtblKBDescriptionLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionlinks_checksum = models.TextField(db_column='_rtblKBDescriptionLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKBDescriptionLinks'


class Rtblkbdescriptionsetup(models.Model):
    idkbdescriptionsetup = models.AutoField(db_column='idKBDescriptionSetup', primary_key=True)  # Field name made lowercase.
    iddescription = models.IntegerField(db_column='idDescription')  # Field name made lowercase.
    cdescriptionlabel = models.CharField(db_column='cDescriptionLabel', max_length=35)  # Field name made lowercase.
    binuse = models.BooleanField(db_column='bInUse')  # Field name made lowercase.
    field_rtblkbdescriptionsetup_ibranchid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_dcreateddate = models.DateTimeField(db_column='_rtblKBDescriptionSetup_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_dmodifieddate = models.DateTimeField(db_column='_rtblKBDescriptionSetup_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_icreatedbranchid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_imodifiedbranchid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_icreatedagentid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_imodifiedagentid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_ichangesetid = models.IntegerField(db_column='_rtblKBDescriptionSetup_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblkbdescriptionsetup_checksum = models.TextField(db_column='_rtblKBDescriptionSetup_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKBDescriptionSetup'


class Rtblknowledgebase(models.Model):
    idknowledgebase = models.AutoField(db_column='idKnowledgeBase', primary_key=True)  # Field name made lowercase.
    carticlenumber = models.CharField(db_column='cArticleNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csummary = models.CharField(db_column='cSummary', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus')  # Field name made lowercase.
    bpublic = models.BooleanField(db_column='bPublic')  # Field name made lowercase.
    dcreateddate = models.DateTimeField(db_column='dCreatedDate')  # Field name made lowercase.
    icreatedagentid = models.IntegerField(db_column='iCreatedAgentID')  # Field name made lowercase.
    ddateedited = models.DateTimeField(db_column='dDateEdited', blank=True, null=True)  # Field name made lowercase.
    ieditedagentid = models.IntegerField(db_column='iEditedAgentID')  # Field name made lowercase.
    bisactive = models.BooleanField(db_column='bIsActive')  # Field name made lowercase.
    field_rtblknowledgebase_ibranchid = models.IntegerField(db_column='_rtblKnowledgeBase_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_dcreateddate = models.DateTimeField(db_column='_rtblKnowledgeBase_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_dmodifieddate = models.DateTimeField(db_column='_rtblKnowledgeBase_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_icreatedbranchid = models.IntegerField(db_column='_rtblKnowledgeBase_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_imodifiedbranchid = models.IntegerField(db_column='_rtblKnowledgeBase_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_icreatedagentid = models.IntegerField(db_column='_rtblKnowledgeBase_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_imodifiedagentid = models.IntegerField(db_column='_rtblKnowledgeBase_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_ichangesetid = models.IntegerField(db_column='_rtblKnowledgeBase_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebase_checksum = models.TextField(db_column='_rtblKnowledgeBase_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKnowledgeBase'


class Rtblknowledgebasecat(models.Model):
    idknowledgebasecat = models.IntegerField(db_column='idKnowledgeBaseCat', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=30)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binuse = models.BooleanField(db_column='bInUse')  # Field name made lowercase.
    field_rtblknowledgebasecat_ibranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_dcreateddate = models.DateTimeField(db_column='_rtblKnowledgeBaseCat_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_dmodifieddate = models.DateTimeField(db_column='_rtblKnowledgeBaseCat_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_icreatedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_imodifiedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_icreatedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_imodifiedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_ichangesetid = models.IntegerField(db_column='_rtblKnowledgeBaseCat_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecat_checksum = models.TextField(db_column='_rtblKnowledgeBaseCat_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKnowledgeBaseCat'


class Rtblknowledgebasecatvalue(models.Model):
    idknowledgebasecatvalue = models.AutoField(db_column='idKnowledgeBaseCatValue', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50)  # Field name made lowercase.
    iknowledgebasecatid = models.IntegerField(db_column='iKnowledgeBaseCatID', blank=True, null=True)  # Field name made lowercase.
    field_rtblknowledgebasecatvalue_ibranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_dcreateddate = models.DateTimeField(db_column='_rtblKnowledgeBaseCatValue_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_dmodifieddate = models.DateTimeField(db_column='_rtblKnowledgeBaseCatValue_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_icreatedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_imodifiedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_icreatedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_imodifiedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_ichangesetid = models.IntegerField(db_column='_rtblKnowledgeBaseCatValue_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebasecatvalue_checksum = models.TextField(db_column='_rtblKnowledgeBaseCatValue_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKnowledgeBaseCatValue'


class Rtblknowledgebaselinks(models.Model):
    idknowledgebaselinks = models.AutoField(db_column='idKnowledgeBaseLinks', primary_key=True)  # Field name made lowercase.
    iknowledgebaseid = models.IntegerField(db_column='iKnowledgeBaseID')  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID')  # Field name made lowercase.
    field_rtblknowledgebaselinks_ibranchid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_dcreateddate = models.DateTimeField(db_column='_rtblKnowledgeBaseLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_dmodifieddate = models.DateTimeField(db_column='_rtblKnowledgeBaseLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_icreatedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_imodifiedbranchid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_icreatedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_imodifiedagentid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_ichangesetid = models.IntegerField(db_column='_rtblKnowledgeBaseLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblknowledgebaselinks_checksum = models.TextField(db_column='_rtblKnowledgeBaseLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblKnowledgeBaseLinks'


class Rtblnotify(models.Model):
    idnotify = models.AutoField(db_column='idNotify', primary_key=True)  # Field name made lowercase.
    dnotifydate = models.DateTimeField(db_column='dNotifyDate', blank=True, null=True)  # Field name made lowercase.
    iforagentid = models.IntegerField(db_column='iForAgentID')  # Field name made lowercase.
    iincidentid = models.IntegerField(db_column='iIncidentID', blank=True, null=True)  # Field name made lowercase.
    iincidentlogid = models.IntegerField(db_column='iIncidentLogID', blank=True, null=True)  # Field name made lowercase.
    bread = models.BooleanField(db_column='bRead')  # Field name made lowercase.
    iwhseibtid = models.IntegerField(db_column='iWhseIBTID', blank=True, null=True)  # Field name made lowercase.
    field_rtblnotify_ibranchid = models.IntegerField(db_column='_rtblNotify_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_dcreateddate = models.DateTimeField(db_column='_rtblNotify_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_dmodifieddate = models.DateTimeField(db_column='_rtblNotify_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_icreatedbranchid = models.IntegerField(db_column='_rtblNotify_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_imodifiedbranchid = models.IntegerField(db_column='_rtblNotify_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_icreatedagentid = models.IntegerField(db_column='_rtblNotify_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_imodifiedagentid = models.IntegerField(db_column='_rtblNotify_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_ichangesetid = models.IntegerField(db_column='_rtblNotify_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblnotify_checksum = models.TextField(db_column='_rtblNotify_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblNotify'


class Rtblopportunity(models.Model):
    idopportunity = models.AutoField(db_column='IDOpportunity', primary_key=True)  # Field name made lowercase.
    copportunitynumber = models.CharField(db_column='cOpportunityNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iclientid = models.IntegerField(db_column='iClientID')  # Field name made lowercase.
    iprospectid = models.IntegerField(db_column='iProspectID')  # Field name made lowercase.
    ipeopleid = models.IntegerField(db_column='iPeopleID')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    iopportunitystageid = models.IntegerField(db_column='iOpportunityStageID')  # Field name made lowercase.
    iopportunitystatusid = models.IntegerField(db_column='iOpportunityStatusID')  # Field name made lowercase.
    iopportunitysourceid = models.IntegerField(db_column='iOpportunitySourceID')  # Field name made lowercase.
    ioppsourceclientid = models.IntegerField(db_column='iOppSourceClientID')  # Field name made lowercase.
    ioppsourcesupplierid = models.IntegerField(db_column='iOppSourceSupplierID')  # Field name made lowercase.
    ioppsourceagentid = models.IntegerField(db_column='iOppSourceAgentID')  # Field name made lowercase.
    ddatestart = models.DateTimeField(db_column='dDateStart', blank=True, null=True)  # Field name made lowercase.
    ddateclose = models.DateTimeField(db_column='dDateClose', blank=True, null=True)  # Field name made lowercase.
    ddateactualclose = models.DateTimeField(db_column='dDateActualClose', blank=True, null=True)  # Field name made lowercase.
    fclosedamount = models.FloatField(db_column='fClosedAmount', blank=True, null=True)  # Field name made lowercase.
    fprobabilityperc = models.FloatField(db_column='fProbabilityPerc', blank=True, null=True)  # Field name made lowercase.
    bpublic = models.BooleanField(db_column='bPublic')  # Field name made lowercase.
    iactiveinvnumid = models.BigIntegerField(db_column='iActiveInvNumID')  # Field name made lowercase.
    fforecastamount = models.FloatField(db_column='fForecastAmount', blank=True, null=True)  # Field name made lowercase.
    fbudgetedamount = models.FloatField(db_column='fBudgetedAmount', blank=True, null=True)  # Field name made lowercase.
    copportunitydescription = models.CharField(db_column='cOpportunityDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID')  # Field name made lowercase.
    field_rtblopportunity_ibranchid = models.IntegerField(db_column='_rtblOpportunity_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_dcreateddate = models.DateTimeField(db_column='_rtblOpportunity_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunity_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunity_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunity_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_icreatedagentid = models.IntegerField(db_column='_rtblOpportunity_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunity_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_ichangesetid = models.IntegerField(db_column='_rtblOpportunity_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunity_checksum = models.TextField(db_column='_rtblOpportunity_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunity'


class Rtblopportunitycompetitor(models.Model):
    idopportunitycompetitor = models.AutoField(db_column='idOpportunityCompetitor', primary_key=True)  # Field name made lowercase.
    iopportunityid = models.IntegerField(db_column='iOpportunityID')  # Field name made lowercase.
    icompetitorid = models.IntegerField(db_column='iCompetitorID')  # Field name made lowercase.
    icompetitorproductid = models.IntegerField(db_column='iCompetitorProductID')  # Field name made lowercase.
    fprice = models.FloatField(db_column='fPrice', blank=True, null=True)  # Field name made lowercase.
    bwondeal = models.BooleanField(db_column='bWonDeal')  # Field name made lowercase.
    field_rtblopportunitycompetitor_ibranchid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_dcreateddate = models.DateTimeField(db_column='_rtblOpportunityCompetitor_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunityCompetitor_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_icreatedagentid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_ichangesetid = models.IntegerField(db_column='_rtblOpportunityCompetitor_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitycompetitor_checksum = models.TextField(db_column='_rtblOpportunityCompetitor_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunityCompetitor'


class Rtblopportunitydoclinks(models.Model):
    iddoclinks = models.AutoField(db_column='IDDocLinks', primary_key=True)  # Field name made lowercase.
    idocstoreid = models.IntegerField(db_column='iDocStoreID', blank=True, null=True)  # Field name made lowercase.
    ilinksource = models.IntegerField(db_column='iLinkSource', blank=True, null=True)  # Field name made lowercase.
    ilinkid = models.IntegerField(db_column='iLinkID', blank=True, null=True)  # Field name made lowercase.
    field_rtblopportunitydoclinks_ibranchid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_dcreateddate = models.DateTimeField(db_column='_rtblOpportunityDocLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunityDocLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_icreatedagentid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_ichangesetid = models.IntegerField(db_column='_rtblOpportunityDocLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitydoclinks_checksum = models.TextField(db_column='_rtblOpportunityDocLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunityDocLinks'


class Rtblopportunitysource(models.Model):
    idopportunitysource = models.AutoField(db_column='IDOpportunitySource', primary_key=True)  # Field name made lowercase.
    csourcedesc = models.CharField(db_column='cSourceDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_rtblopportunitysource_ibranchid = models.IntegerField(db_column='_rtblOpportunitySource_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_dcreateddate = models.DateTimeField(db_column='_rtblOpportunitySource_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunitySource_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunitySource_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunitySource_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_icreatedagentid = models.IntegerField(db_column='_rtblOpportunitySource_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunitySource_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_ichangesetid = models.IntegerField(db_column='_rtblOpportunitySource_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitysource_checksum = models.TextField(db_column='_rtblOpportunitySource_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunitySource'


class Rtblopportunitystage(models.Model):
    idopportunitystage = models.AutoField(db_column='IDOpportunityStage', primary_key=True)  # Field name made lowercase.
    cstagename = models.CharField(db_column='cStageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstagedescription = models.CharField(db_column='cStageDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iopportunitystatusid = models.IntegerField(db_column='iOpportunityStatusID', blank=True, null=True)  # Field name made lowercase.
    istagesequence = models.IntegerField(db_column='iStageSequence', blank=True, null=True)  # Field name made lowercase.
    fdefprobabilityperc = models.FloatField(db_column='fDefProbabilityPerc', blank=True, null=True)  # Field name made lowercase.
    field_rtblopportunitystage_ibranchid = models.IntegerField(db_column='_rtblOpportunityStage_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_dcreateddate = models.DateTimeField(db_column='_rtblOpportunityStage_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunityStage_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunityStage_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunityStage_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_icreatedagentid = models.IntegerField(db_column='_rtblOpportunityStage_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunityStage_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_ichangesetid = models.IntegerField(db_column='_rtblOpportunityStage_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystage_checksum = models.TextField(db_column='_rtblOpportunityStage_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunityStage'


class Rtblopportunitystatus(models.Model):
    idopportunitystatus = models.AutoField(db_column='IDOpportunityStatus', primary_key=True)  # Field name made lowercase.
    cstatusname = models.CharField(db_column='cStatusName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bfinal = models.BooleanField(db_column='bFinal')  # Field name made lowercase.
    field_rtblopportunitystatus_ibranchid = models.IntegerField(db_column='_rtblOpportunityStatus_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_dcreateddate = models.DateTimeField(db_column='_rtblOpportunityStatus_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_dmodifieddate = models.DateTimeField(db_column='_rtblOpportunityStatus_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_icreatedbranchid = models.IntegerField(db_column='_rtblOpportunityStatus_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_imodifiedbranchid = models.IntegerField(db_column='_rtblOpportunityStatus_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_icreatedagentid = models.IntegerField(db_column='_rtblOpportunityStatus_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_imodifiedagentid = models.IntegerField(db_column='_rtblOpportunityStatus_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_ichangesetid = models.IntegerField(db_column='_rtblOpportunityStatus_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblopportunitystatus_checksum = models.TextField(db_column='_rtblOpportunityStatus_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblOpportunityStatus'


class Rtblpeople(models.Model):
    idpeople = models.AutoField(db_column='idPeople', primary_key=True)  # Field name made lowercase.
    cfirstname = models.CharField(db_column='cFirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cinitials = models.CharField(db_column='cInitials', max_length=5, blank=True, null=True)  # Field name made lowercase.
    clastname = models.CharField(db_column='cLastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cdisplayname = models.CharField(db_column='cDisplayName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ctitle = models.CharField(db_column='cTitle', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctelwork = models.CharField(db_column='cTelWork', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelfax = models.CharField(db_column='cTelFax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelmobile = models.CharField(db_column='cTelMobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctelhome = models.CharField(db_column='cTelHome', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cwebpage = models.CharField(db_column='cWebPage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccomments = models.CharField(db_column='cComments', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    caddress = models.CharField(db_column='cAddress', max_length=240, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress = models.CharField(db_column='cPostalAddress', max_length=240, blank=True, null=True)  # Field name made lowercase.
    ibusdeptid = models.IntegerField(db_column='iBusDeptID', blank=True, null=True)  # Field name made lowercase.
    ibusdesigid = models.IntegerField(db_column='iBusDesigID', blank=True, null=True)  # Field name made lowercase.
    dbirthdate = models.DateTimeField(db_column='dBirthDate', blank=True, null=True)  # Field name made lowercase.
    dpeopletimestamp = models.DateTimeField(db_column='dPeopleTimeStamp', blank=True, null=True)  # Field name made lowercase.
    field_rtblpeople_ibranchid = models.IntegerField(db_column='_rtblPeople_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_dcreateddate = models.DateTimeField(db_column='_rtblPeople_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_dmodifieddate = models.DateTimeField(db_column='_rtblPeople_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_icreatedbranchid = models.IntegerField(db_column='_rtblPeople_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_imodifiedbranchid = models.IntegerField(db_column='_rtblPeople_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_icreatedagentid = models.IntegerField(db_column='_rtblPeople_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_imodifiedagentid = models.IntegerField(db_column='_rtblPeople_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_ichangesetid = models.IntegerField(db_column='_rtblPeople_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeople_checksum = models.TextField(db_column='_rtblPeople_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    bobjecttoprocess = models.BooleanField(db_column='bObjectToProcess')  # Field name made lowercase.
    bstatemail = models.BooleanField(db_column='bStatEmail')  # Field name made lowercase.
    bsourcedocemail = models.BooleanField(db_column='bSourceDocEmail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblPeople'


class Rtblpeoplelinks(models.Model):
    idpeoplelinks = models.AutoField(db_column='idPeopleLinks', primary_key=True)  # Field name made lowercase.
    ipeopleid = models.IntegerField(db_column='iPeopleID', blank=True, null=True)  # Field name made lowercase.
    idebtorid = models.IntegerField(db_column='iDebtorID', blank=True, null=True)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field_rtblpeoplelinks_ibranchid = models.IntegerField(db_column='_rtblPeopleLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_dcreateddate = models.DateTimeField(db_column='_rtblPeopleLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_dmodifieddate = models.DateTimeField(db_column='_rtblPeopleLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_icreatedbranchid = models.IntegerField(db_column='_rtblPeopleLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_imodifiedbranchid = models.IntegerField(db_column='_rtblPeopleLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_icreatedagentid = models.IntegerField(db_column='_rtblPeopleLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_imodifiedagentid = models.IntegerField(db_column='_rtblPeopleLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_ichangesetid = models.IntegerField(db_column='_rtblPeopleLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblpeoplelinks_checksum = models.TextField(db_column='_rtblPeopleLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblPeopleLinks'


class Rtblprospect(models.Model):
    idprospect = models.AutoField(db_column='IDProspect', primary_key=True)  # Field name made lowercase.
    ccompanyname = models.CharField(db_column='cCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctelephone = models.CharField(db_column='cTelephone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cfax = models.CharField(db_column='cFax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdress1 = models.CharField(db_column='cPhysicalAddress1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdress2 = models.CharField(db_column='cPhysicalAddress2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdress3 = models.CharField(db_column='cPhysicalAddress3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdress4 = models.CharField(db_column='cPhysicalAddress4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdress5 = models.CharField(db_column='cPhysicalAddress5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cphysicaladdresspc = models.CharField(db_column='cPhysicalAddressPC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress1 = models.CharField(db_column='cPostalAddress1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress2 = models.CharField(db_column='cPostalAddress2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress3 = models.CharField(db_column='cPostalAddress3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress4 = models.CharField(db_column='cPostalAddress4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpostaladdress5 = models.CharField(db_column='cPostalAddress5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpostaladdresspc = models.CharField(db_column='cPostalAddressPC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cwebsite = models.CharField(db_column='cWebsite', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bchargetax = models.BooleanField(db_column='bChargeTax')  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    bpublic = models.BooleanField(db_column='bPublic')  # Field name made lowercase.
    irepid = models.IntegerField(db_column='iRepID')  # Field name made lowercase.
    field_rtblprospect_ibranchid = models.IntegerField(db_column='_rtblProspect_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_dcreateddate = models.DateTimeField(db_column='_rtblProspect_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_dmodifieddate = models.DateTimeField(db_column='_rtblProspect_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_icreatedbranchid = models.IntegerField(db_column='_rtblProspect_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_imodifiedbranchid = models.IntegerField(db_column='_rtblProspect_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_icreatedagentid = models.IntegerField(db_column='_rtblProspect_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_imodifiedagentid = models.IntegerField(db_column='_rtblProspect_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_ichangesetid = models.IntegerField(db_column='_rtblProspect_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblprospect_checksum = models.TextField(db_column='_rtblProspect_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblProspect'


class Rtblrefbase(models.Model):
    idrefbase = models.AutoField(db_column='idRefBase', primary_key=True)  # Field name made lowercase.
    creftype = models.CharField(db_column='cRefType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inextno = models.IntegerField(db_column='iNextNo', blank=True, null=True)  # Field name made lowercase.
    field_rtblrefbase_ibranchid = models.IntegerField(db_column='_rtblRefBase_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_dcreateddate = models.DateTimeField(db_column='_rtblRefBase_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_dmodifieddate = models.DateTimeField(db_column='_rtblRefBase_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_icreatedbranchid = models.IntegerField(db_column='_rtblRefBase_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_imodifiedbranchid = models.IntegerField(db_column='_rtblRefBase_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_icreatedagentid = models.IntegerField(db_column='_rtblRefBase_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_imodifiedagentid = models.IntegerField(db_column='_rtblRefBase_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_ichangesetid = models.IntegerField(db_column='_rtblRefBase_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbase_checksum = models.TextField(db_column='_rtblRefBase_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblRefBase'


class Rtblrefbook(models.Model):
    idrefbook = models.AutoField(db_column='idRefBook', primary_key=True)  # Field name made lowercase.
    irefbaseid = models.IntegerField(db_column='iRefBaseID', blank=True, null=True)  # Field name made lowercase.
    ibookedno = models.IntegerField(db_column='iBookedNo', blank=True, null=True)  # Field name made lowercase.
    bavailable = models.BooleanField(db_column='bAvailable')  # Field name made lowercase.
    field_rtblrefbook_ibranchid = models.IntegerField(db_column='_rtblRefBook_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_dcreateddate = models.DateTimeField(db_column='_rtblRefBook_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_dmodifieddate = models.DateTimeField(db_column='_rtblRefBook_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_icreatedbranchid = models.IntegerField(db_column='_rtblRefBook_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_imodifiedbranchid = models.IntegerField(db_column='_rtblRefBook_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_icreatedagentid = models.IntegerField(db_column='_rtblRefBook_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_imodifiedagentid = models.IntegerField(db_column='_rtblRefBook_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_ichangesetid = models.IntegerField(db_column='_rtblRefBook_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblrefbook_checksum = models.TextField(db_column='_rtblRefBook_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblRefBook'


class Rtblstocklinks(models.Model):
    idstocklinks = models.AutoField(db_column='idStockLinks', primary_key=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockID')  # Field name made lowercase.
    idclink = models.IntegerField(db_column='iDCLink')  # Field name made lowercase.
    bitemactive = models.BooleanField(db_column='bItemActive')  # Field name made lowercase.
    cproductreference = models.CharField(db_column='cProductReference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cmodule = models.CharField(db_column='cModule', max_length=2)  # Field name made lowercase.
    csupinvcode = models.CharField(db_column='cSupInvCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iwhseid = models.IntegerField(db_column='iWhseID')  # Field name made lowercase.
    bdefaultsupplier = models.BooleanField(db_column='bDefaultSupplier')  # Field name made lowercase.
    bdconhold = models.BooleanField(db_column='bDCOnHold')  # Field name made lowercase.
    dtimestamp = models.DateTimeField(db_column='dTimeStamp', blank=True, null=True)  # Field name made lowercase.
    flastgrvcost = models.FloatField(db_column='fLastGRVCost')  # Field name made lowercase.
    dlastgrvcostdate = models.DateTimeField(db_column='dLastGRVCostDate', blank=True, null=True)  # Field name made lowercase.
    fmanualcost = models.FloatField(db_column='fManualCost')  # Field name made lowercase.
    field_rtblstocklinks_fleaddays = models.FloatField(db_column='_rtblStockLinks_fLeadDays', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    fminorderquantity = models.FloatField(db_column='fMinOrderQuantity', blank=True, null=True)  # Field name made lowercase.
    field_rtblstocklinks_ibranchid = models.IntegerField(db_column='_rtblStockLinks_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_dcreateddate = models.DateTimeField(db_column='_rtblStockLinks_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_dmodifieddate = models.DateTimeField(db_column='_rtblStockLinks_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_icreatedbranchid = models.IntegerField(db_column='_rtblStockLinks_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_imodifiedbranchid = models.IntegerField(db_column='_rtblStockLinks_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_icreatedagentid = models.IntegerField(db_column='_rtblStockLinks_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_imodifiedagentid = models.IntegerField(db_column='_rtblStockLinks_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_ichangesetid = models.IntegerField(db_column='_rtblStockLinks_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblstocklinks_checksum = models.TextField(db_column='_rtblStockLinks_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    itaxtypeid = models.IntegerField(db_column='iTaxTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rtblStockLinks'
        unique_together = (('istockid', 'idclink', 'cmodule', 'iwhseid', 'bdefaultsupplier'),)


class Rtbluserdict(models.Model):
    iduserdict = models.AutoField(db_column='idUserDict', primary_key=True)  # Field name made lowercase.
    cfieldname = models.CharField(db_column='cFieldName', max_length=50)  # Field name made lowercase.
    cfielddescription = models.CharField(db_column='cFieldDescription', max_length=50)  # Field name made lowercase.
    ifieldtype = models.IntegerField(db_column='iFieldType')  # Field name made lowercase.
    ifieldsize = models.IntegerField(db_column='iFieldSize', blank=True, null=True)  # Field name made lowercase.
    ifieldindex = models.IntegerField(db_column='iFieldIndex')  # Field name made lowercase.
    ctablename = models.CharField(db_column='cTableName', max_length=50)  # Field name made lowercase.
    clookupoptions = models.TextField(db_column='cLookupOptions', blank=True, null=True)  # Field name made lowercase.
    bforcevalue = models.BooleanField(db_column='bForceValue')  # Field name made lowercase.
    cdefaultvalue = models.CharField(db_column='cDefaultValue', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ipageindex = models.IntegerField(db_column='iPageIndex', blank=True, null=True)  # Field name made lowercase.
    cpagename = models.CharField(db_column='cPageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ifielddecimals = models.IntegerField(db_column='iFieldDecimals', blank=True, null=True)  # Field name made lowercase.
    imoduleoptions = models.IntegerField(db_column='iModuleOptions', blank=True, null=True)  # Field name made lowercase.
    bisuserhist = models.BooleanField(db_column='bIsUserHist')  # Field name made lowercase.
    field_rtbluserdict_ibranchid = models.IntegerField(db_column='_rtblUserDict_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_dcreateddate = models.DateTimeField(db_column='_rtblUserDict_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_dmodifieddate = models.DateTimeField(db_column='_rtblUserDict_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_icreatedbranchid = models.IntegerField(db_column='_rtblUserDict_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_imodifiedbranchid = models.IntegerField(db_column='_rtblUserDict_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_icreatedagentid = models.IntegerField(db_column='_rtblUserDict_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_imodifiedagentid = models.IntegerField(db_column='_rtblUserDict_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_ichangesetid = models.IntegerField(db_column='_rtblUserDict_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtbluserdict_checksum = models.TextField(db_column='_rtblUserDict_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblUserDict'


class Rtblworkcal(models.Model):
    idworkcal = models.AutoField(db_column='idWorkCal', primary_key=True)  # Field name made lowercase.
    istarttime = models.IntegerField(db_column='iStartTime')  # Field name made lowercase.
    iendtime = models.IntegerField(db_column='iEndTime')  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bsunday = models.BooleanField(db_column='bSunday')  # Field name made lowercase.
    bmonday = models.BooleanField(db_column='bMonday')  # Field name made lowercase.
    btuesday = models.BooleanField(db_column='bTuesday')  # Field name made lowercase.
    bwednesday = models.BooleanField(db_column='bWednesday')  # Field name made lowercase.
    bthursday = models.BooleanField(db_column='bThursday')  # Field name made lowercase.
    bfriday = models.BooleanField(db_column='bFriday')  # Field name made lowercase.
    bsaturday = models.BooleanField(db_column='bSaturday')  # Field name made lowercase.
    field_rtblworkcal_ibranchid = models.IntegerField(db_column='_rtblWorkCal_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_dcreateddate = models.DateTimeField(db_column='_rtblWorkCal_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_dmodifieddate = models.DateTimeField(db_column='_rtblWorkCal_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_icreatedbranchid = models.IntegerField(db_column='_rtblWorkCal_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_imodifiedbranchid = models.IntegerField(db_column='_rtblWorkCal_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_icreatedagentid = models.IntegerField(db_column='_rtblWorkCal_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_imodifiedagentid = models.IntegerField(db_column='_rtblWorkCal_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_ichangesetid = models.IntegerField(db_column='_rtblWorkCal_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcal_checksum = models.TextField(db_column='_rtblWorkCal_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblWorkCal'


class Rtblworkcalexdates(models.Model):
    idworkcalexdates = models.AutoField(db_column='idWorkCalExDates', primary_key=True)  # Field name made lowercase.
    dexdate = models.DateTimeField(db_column='dExDate')  # Field name made lowercase.
    brepeat = models.BooleanField(db_column='bRepeat')  # Field name made lowercase.
    field_rtblworkcalexdates_ibranchid = models.IntegerField(db_column='_rtblWorkCalExDates_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_dcreateddate = models.DateTimeField(db_column='_rtblWorkCalExDates_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_dmodifieddate = models.DateTimeField(db_column='_rtblWorkCalExDates_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_icreatedbranchid = models.IntegerField(db_column='_rtblWorkCalExDates_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_imodifiedbranchid = models.IntegerField(db_column='_rtblWorkCalExDates_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_icreatedagentid = models.IntegerField(db_column='_rtblWorkCalExDates_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_imodifiedagentid = models.IntegerField(db_column='_rtblWorkCalExDates_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_ichangesetid = models.IntegerField(db_column='_rtblWorkCalExDates_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_rtblworkcalexdates_checksum = models.TextField(db_column='_rtblWorkCalExDates_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_rtblWorkCalExDates'


class Simtbldefaults(models.Model):
    bgeneralledger = models.BooleanField(db_column='bGeneralLedger', blank=True, null=True)  # Field name made lowercase.
    bjobcards = models.BooleanField(db_column='bJobCards', blank=True, null=True)  # Field name made lowercase.
    bproject = models.BooleanField(db_column='bProject', blank=True, null=True)  # Field name made lowercase.
    cstockissue_trans = models.CharField(db_column='cStockIssue_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstockcredit_trans = models.CharField(db_column='cStockCredit_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cincidenttype = models.CharField(db_column='cIncidentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ballowstock_requistion = models.BooleanField(db_column='bAllowStock_requistion', blank=True, null=True)  # Field name made lowercase.
    bstockauto_numbering = models.BooleanField(db_column='bStockAuto_Numbering', blank=True, null=True)  # Field name made lowercase.
    cstockprefix = models.CharField(db_column='cStockPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    istock_padtonumber = models.IntegerField(db_column='iStock_PadtoNumber', blank=True, null=True)  # Field name made lowercase.
    istocknextnumber = models.IntegerField(db_column='iStockNextNumber', blank=True, null=True)  # Field name made lowercase.
    bstockuniquenumber = models.BooleanField(db_column='bStockUniqueNumber', blank=True, null=True)  # Field name made lowercase.
    bissueauto_numbering = models.BooleanField(db_column='bIssueAuto_Numbering', blank=True, null=True)  # Field name made lowercase.
    cissueprefix = models.CharField(db_column='cIssuePrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    iissue_padtonumber = models.IntegerField(db_column='iIssue_PadtoNumber', blank=True, null=True)  # Field name made lowercase.
    iissuenextnumber = models.IntegerField(db_column='iIssueNextNumber', blank=True, null=True)  # Field name made lowercase.
    bissueuniquenumber = models.BooleanField(db_column='bIssueUniqueNumber', blank=True, null=True)  # Field name made lowercase.
    btemplateautonumbering = models.BooleanField(db_column='bTemplateAutoNumbering', blank=True, null=True)  # Field name made lowercase.
    ctemplateprefix = models.CharField(db_column='cTemplatePrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    itemplate_padtonumber = models.IntegerField(db_column='iTemplate_PadtoNumber', blank=True, null=True)  # Field name made lowercase.
    itemplatenextnumber = models.IntegerField(db_column='iTemplateNextNumber', blank=True, null=True)  # Field name made lowercase.
    btemplateuniquenumber = models.BooleanField(db_column='bTemplateUniqueNumber', blank=True, null=True)  # Field name made lowercase.
    itrcode = models.IntegerField(db_column='iTrcode', blank=True, null=True)  # Field name made lowercase.
    buseworkflow = models.BooleanField(db_column='bUseWorkFlow', blank=True, null=True)  # Field name made lowercase.
    field_simtbldefaults_ibranchid = models.IntegerField(db_column='_simtblDefaults_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_dcreateddate = models.DateTimeField(db_column='_simtblDefaults_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_dmodifieddate = models.DateTimeField(db_column='_simtblDefaults_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_icreatedbranchid = models.IntegerField(db_column='_simtblDefaults_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_imodifiedbranchid = models.IntegerField(db_column='_simtblDefaults_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_icreatedagentid = models.IntegerField(db_column='_simtblDefaults_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_imodifiedagentid = models.IntegerField(db_column='_simtblDefaults_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_ichangesetid = models.IntegerField(db_column='_simtblDefaults_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtbldefaults_checksum = models.TextField(db_column='_simtblDefaults_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblDefaults'


class Simtblreportlayout(models.Model):
    idreportlayout = models.AutoField(db_column='idReportLayout')  # Field name made lowercase.
    crptdescription = models.CharField(db_column='cRptDescription', max_length=80)  # Field name made lowercase.
    crpttypedescription = models.CharField(db_column='cRptTypeDescription', max_length=80)  # Field name made lowercase.
    imoduleid = models.IntegerField(db_column='iModuleId', blank=True, null=True)  # Field name made lowercase.
    iversion = models.IntegerField(db_column='iVersion', blank=True, null=True)  # Field name made lowercase.
    nlayout = models.BinaryField(db_column='nLayout')  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly')  # Field name made lowercase.
    bisdefaultlayout = models.BooleanField(db_column='bIsDefaultLayout', blank=True, null=True)  # Field name made lowercase.
    bisstandard = models.BooleanField(db_column='bIsStandard', blank=True, null=True)  # Field name made lowercase.
    field_simtblreportlayout_ibranchid = models.IntegerField(db_column='_simtblReportLayout_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_dcreateddate = models.DateTimeField(db_column='_simtblReportLayout_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_dmodifieddate = models.DateTimeField(db_column='_simtblReportLayout_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_icreatedbranchid = models.IntegerField(db_column='_simtblReportLayout_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_imodifiedbranchid = models.IntegerField(db_column='_simtblReportLayout_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_icreatedagentid = models.IntegerField(db_column='_simtblReportLayout_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_imodifiedagentid = models.IntegerField(db_column='_simtblReportLayout_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_ichangesetid = models.IntegerField(db_column='_simtblReportLayout_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreportlayout_checksum = models.TextField(db_column='_simtblReportLayout_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblReportLayout'


class Simtblreqheader(models.Model):
    idreqheader = models.AutoField(db_column='idReqHeader', primary_key=True)  # Field name made lowercase.
    crequisitionno = models.CharField(db_column='cRequisitionNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drequisitiondate = models.DateTimeField(db_column='dRequisitionDate', blank=True, null=True)  # Field name made lowercase.
    iprojectdefaultid = models.IntegerField(db_column='iProjectDefaultID', blank=True, null=True)  # Field name made lowercase.
    crequestedby = models.CharField(db_column='cRequestedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iincidenttypedefaultid = models.IntegerField(db_column='iIncidentTypeDefaultID', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    field_simtblreqheader_ibranchid = models.IntegerField(db_column='_simtblReqHeader_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_dcreateddate = models.DateTimeField(db_column='_simtblReqHeader_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_dmodifieddate = models.DateTimeField(db_column='_simtblReqHeader_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_icreatedbranchid = models.IntegerField(db_column='_simtblReqHeader_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_imodifiedbranchid = models.IntegerField(db_column='_simtblReqHeader_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_icreatedagentid = models.IntegerField(db_column='_simtblReqHeader_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_imodifiedagentid = models.IntegerField(db_column='_simtblReqHeader_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_ichangesetid = models.IntegerField(db_column='_simtblReqHeader_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqheader_checksum = models.TextField(db_column='_simtblReqHeader_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblReqHeader'


class Simtblreqlines(models.Model):
    idreqlines = models.AutoField(db_column='idReqLines', primary_key=True)  # Field name made lowercase.
    fk_idreqheader = models.IntegerField(db_column='fk_idReqHeader', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockId', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.TextField(db_column='cDescription', blank=True, null=True)  # Field name made lowercase.
    ireqstatus = models.IntegerField(db_column='iReqStatus', blank=True, null=True)  # Field name made lowercase.
    dsartdate = models.DateTimeField(db_column='dSartDate', blank=True, null=True)  # Field name made lowercase.
    denddate = models.DateTimeField(db_column='dEndDate', blank=True, null=True)  # Field name made lowercase.
    funitcost = models.FloatField(db_column='fUnitCost', blank=True, null=True)  # Field name made lowercase.
    iunitofmeasure = models.IntegerField(db_column='iUnitOfMeasure', blank=True, null=True)  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseId', blank=True, null=True)  # Field name made lowercase.
    istockbinlocationid = models.IntegerField(db_column='iStockBinLocationID', blank=True, null=True)  # Field name made lowercase.
    flinetotalcost = models.FloatField(db_column='fLineTotalCost', blank=True, null=True)  # Field name made lowercase.
    bisprocessed = models.BooleanField(db_column='bIsprocessed', blank=True, null=True)  # Field name made lowercase.
    fconfirmqty = models.FloatField(db_column='fConfirmQty', blank=True, null=True)  # Field name made lowercase.
    biswarehouse = models.BooleanField(db_column='bIswarehouse', blank=True, null=True)  # Field name made lowercase.
    ctype = models.CharField(db_column='cType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctypedetails = models.IntegerField(db_column='cTypeDetails', blank=True, null=True)  # Field name made lowercase.
    itrcodeid = models.IntegerField(db_column='iTrcodeId', blank=True, null=True)  # Field name made lowercase.
    iincidenttypeid = models.IntegerField(db_column='iIncidentTypeID', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectID', blank=True, null=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID', blank=True, null=True)  # Field name made lowercase.
    ilineno = models.IntegerField(db_column='iLineNo', blank=True, null=True)  # Field name made lowercase.
    itaxtype = models.IntegerField(db_column='iTaxType', blank=True, null=True)  # Field name made lowercase.
    fk_iincidentid = models.IntegerField(db_column='fk_iIncidentId', blank=True, null=True)  # Field name made lowercase.
    istockingunitid = models.IntegerField(db_column='iStockingUnitID', blank=True, null=True)  # Field name made lowercase.
    iunitcategoryid = models.IntegerField(db_column='iUnitCategoryID', blank=True, null=True)  # Field name made lowercase.
    istockingunitcategoryid = models.IntegerField(db_column='iStockingUnitCategoryID', blank=True, null=True)  # Field name made lowercase.
    bislot = models.BooleanField(db_column='bIsLot', blank=True, null=True)  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem', blank=True, null=True)  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID', blank=True, null=True)  # Field name made lowercase.
    field_simtblreqlines_ibranchid = models.IntegerField(db_column='_simtblReqLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_dcreateddate = models.DateTimeField(db_column='_simtblReqLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_dmodifieddate = models.DateTimeField(db_column='_simtblReqLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_icreatedbranchid = models.IntegerField(db_column='_simtblReqLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_imodifiedbranchid = models.IntegerField(db_column='_simtblReqLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_icreatedagentid = models.IntegerField(db_column='_simtblReqLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_imodifiedagentid = models.IntegerField(db_column='_simtblReqLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_ichangesetid = models.IntegerField(db_column='_simtblReqLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblreqlines_checksum = models.TextField(db_column='_simtblReqLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblReqLines'


class Simtblstkissuelines(models.Model):
    iautoidx = models.AutoField(db_column='iAutoIdx', primary_key=True)  # Field name made lowercase.
    istkissueid = models.IntegerField(db_column='iStkIssueId', blank=True, null=True)  # Field name made lowercase.
    istkissuetaxtpid = models.IntegerField(db_column='iStkIssueTaxTpId', blank=True, null=True)  # Field name made lowercase.
    istockid = models.IntegerField(db_column='iStockId', blank=True, null=True)  # Field name made lowercase.
    cdescription = models.TextField(db_column='cDescription', blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus', blank=True, null=True)  # Field name made lowercase.
    funitcost = models.FloatField(db_column='fUnitCost', blank=True, null=True)  # Field name made lowercase.
    iunitofmeasure = models.IntegerField(db_column='iUnitOfMeasure', blank=True, null=True)  # Field name made lowercase.
    iwarehouseid = models.IntegerField(db_column='iWarehouseId', blank=True, null=True)  # Field name made lowercase.
    istockbinlocationid = models.IntegerField(db_column='iStockBinLocationID', blank=True, null=True)  # Field name made lowercase.
    flinetotalcost = models.FloatField(db_column='fLineTotalCost', blank=True, null=True)  # Field name made lowercase.
    bisprocessed = models.BooleanField(db_column='bIsprocessed', blank=True, null=True)  # Field name made lowercase.
    fconfirmqty = models.FloatField(db_column='fConfirmQty', blank=True, null=True)  # Field name made lowercase.
    biswarehouse = models.BooleanField(db_column='bIswarehouse', blank=True, null=True)  # Field name made lowercase.
    ctype = models.CharField(db_column='cType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctypedetails = models.CharField(db_column='cTypeDetails', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cproject = models.CharField(db_column='cProject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itrcodeid = models.IntegerField(db_column='iTrcodeId', blank=True, null=True)  # Field name made lowercase.
    bislot = models.BooleanField(db_column='bIsLot', blank=True, null=True)  # Field name made lowercase.
    ilotnumber = models.IntegerField(db_column='iLotNumber', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectId', blank=True, null=True)  # Field name made lowercase.
    istockingunitid = models.IntegerField(db_column='iStockingUnitID', blank=True, null=True)  # Field name made lowercase.
    iunitcategoryid = models.IntegerField(db_column='iUnitCategoryID', blank=True, null=True)  # Field name made lowercase.
    istockingunitcategoryid = models.IntegerField(db_column='iStockingUnitCategoryID', blank=True, null=True)  # Field name made lowercase.
    bisserialitem = models.BooleanField(db_column='bIsSerialItem', blank=True, null=True)  # Field name made lowercase.
    dlotexpirydate = models.DateTimeField(db_column='dLotExpiryDate', blank=True, null=True)  # Field name made lowercase.
    xattribute = models.TextField(db_column='xAttribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iattributegroupid = models.IntegerField(db_column='iAttributeGroupID', blank=True, null=True)  # Field name made lowercase.
    field_simtblstkissuelines_ibranchid = models.IntegerField(db_column='_simtblStkIssueLines_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_dcreateddate = models.DateTimeField(db_column='_simtblStkIssueLines_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_dmodifieddate = models.DateTimeField(db_column='_simtblStkIssueLines_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_icreatedbranchid = models.IntegerField(db_column='_simtblStkIssueLines_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_imodifiedbranchid = models.IntegerField(db_column='_simtblStkIssueLines_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_icreatedagentid = models.IntegerField(db_column='_simtblStkIssueLines_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_imodifiedagentid = models.IntegerField(db_column='_simtblStkIssueLines_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_ichangesetid = models.IntegerField(db_column='_simtblStkIssueLines_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstkissuelines_checksum = models.TextField(db_column='_simtblStkIssueLines_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblStkIssueLines'


class Simtblstockissuelinesn(models.Model):
    idstockissuelinesn = models.AutoField(db_column='idStockIssueLineSN', primary_key=True)  # Field name made lowercase.
    iserialstockissueid = models.IntegerField(db_column='iSerialStockIssueID')  # Field name made lowercase.
    iserialstockissuelineid = models.BigIntegerField(db_column='iSerialStockIssueLineID')  # Field name made lowercase.
    cserialnumber = models.CharField(db_column='cSerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iserialmfid = models.IntegerField(db_column='iSerialMFID')  # Field name made lowercase.
    field_simtblstockissuelinesn_ibranchid = models.IntegerField(db_column='_simtblStockIssueLineSN_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_dcreateddate = models.DateTimeField(db_column='_simtblStockIssueLineSN_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_dmodifieddate = models.DateTimeField(db_column='_simtblStockIssueLineSN_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_icreatedbranchid = models.IntegerField(db_column='_simtblStockIssueLineSN_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_imodifiedbranchid = models.IntegerField(db_column='_simtblStockIssueLineSN_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_icreatedagentid = models.IntegerField(db_column='_simtblStockIssueLineSN_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_imodifiedagentid = models.IntegerField(db_column='_simtblStockIssueLineSN_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_ichangesetid = models.IntegerField(db_column='_simtblStockIssueLineSN_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuelinesn_checksum = models.TextField(db_column='_simtblStockIssueLineSN_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblStockIssueLineSN'


class Simtblstockissuemaster(models.Model):
    istkissueid = models.AutoField(db_column='iStkIssueId', primary_key=True)  # Field name made lowercase.
    cstkissuenumber = models.CharField(db_column='cStkIssueNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescripton = models.TextField(db_column='cDescripton', blank=True, null=True)  # Field name made lowercase.
    ctype = models.CharField(db_column='cType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    istatus = models.IntegerField(db_column='iStatus', blank=True, null=True)  # Field name made lowercase.
    dissuedate = models.DateTimeField(db_column='dIssueDate', blank=True, null=True)  # Field name made lowercase.
    iprojectid = models.IntegerField(db_column='iProjectId', blank=True, null=True)  # Field name made lowercase.
    bistemplate = models.BooleanField(db_column='bIsTemplate', blank=True, null=True)  # Field name made lowercase.
    ctemplateid = models.CharField(db_column='cTemplateId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctemplatedescription = models.CharField(db_column='cTemplateDescription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irequisitionid = models.IntegerField(db_column='iRequisitionId')  # Field name made lowercase.
    crequestedby = models.CharField(db_column='cRequestedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field_simtblstockissuemaster_ibranchid = models.IntegerField(db_column='_simtblStockIssueMaster_iBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_dcreateddate = models.DateTimeField(db_column='_simtblStockIssueMaster_dCreatedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_dmodifieddate = models.DateTimeField(db_column='_simtblStockIssueMaster_dModifiedDate', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_icreatedbranchid = models.IntegerField(db_column='_simtblStockIssueMaster_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_imodifiedbranchid = models.IntegerField(db_column='_simtblStockIssueMaster_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_icreatedagentid = models.IntegerField(db_column='_simtblStockIssueMaster_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_imodifiedagentid = models.IntegerField(db_column='_simtblStockIssueMaster_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_ichangesetid = models.IntegerField(db_column='_simtblStockIssueMaster_iChangeSetID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_simtblstockissuemaster_checksum = models.TextField(db_column='_simtblStockIssueMaster_Checksum', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_simtblStockIssueMaster'


class Smstblagentpermissions(models.Model):
    idagentpermission = models.AutoField(db_column='idAgentPermission', primary_key=True)  # Field name made lowercase.
    iagentid = models.IntegerField(db_column='iAgentID')  # Field name made lowercase.
    itemplateid = models.IntegerField(db_column='iTemplateID')  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblAgentPermissions'


class Smstblcustomtemplate(models.Model):
    custtemplateid = models.AutoField(db_column='CustTemplateID', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=100)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sqltext = models.CharField(db_column='SQLText', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    templatetext = models.CharField(db_column='TemplateText', max_length=320)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    querytemplate = models.CharField(db_column='QueryTemplate', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    filter = models.CharField(db_column='Filter', max_length=500, blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    isemail = models.BooleanField(db_column='IsEmail', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailnotification = models.CharField(db_column='EmailNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smsnotification = models.CharField(db_column='SMSNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowrecur = models.BooleanField(db_column='AllowRecur', blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault', blank=True, null=True)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='EmailSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messageheader = models.CharField(db_column='MessageHeader', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messagefooter = models.CharField(db_column='MessageFooter', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblCustomTemplate'


class Smstbldatadriventemplate(models.Model):
    datadriventemplateid = models.AutoField(db_column='DataDrivenTemplateID', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=100)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    sqltext = models.CharField(db_column='SQLText', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    distlist = models.CharField(db_column='DistList', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    templatetext = models.CharField(db_column='TemplateText', max_length=320)  # Field name made lowercase.
    querytemplate = models.CharField(db_column='QueryTemplate', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    isemail = models.BooleanField(db_column='IsEmail', blank=True, null=True)  # Field name made lowercase.
    queryjoincol = models.CharField(db_column='QueryJoinCol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distjoincol = models.CharField(db_column='DistJoinCol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smscol = models.CharField(db_column='SMSCol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailcol = models.CharField(db_column='EmailCol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailnotification = models.CharField(db_column='EmailNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smsnotification = models.CharField(db_column='SMSNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowrecur = models.BooleanField(db_column='AllowRecur', blank=True, null=True)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='EmailSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault', blank=True, null=True)  # Field name made lowercase.
    messageheader = models.CharField(db_column='MessageHeader', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messagefooter = models.CharField(db_column='MessageFooter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblDataDrivenTemplate'


class Smstbldefaults(models.Model):
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    recurdays = models.IntegerField(db_column='RecurDays', blank=True, null=True)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='EmailSubject', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblDefaults'


class Smstbldistributionlist(models.Model):
    distributionlistid = models.AutoField(db_column='DistributionListID', primary_key=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityID')  # Field name made lowercase.
    boptout = models.BooleanField(db_column='bOptOut')  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblDistributionList'


class Smstblexclusionlist(models.Model):
    exclusionlistid = models.AutoField(db_column='ExclusionListID', primary_key=True)  # Field name made lowercase.
    templateid = models.ForeignKey('Smstbltrantemplate', models.DO_NOTHING, db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityID')  # Field name made lowercase.
    boptout = models.BooleanField(db_column='bOptOut')  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblExclusionList'


class Smstbllog(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    messagedate = models.DateTimeField(db_column='MessageDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entitynumber = models.CharField(db_column='EntityNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityemail = models.CharField(db_column='EntityEMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smstext = models.CharField(db_column='SMSText', max_length=480, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bdelivered = models.BooleanField(db_column='bDelivered', blank=True, null=True)  # Field name made lowercase.
    logtype = models.CharField(db_column='LogType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblLog'


class Smstblmastertables(models.Model):
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.
    tablecaption = models.CharField(db_column='TableCaption', max_length=100)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblMasterTables'


class Smstblmastertemplate(models.Model):
    mastertemplateid = models.AutoField(db_column='MasterTemplateID', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=100)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    templatetext = models.CharField(db_column='TemplateText', max_length=320)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    querytemplate = models.CharField(db_column='QueryTemplate', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    filter = models.CharField(db_column='Filter', max_length=500, blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    isemail = models.BooleanField(db_column='IsEmail', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault', blank=True, null=True)  # Field name made lowercase.
    emailnotification = models.CharField(db_column='EmailNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smsnotification = models.CharField(db_column='SMSNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    allowrecur = models.BooleanField(db_column='AllowRecur', blank=True, null=True)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='EmailSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messageheader = models.CharField(db_column='MessageHeader', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messagefooter = models.CharField(db_column='MessageFooter', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblMasterTemplate'


class Smstblpeoplelist(models.Model):
    peoplelistid = models.AutoField(db_column='PeopleListID', primary_key=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityID')  # Field name made lowercase.
    boptout = models.BooleanField(db_column='bOptOut')  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblPeopleList'


class Smstblreportlayout(models.Model):
    idreportlayout = models.AutoField(db_column='idReportLayout', primary_key=True)  # Field name made lowercase.
    crptdescription = models.CharField(db_column='cRptDescription', max_length=80)  # Field name made lowercase.
    imoduleid = models.IntegerField(db_column='iModuleId', blank=True, null=True)  # Field name made lowercase.
    iversion = models.IntegerField(db_column='iVersion', blank=True, null=True)  # Field name made lowercase.
    nlayout = models.BinaryField(db_column='nLayout')  # Field name made lowercase.
    breadonly = models.BooleanField(db_column='bReadOnly')  # Field name made lowercase.
    bisdefaultlayout = models.BooleanField(db_column='bIsDefaultLayout', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblReportLayout'


class Smstblschedules(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freqtype = models.IntegerField(db_column='FreqType', blank=True, null=True)  # Field name made lowercase.
    dailyrecure = models.IntegerField(db_column='DailyRecure', blank=True, null=True)  # Field name made lowercase.
    weekrecure = models.CharField(db_column='WeekRecure', max_length=200, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    lastrunon = models.DateTimeField(db_column='LastRunOn', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    intervalminute = models.IntegerField(db_column='IntervalMinute', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblSchedules'


class Smstbltask(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    taskdate = models.DateTimeField(db_column='TaskDate', blank=True, null=True)  # Field name made lowercase.
    smsnumber = models.CharField(db_column='SMSNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smstext = models.TextField(db_column='SMSText', blank=True, null=True)  # Field name made lowercase.
    istaskcompleted = models.BooleanField(db_column='IsTaskCompleted', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    thresholdexceed = models.BooleanField(db_column='ThresholdExceed', blank=True, null=True)  # Field name made lowercase.
    notificationsent = models.BooleanField(db_column='NotificationSent', blank=True, null=True)  # Field name made lowercase.
    isemail = models.BooleanField(db_column='IsEmail', blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    emailsent = models.BooleanField(db_column='EmailSent', blank=True, null=True)  # Field name made lowercase.
    smssent = models.BooleanField(db_column='SMSSent', blank=True, null=True)  # Field name made lowercase.
    mailsubject = models.CharField(db_column='MailSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblTask'


class Smstbltaskreport(models.Model):
    taskreportid = models.AutoField(db_column='TaskReportID', primary_key=True)  # Field name made lowercase.
    execdate = models.DateTimeField(db_column='ExecDate', blank=True, null=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    tasktype = models.CharField(db_column='TaskType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblTaskReport'


class Smstbltrantables(models.Model):
    trantableid = models.AutoField(db_column='TranTableID', primary_key=True)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tablecaption = models.CharField(db_column='TableCaption', max_length=100)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50)  # Field name made lowercase.
    joinquery = models.CharField(db_column='JoinQuery', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wherequery = models.CharField(db_column='WhereQuery', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    peoplejoin = models.CharField(db_column='PeopleJoin', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblTranTables'


class Smstbltrantemplate(models.Model):
    trantemplateid = models.AutoField(db_column='TranTemplateID', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=100)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tableid = models.ForeignKey(Smstbltrantables, models.DO_NOTHING, db_column='TableID', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    templatetext = models.CharField(db_column='TemplateText', max_length=320)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    querytemplate = models.CharField(db_column='QueryTemplate', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    isemail = models.BooleanField(db_column='IsEmail', blank=True, null=True)  # Field name made lowercase.
    isordercreation = models.BooleanField(db_column='IsOrderCreation', blank=True, null=True)  # Field name made lowercase.
    isstatuschange = models.BooleanField(db_column='IsStatusChange', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    bdefault = models.BooleanField(db_column='bDefault', blank=True, null=True)  # Field name made lowercase.
    emailnotification = models.CharField(db_column='EmailNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smsnotification = models.CharField(db_column='SMSNotification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='EmailSubject', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblTranTemplate'


class Smstbltrignote(models.Model):
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=400, blank=True, null=True)  # Field name made lowercase.
    notedate = models.DateTimeField(db_column='NoteDate', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.CharField(db_column='OrderNum', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_smstblTrigNote'


class Wtblpemmobilitymodules(models.Model):
    idmobilitymodule = models.AutoField(db_column='idMobilityModule', primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='cCode', max_length=50)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=50)  # Field name made lowercase.
    cdescription = models.TextField(db_column='cDescription')  # Field name made lowercase.
    imoduletypeid = models.IntegerField(db_column='iModuleTypeId')  # Field name made lowercase.
    gidentifier = models.CharField(db_column='gIdentifier', max_length=36, blank=True, null=True)  # Field name made lowercase.
    biswinjitmodule = models.BooleanField(db_column='bIsWinjitModule')  # Field name made lowercase.
    bisoneagentperdevice = models.BooleanField(db_column='bIsOneAgentPerDevice')  # Field name made lowercase.
    bismultipledeviceperagent = models.BooleanField(db_column='bIsMultipleDevicePerAgent')  # Field name made lowercase.
    bisactive = models.BooleanField(db_column='bIsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_wtblPEMMobilityModules'


class Wtblsystem(models.Model):
    idsystem = models.AutoField(db_column='idSystem', primary_key=True)  # Field name made lowercase.
    cidentity = models.CharField(db_column='cIdentity', max_length=35, blank=True, null=True)  # Field name made lowercase.
    cvalue = models.CharField(db_column='cValue', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_wtblSystem'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class OdmsOrder(models.Model):
    customer_id = models.IntegerField(db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odms_order'


class OdmsProducts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'odms_products'
