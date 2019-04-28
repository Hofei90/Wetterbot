from peewee import *

database = SqliteDatabase('weewx.sdb', **{})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Archive(BaseModel):
    et = FloatField(column_name='ET', null=True)
    uv = FloatField(column_name='UV', null=True)
    altimeter = FloatField(null=True)
    barometer = FloatField(null=True)
    consbatteryvoltage = FloatField(column_name='consBatteryVoltage', null=True)
    datetime = AutoField(column_name='dateTime')
    dewpoint = FloatField(null=True)
    extrahumid1 = FloatField(column_name='extraHumid1', null=True)
    extrahumid2 = FloatField(column_name='extraHumid2', null=True)
    extratemp1 = FloatField(column_name='extraTemp1', null=True)
    extratemp2 = FloatField(column_name='extraTemp2', null=True)
    extratemp3 = FloatField(column_name='extraTemp3', null=True)
    hail = FloatField(null=True)
    hailrate = FloatField(column_name='hailRate', null=True)
    heatindex = FloatField(null=True)
    heatingtemp = FloatField(column_name='heatingTemp', null=True)
    heatingvoltage = FloatField(column_name='heatingVoltage', null=True)
    inhumidity = FloatField(column_name='inHumidity', null=True)
    intemp = FloatField(column_name='inTemp', null=True)
    intempbatterystatus = FloatField(column_name='inTempBatteryStatus', null=True)
    interval = IntegerField()
    leaftemp1 = FloatField(column_name='leafTemp1', null=True)
    leaftemp2 = FloatField(column_name='leafTemp2', null=True)
    leafwet1 = FloatField(column_name='leafWet1', null=True)
    leafwet2 = FloatField(column_name='leafWet2', null=True)
    outhumidity = FloatField(column_name='outHumidity', null=True)
    outtemp = FloatField(column_name='outTemp', null=True)
    outtempbatterystatus = FloatField(column_name='outTempBatteryStatus', null=True)
    pressure = FloatField(null=True)
    radiation = FloatField(null=True)
    rain = FloatField(null=True)
    rainbatterystatus = FloatField(column_name='rainBatteryStatus', null=True)
    rainrate = FloatField(column_name='rainRate', null=True)
    referencevoltage = FloatField(column_name='referenceVoltage', null=True)
    rxcheckpercent = FloatField(column_name='rxCheckPercent', null=True)
    soilmoist1 = FloatField(column_name='soilMoist1', null=True)
    soilmoist2 = FloatField(column_name='soilMoist2', null=True)
    soilmoist3 = FloatField(column_name='soilMoist3', null=True)
    soilmoist4 = FloatField(column_name='soilMoist4', null=True)
    soiltemp1 = FloatField(column_name='soilTemp1', null=True)
    soiltemp2 = FloatField(column_name='soilTemp2', null=True)
    soiltemp3 = FloatField(column_name='soilTemp3', null=True)
    soiltemp4 = FloatField(column_name='soilTemp4', null=True)
    supplyvoltage = FloatField(column_name='supplyVoltage', null=True)
    txbatterystatus = FloatField(column_name='txBatteryStatus', null=True)
    usunits = IntegerField(column_name='usUnits')
    windbatterystatus = FloatField(column_name='windBatteryStatus', null=True)
    winddir = FloatField(column_name='windDir', null=True)
    windgust = FloatField(column_name='windGust', null=True)
    windgustdir = FloatField(column_name='windGustDir', null=True)
    windspeed = FloatField(column_name='windSpeed', null=True)
    windchill = FloatField(null=True)

    class Meta:
        table_name = 'archive'


class ArchiveDayEt(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_ET'


class ArchiveDayUv(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_UV'


class ArchiveDayMetadata(BaseModel):
    name = CharField(primary_key=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'archive_day__metadata'


class ArchiveDayAltimeter(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_altimeter'


class ArchiveDayBarometer(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_barometer'


class ArchiveDayConsbatteryvoltage(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_consBatteryVoltage'


class ArchiveDayDewpoint(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_dewpoint'


class ArchiveDayExtrahumid1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_extraHumid1'


class ArchiveDayExtrahumid2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_extraHumid2'


class ArchiveDayExtratemp1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_extraTemp1'


class ArchiveDayExtratemp2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_extraTemp2'


class ArchiveDayExtratemp3(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_extraTemp3'


class ArchiveDayHail(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_hail'


class ArchiveDayHailrate(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_hailRate'


class ArchiveDayHeatindex(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_heatindex'


class ArchiveDayHeatingtemp(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_heatingTemp'


class ArchiveDayHeatingvoltage(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_heatingVoltage'


class ArchiveDayInhumidity(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_inHumidity'


class ArchiveDayIntemp(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_inTemp'


class ArchiveDayIntempbatterystatus(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_inTempBatteryStatus'


class ArchiveDayLeaftemp1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_leafTemp1'


class ArchiveDayLeaftemp2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_leafTemp2'


class ArchiveDayLeafwet1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_leafWet1'


class ArchiveDayLeafwet2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_leafWet2'


class ArchiveDayOuthumidity(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_outHumidity'


class ArchiveDayOuttemp(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_outTemp'


class ArchiveDayOuttempbatterystatus(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_outTempBatteryStatus'


class ArchiveDayPressure(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_pressure'


class ArchiveDayRadiation(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_radiation'


class ArchiveDayRain(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_rain'


class ArchiveDayRainbatterystatus(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_rainBatteryStatus'


class ArchiveDayRainrate(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_rainRate'


class ArchiveDayReferencevoltage(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_referenceVoltage'


class ArchiveDayRxcheckpercent(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_rxCheckPercent'


class ArchiveDaySoilmoist1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilMoist1'


class ArchiveDaySoilmoist2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilMoist2'


class ArchiveDaySoilmoist3(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilMoist3'


class ArchiveDaySoilmoist4(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilMoist4'


class ArchiveDaySoiltemp1(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilTemp1'


class ArchiveDaySoiltemp2(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilTemp2'


class ArchiveDaySoiltemp3(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilTemp3'


class ArchiveDaySoiltemp4(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_soilTemp4'


class ArchiveDaySupplyvoltage(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_supplyVoltage'


class ArchiveDayTxbatterystatus(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_txBatteryStatus'


class ArchiveDayWind(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    dirsumtime = IntegerField(null=True)
    max = FloatField(null=True)
    max_dir = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    squaresum = FloatField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsquaresum = FloatField(null=True)
    wsum = FloatField(null=True)
    xsum = FloatField(null=True)
    ysum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_wind'


class ArchiveDayWindbatterystatus(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windBatteryStatus'


class ArchiveDayWinddir(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windDir'


class ArchiveDayWindgust(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windGust'


class ArchiveDayWindgustdir(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windGustDir'


class ArchiveDayWindspeed(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windSpeed'


class ArchiveDayWindchill(BaseModel):
    count = IntegerField(null=True)
    datetime = AutoField(column_name='dateTime')
    max = FloatField(null=True)
    maxtime = IntegerField(null=True)
    min = FloatField(null=True)
    mintime = IntegerField(null=True)
    sum = FloatField(null=True)
    sumtime = IntegerField(null=True)
    wsum = FloatField(null=True)

    class Meta:
        table_name = 'archive_day_windchill'
