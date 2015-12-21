from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


#-----------------------大队表-------------------------------------
class Dgroup(models.Model):
    """
    ------------------------------------------------------
    |    did      int         8    no    主键
    |    dname    varchar    32    no    大队名称
    |    daddr    varchar    32    no    大队地址
    |    dtime    datetime   32    no    大队创建时间
    ------------------------------------------------------
    """
    dname = models.CharField(max_length=32, verbose_name="大队名称") # 大队名称
    daddr = models.CharField(max_length=32, verbose_name="大队地址") # 大队地址
    dtime = models.DateTimeField(verbose_name="大队创建时间")          # 大队创建时间

    def __str__(self):
        return "大队名称为：" + self.dname




#-----------------------------中队表------------------------------
class Zgroup(models.Model):
    """
    --------------------------------------------------------
    |    zid      int         8     no    主键
    |    did      int         8     no    大队表外键
    |    zname    varchar     32    no    中队名称
    |    zaddr    varchar     32    no    中队地址
    |    ztime    datetime    32    no    中队创建时间
    --------------------------------------------------------
    """

    did   = models.ForeignKey(Dgroup)       # 大队外键表
    zname = models.CharField(max_length=32,verbose_name="中队名称") # 中队名称
    zaddr = models.CharField(max_length=32,verbose_name="中队地址") # 中队地址
    ztime = models.DateTimeField(verbose_name="中队创建时间")          # 中队创建时间

    def __str__(self):
        return "中队名称为：" + self.zname

#----------------------------管理员权限表---------------------------
class Admin(models.Model):
    """
    -----------------------------------------------------------
    |    aid         int          8    no    主键
    |    apower      int         11    no    权限    或许用1248 2的0 2的1 2的2 2的3次方形式更好？
    |    atime       datetime    32    no    授权时间
    -----------------------------------------------------------
    """
    apower  = models.IntegerField(verbose_name="权限")
    atime   = models.DateTimeField(verbose_name="管理员创建时间")

    def __str__(self):
        return "管理员用户ID为： " + str(self.apower)


#--------------------------------用户表-----------------------------
class User(models.Model):
    """
    ---------------------------------------------------
    |   uid      int         8    no    主键
    |   zid      int         8    no    中队表外键
    |   aid      int         8    no    管理员权限表外键
    |   uname    varchar    32    no    用户名
    |   upass    varchar    32    no    密码
    |   utime    datetime   32    no    用户注册时间
    ---------------------------------------------------
    """

    zid    = models.ForeignKey(Zgroup)        # 中队外键表
    aid    = models.ForeignKey(Admin)         # 管理员权限外键
    uname  = models.CharField(max_length=32, verbose_name="用户名")  # 用户名
    upass  = models.CharField(max_length=32, verbose_name="密码")  # 密码
    utime  = models.DateTimeField(verbose_name="注册时间")           # 注册时间

    def __str__(self):
        return "用户名为：" + self.uname


#---------------------------------火场信息表-----------------------------
class Fireinfo(models.Model):
    """
    ----------------------------------------------------------------

    |    zid          int         8    no    中队表外键
    |    fcar         int         8    no    出动 车辆数
    |    fperson      int         8    no    出动人员数
    |    faddr        varchar    32    no    事故现场地址
    |    ftype        varchar    32    no    着火类型
    |    fmaterial    varchar    32    no    燃烧物质
    |    fhelptime    datetime   32    no    救助时间
    |    finishtime   datetime   32    no    结束时间
    |    fhelp        int              no    救助人数
    |    fhurt        int              no    受伤人数
    |    fdie         int              no    死亡人数
    |    farea        int                    过火面积（平米）
    |    fmoney       decimal                损失（万）
    |    fcontent     varchar    32    no    救助情况（车到火灭）
    |    freason      varchar    32          原因
    |    ftime        datetime   32    no    填表时间
    ----------------------------------------------------------------
    """
    zid  = models.ForeignKey(Zgroup, verbose_name="主战中队")                # 中队表外键
    fcar = models.IntegerField(verbose_name="出动车辆数")                    # 出动车辆数
    fperson = models.IntegerField(verbose_name="出动人员数")                 # 出动人员数
    faddr = models.CharField(max_length=32,verbose_name="事故现场地址")         # 事故现场地址
    ftype = models.CharField(max_length=32, verbose_name="着火类型")         # 着火类型
    fmaterial = models.CharField(max_length=32, verbose_name="燃烧物质")     # 燃烧物质
    fhelptime = models.DateTimeField(verbose_name="救助时间")              # 救助时间
    finishtime = models.DateTimeField(verbose_name="结束时间")             # 结束时间
    fhelp = models.IntegerField(verbose_name="救助人数")                   # 救助人数
    fhurt = models.IntegerField(verbose_name="受伤人数")                   # 受伤人数
    fdie = models.IntegerField(verbose_name="死亡人数")                    # 死亡人数
    farea = models.IntegerField(verbose_name="过火面积")                   # 过火面积
    fmoney = models.IntegerField(verbose_name="损失金额（万元）")                 # 损失金额(万元)
    fcontent = models.CharField(max_length=32, verbose_name="救助情况")      # 救助情况（车到火灭）
    freason = models.CharField(max_length=32, verbose_name="事故原因")       # 事故原因
    ftime = models.DateTimeField(verbose_name="填表时间")                  # 填表时间

    def __str__(self):
        return "火场信息：地址为 " + self.faddr + " 着火类型 " + self.ftype + " 事故原因 " + self.freason




#--------------------------------增援信息表---------------------------------
class Reinforce(models.Model):
    """
    ------------------------------------------------------------
    |    rid            int          8    no    主键
    |    id             int          8    no    火场外键
    |    zid            int          8    no    中队表外键
    |    fcar           int          8    no    出动 车辆数
    |    fperson        int          8    no    出动人员数
    |    rhelptime      datetime    32    no    增援到场时间
    |    rfinishtime    datetime    32    no    结束时间
    |    rtime          datetime    32    no    填表时间
    ------------------------------------------------------------
    """
    fid         = models.ForeignKey(Fireinfo, verbose_name="增援火场")                                #火场外键表
    zid         = models.ForeignKey(Zgroup, verbose_name="增援中队")                                  # 中队外键表
    fcar        = models.IntegerField(verbose_name="增援出动车辆数")        # 出动车辆数
    fperson     = models.IntegerField(verbose_name="增援出动人员数")        # 出动人员数
    rhelptime   = models.DateTimeField(verbose_name="增援到长时间")         # 增援到场时间
    rfinishtime = models.DateTimeField(verbose_name="增援结束时间")         # 结束时间
    rtime       = models.DateTimeField(verbose_name="填表时间")             # 填表时间

    def __str__(self):
        return "增援中队外键为： "+str(self.zid)+"火场外键表为： "+ str(self.fid)