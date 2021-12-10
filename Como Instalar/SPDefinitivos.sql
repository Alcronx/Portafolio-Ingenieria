-----------------------Usuarios---------------------
--Procedure Editar Usuarios
create or replace procedure sp_EditarUsuario(v_id varchar2,v_usuario varchar2,v_contrasena varchar2,v_rol varchar2,v_salida out number)
IS

BEGIN

UPDATE LOGIN
SET USERNAME = v_usuario,
    PASSWORDUSER = v_contrasena,
    ROL = v_rol
WHERE IDUSER = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Usuarios
create or replace procedure sp_Agregar_Usuarios(v_username varchar2, v_password varchar2, v_Rol varchar2, v_STATE varchar2,v_salida out number)
IS

BEGIN
        insert into login(USERNAME,PASSWORDUSER,ROL,STATE)
        values (v_username,v_password,v_Rol,v_STATE);
        commit;

        v_salida:= 1;
 
    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Usuarios
create or replace procedure sp_EliminarUsuario(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE LOGIN
SET STATE=0
WHERE IDUSER = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Usuario"
create or replace  procedure sp_DetallesUsuario(v_id varchar2,usuarios out SYS_REFCURSOR)
IS

BEGIN

 open usuarios for SELECT
    "A1"."IDUSER"       "IDUSER",
    "A1"."USERNAME"     "USERNAME",
    "A1"."PASSWORDUSER" "PASSWORDUSER",
    "A1"."ROL"          "ROL",
    "A1"."STATE"        "STATE"
FROM
    "RESTAURANTE"."LOGIN" "A1"
WHERE
    "A1"."STATE" = 1 AND "A1"."IDUSER"=v_id;
END;
/
--Procedure listar usuario Usuarios
create or replace procedure sp_listar_Usuarios(usuarios out SYS_REFCURSOR)
IS

BEGIN


 open usuarios for SELECT
    "A1"."IDUSER"       "IDUSER",
    "A1"."USERNAME"     "USERNAME",
    "A1"."PASSWORDUSER" "PASSWORDUSER",
    "A1"."ROL"          "ROL",
    "A1"."STATE"        "STATE"
FROM
    "RESTAURANTE"."LOGIN" "A1"
WHERE
    "A1"."STATE" = 1;
END;
/


-----------------------Mesa---------------------
--Procedure Editar Mesa
create or replace procedure sp_EditarMesa(v_id varchar2,v_tableNumber varchar2,v_tableMembers varchar2,v_aviable varchar2, v_salida out number)
IS

BEGIN

UPDATE restauranttable
SET     tablenumber =   v_tableNumber,
        tablemembers = v_tableMembers,
        aviable = v_aviable
WHERE tableid = v_id;
commit;

        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Mesa
create or replace procedure sp_Agregar_Mesa(v_tableNumber varchar2,v_tableMembers varchar2,v_aviable varchar2,v_state varchar2, v_salida out number)
IS

BEGIN
        insert into restauranttable(tablenumber,tablemembers,aviable,state)
        values (v_tableNumber,v_tableMembers,v_aviable,v_state);
        commit;

        v_salida:= 1;
 
    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Mesa
create or replace procedure sp_EliminarMesa(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE restauranttable
SET STATE=0
WHERE tableid = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Mesa"
create or replace  procedure sp_DetallesMesa(v_id varchar2,mesas out SYS_REFCURSOR)
IS

BEGIN

open mesas for SELECT
    "A1"."TABLEID"       "TABLEID",
    "A1"."TABLENUMBER"    "TABLENUMBER",
    "A1"."TABLEMEMBERS" "TABLEMEMBERS",
    "A1"."AVIABLE"      "AVIABLE",
    "A1"."STATE"    "STATE"
FROM
    "RESTAURANTE"."RESTAURANTTABLE" "A1"
WHERE
    "A1"."STATE" = 1 AND "A1"."TABLEID"=v_id;
END;
/
--Procedure listar Mesa
create or replace procedure sp_listar_Mesas(mesas out SYS_REFCURSOR)
IS
BEGIN
open mesas for SELECT
    "A1"."TABLEID"       "TABLEID",
    "A1"."TABLENUMBER"    "TABLENUMBER",
    "A1"."TABLEMEMBERS" "TABLEMEMBERS",
    "A1"."AVIABLE"      "AVIABLE",
    "A1"."STATE"    "STATE"
FROM
    "RESTAURANTE"."RESTAURANTTABLE" "A1"
WHERE
    "A1"."STATE" = 1;

END;
/
-----------------------Meseros---------------------
--Procedure Editar Meseros
create or replace procedure sp_EditarMesero(v_id varchar2,v_rut varchar2,v_name1 varchar2,v_name2 varchar2,v_lastname1 varchar2,v_lastname2 varchar2, v_salida out number)
IS

BEGIN

UPDATE waiter
SET     RUT =   v_rut,
        NAME1 =   v_name1,
        NAME2 =   v_name2,
        LASTNAME1 =   v_lastname1,
        LASTNAME2 =   v_lastname2
WHERE WAITERID = v_id;
commit;

        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Meseros
create or replace procedure sp_Agregar_Mesero(v_rut varchar2,v_name1 varchar2,v_name2 varchar2,v_lastname1 varchar2,v_lastname2 varchar2,v_state varchar2, v_salida out number)
IS

BEGIN
        insert into waiter(RUT,NAME1,NAME2,LASTNAME1,LASTNAME2,STATE)
        values (v_rut,v_name1,v_name2,v_lastname1,v_lastname2,v_state);
        commit;

        v_salida:= 1;
 
    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Meseros
create or replace procedure sp_EliminarMesero(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE waiter
SET STATE=0
WHERE waiterid = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Meseros"
create or replace  procedure sp_DetallesMesero(v_id varchar2,meseros out SYS_REFCURSOR)
IS

BEGIN

open meseros for SELECT
    "A1"."WAITERID"       "WAITERID",
    "A1"."RUT"       "RUT",
    "A1"."NAME1"    "NAME1",
    "A1"."NAME2" "NAME2",
    "A1"."LASTNAME1"      "LASTNAME1",
    "A1"."LASTNAME2"    "LASTNAME2",
    "A1"."STATE"    "STATE"
FROM
    "RESTAURANTE"."WAITER" "A1"
WHERE
    "A1"."STATE" = 1 AND "A1"."WAITERID"=v_id;
END;
/
--Procedure listar Meseros
create or replace procedure sp_listar_Meseros(meseros out SYS_REFCURSOR)
IS
BEGIN
open meseros for SELECT
    "A1"."WAITERID"       "WAITERID",
    "A1"."RUT"       "RUT",
    "A1"."NAME1"    "NAME1",
    "A1"."NAME2" "NAME2",
    "A1"."LASTNAME1"      "LASTNAME1",
    "A1"."LASTNAME2"    "LASTNAME2",
    "A1"."STATE"    "STATE"
FROM
    "RESTAURANTE"."WAITER" "A1"
WHERE
    "A1"."STATE" = 1 ;

END;
/

-----------------------Reserva---------------------
--Procedure Editar Reserva
create or replace procedure sp_EditarReserva(v_id varchar2,v_reserveDate varchar2,v_reserveHour varchar2,v_tableId varchar2, v_salida out number)
IS
BEGIN
UPDATE reserved
SET     reservedate =   to_date(v_reserveDate, 'yyyy-mm-dd'), 
        reservehour = to_date(v_reserveHour, 'hh24-mi'),
        rt_tableid = v_tableId
WHERE RESERVEID = v_id;
commit;
        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Reserva
create or replace procedure sp_Agregar_Reserva(v_reserveDate varchar2, v_reserveHour varchar2, v_tableId varchar2, v_state varchar2, v_salida out number)
IS

BEGIN
        insert into reserved(reservedate,reservehour,state,rt_tableid)
        values (to_date(v_reserveDate, 'yyyy-mm-dd'),to_date(v_reserveHour, 'hh24-mi'),1,v_tableId);
        commit;



        v_salida:= 1;
 
    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Reserva
create or replace procedure sp_EliminarReserva(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE reserved
SET STATE=0
WHERE reserveid = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Reserva"
create or replace  procedure sp_DetallesReserva(v_id varchar2,reservas out SYS_REFCURSOR)
IS

BEGIN

open reservas for SELECT
        T1.RESERVEID ,
        to_char(T1.RESERVEDATE,'YYYY-MM-DD') ,
        to_char(T1.RESERVEHOUR,'hh24:mi') ,
        T1.STATE ,
        T2.TABLENUMBER,  
        T1.RT_TABLEID 
FROM
    reserved T1
INNER JOIN RESTAURANTTABLE T2 ON
    T1.RT_TABLEID = T2.TABLEID
WHERE T1.STATE = 1 AND T1.RESERVEID = v_id;
END;
/
--Procedure listar Reserva
create or replace procedure sp_listar_Reservas(reservas out SYS_REFCURSOR)
IS
BEGIN
open reservas for SELECT
        T1.RESERVEID ,
        to_char(T1.RESERVEDATE,'dd-mm-yyyy') ,
        to_char(T1.RESERVEHOUR,'hh24:mi') ,
        T1.STATE ,
        T2.TABLENUMBER,  
        T1.RT_TABLEID 
FROM
    reserved T1
INNER JOIN RESTAURANTTABLE T2 ON
    T1.RT_TABLEID = T2.TABLEID
WHERE T1.STATE = 1;

END;
/


-----------------------Proveedor---------------------
--Procedure Editar Proveedor
create or replace  procedure sp_EditarProveedor(v_id varchar2,v_rut varchar2,v_companyname varchar2,v_name1 varchar2,v_name2 varchar2,v_lastname1 varchar2,v_lastname2 varchar2,v_region varchar2,v_commune varchar2,v_direction varchar2,v_cellphone varchar2,v_mail varchar2, v_salida out number)
IS 
BEGIN
UPDATE PROVIDER
SET     
        RUT = v_rut,
        COMPANYNAME =v_companyname,
        NAME1 = v_name1,
        NAME2 = v_name2,
        LASTNAME1 = v_lastname1,
        LASTNAME2 = v_lastname2,
        REGION = v_region,
        COMMUNE = v_commune,
        DIRECTION = v_direction,
        CELLPHONE = v_cellphone,
        MAIL = v_mail
        WHERE IDPROVIDER = v_id;
commit;

        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Proveedor
create or replace procedure sp_Agregar_Proveedor
(v_rut varchar2,v_companyname varchar2,v_name1 varchar2,v_name2 varchar2,v_lastname1 varchar2,v_lastname2 varchar2,v_region varchar2,v_commune varchar2,v_direction varchar2,v_cellphone varchar2,v_mail varchar2, v_state varchar2, v_salida out number)
IS

BEGIN
        insert into provider(rut,companyname,name1,name2,lastname1,lastname2,region,commune,direction,cellphone,mail,state)
        values (v_rut ,v_companyname ,v_name1 ,v_name2 ,v_lastname1 ,v_lastname2 ,v_region ,v_commune ,v_direction ,v_cellphone ,v_mail , v_state );
        commit;

        v_salida:= 1;

    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Proveedor
create or replace procedure sp_EliminarProveedor(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE PROVIDER
SET STATE=0
WHERE IDPROVIDER = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Proveedor"
create or replace procedure sp_DetallesProveedor(v_id varchar2,proveedores out SYS_REFCURSOR)
IS

BEGIN

open proveedores for 
        select  IDPROVIDER ,
                RUT ,
                COMPANYNAME ,
                NAME1 ,
                NAME2 ,
                LASTNAME1 ,
                LASTNAME2 ,
                REGION ,
                COMMUNE ,
                DIRECTION ,
                CELLPHONE ,
                MAIL ,
                STATE  
        from 
        PROVIDER
        WHERE
        STATE = 1 AND IDPROVIDER=v_id;
END;
/
--Procedure listar Proveedor
create or replace  procedure sp_listar_Proveedores(proveedores out SYS_REFCURSOR)
IS
BEGIN
open proveedores for 
select  IDPROVIDER ,
        RUT ,
        COMPANYNAME ,
        NAME1 ,
        NAME2 ,
        LASTNAME1 ,
        LASTNAME2 ,
        REGION ,
        COMMUNE ,
        DIRECTION ,
        CELLPHONE ,
        MAIL ,
        STATE  
from 
PROVIDER
WHERE
    STATE = 1;
END;
/
-----------------------Producto---------------------
--Procedure Editar Producto
create or replace procedure sp_EditarProducto(v_id varchar2,v_purchaseprice varchar2,v_stock varchar2,v_criticalstock varchar2,v_productname varchar2,v_productdescription varchar2,v_p_idprovider varchar2, v_salida out number) 
IS
BEGIN
UPDATE product
SET     
        purchaseprice = v_purchaseprice,
        stock = v_stock,
        criticalstock = v_criticalstock,
        productname = v_productname,
        productdescription = v_productdescription,
        p_idprovider =  v_p_idprovider
WHERE productid = v_id;
commit;
        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure Agregar Producto
create or replace procedure sp_Agregar_Producto(v_purchaseprice varchar2,v_stock varchar2,v_criticalstock varchar2,v_productname varchar2,v_productdescription varchar2,v_state varchar2,v_p_idprovider varchar2, v_salida out number)
IS

BEGIN
        insert into product(purchaseprice,stock,criticalstock,productname,productdescription,state,p_idprovider)
        values (v_purchaseprice,v_stock,v_criticalstock,v_productname,v_productdescription,v_state,v_p_idprovider);
        commit;
        v_salida:= 1;

    EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;
END;
/
--Procedure "eliminar" Producto
create or replace procedure sp_EliminarProducto(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE product
SET STATE=0
WHERE PRODUCTID = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Detalles Producto"
create or replace procedure sp_DetallesProducto(v_id varchar2,productos out SYS_REFCURSOR)
IS

BEGIN

open productos for 
select  PRODUCTID ,
        PURCHASEPRICE ,
        STOCK ,
        CRITICALSTOCK ,
        PRODUCTNAME ,
        PRODUCTDESCRIPTION ,
        STATE ,
        P_IDPROVIDER  
from Product
WHERE STATE = 1 AND PRODUCTID = v_id;
END;
/
--Procedure listar Producto
create or replace  procedure sp_listar_Productos(reservas out SYS_REFCURSOR)
IS
BEGIN
open reservas for
select  T1.PRODUCTID ,
        T1.PURCHASEPRICE ,
        T1.STOCK ,
        T1.CRITICALSTOCK ,
        T1.PRODUCTNAME ,
        T1.PRODUCTDESCRIPTION ,
        T1.STATE ,
        T1.P_IDPROVIDER,
        t2.companyname
from Product T1 inner join provider T2 ON t1.p_idprovider=t2.idprovider
WHERE T1.STATE = 1;
END;
/

-----------------------Bodega---------------------
--Procedure Productos Provedor
create or replace  procedure sp_listar_Productos_Proveedor(v_id varchar2, productos out SYS_REFCURSOR)
IS
BEGIN
open productos for
select  T2.idprovider,
        T1.Productid,
        T1.PRODUCTNAME,
        T2.COMPANYNAME,
        T1.PURCHASEPRICE,
        T1.STOCK,
        T1.CRITICALSTOCK
from Product T1 inner join provider T2 ON t1.p_idprovider=t2.idprovider
WHERE T1.STATE = 1 and T2.idprovider = v_id;
END;
/
--ComboboxProveedores
create or replace  procedure sp_listar_Combobox_Proveedor(Proveedor out SYS_REFCURSOR)
IS
BEGIN
open Proveedor for
select IDPROVIDER,COMPANYNAME 
FROM provider
WHERE STATE=1;
END;
/

--Procedure Agregar Orden
create or replace procedure sp_Agregar_OrdenProducto(v_totalTotal varchar2,v_state varchar2,v_id out number, v_salida out number)
IS

BEGIN
        insert into orderproduct (orderdate,orderhour,receptiondate,receptionhour,totalorderproduct,state) 
        values (SYSDATE,SYSDATE,null,null,v_totalTotal,v_state) 
        returning ORDERPRODUCTID into v_id;
        commit;
        v_salida:= 1;
        EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;

END;
/
--Procedure "eliminar" Orden
create or replace procedure sp_EliminarOrdenProducto(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE orderproduct
SET STATE=0
WHERE ORDERPRODUCTID = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Listar" Orden Producto
create or replace  procedure sp_listar_OrdenesProducto(ordenes out SYS_REFCURSOR)
IS
BEGIN
open ordenes for 
select  ORDERPRODUCTID ,
        to_char(ORDERDATE,'DD-MM-YYYY') ,
        to_char(ORDERHOUR,'hh24:mi') ,
        nvl(to_char(RECEPTIONDATE,'DD-MM-YYYY'),'No Recibido') ,
        nvl(to_char(RECEPTIONHOUR,'hh24:mi'), 'No Recibido'),
        TO_CHAR(TOTALORDERPRODUCT,'$999G999G999G999') ,
        STATE  from orderProduct
WHERE
    STATE = 1;
END;
/
--Procedure "listar" OrdenProductoDetalle
create or replace  procedure sp_listar_OrdenesProductoDetalle(v_id varchar2,ordenesDetalles out SYS_REFCURSOR)
IS
BEGIN
open ordenesDetalles for 
select op.ORDERPRODUCTID,opd.opdproductid,p.productname,opd.quantity,opd.total from 
orderproduct op inner join orderproductdetails opd
on op.ORDERPRODUCTID = opd.opdorderproductid inner join product p on p.productid = opd.opdproductid
where op.ORDERPRODUCTID = v_id and op.state=1;
END;
/
--Procedure Confirmar Orden
create or replace procedure sp_ConfirmarOrdenProducto(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE orderproduct
set receptiondate= SYSDATE ,receptionhour= SYSDATE
WHERE ORDERPRODUCTID = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
    v_salida:= -1;      
end;
/
--Procedure Desconfirmar Orden
create or replace procedure sp_DesconfirmarOrdenProducto(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE orderproduct
set receptiondate= null ,receptionhour= null
WHERE ORDERPRODUCTID = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
    v_salida:= -1;      
end;
/
-----------------------Stock Producto---------------------
--Procedure Editar Stock Producto
create or replace procedure sp_EditarStockProducto(v_id varchar2,v_stock varchar2,v_criticalstock varchar2, v_salida out number) 
IS
BEGIN
UPDATE product
SET     
        stock = v_stock,
        criticalstock = v_criticalstock
WHERE productid = v_id;
commit;
        v_salida:= 1;
EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
end;
/
--Procedure "Detalles Stock Producto"
create or replace procedure sp_DetallesStockProducto(v_id varchar2,productos out SYS_REFCURSOR)
IS

BEGIN

open productos for 
select  PRODUCTID ,
        PURCHASEPRICE ,
        STOCK ,
        CRITICALSTOCK ,
        PRODUCTNAME ,
        PRODUCTDESCRIPTION ,
        STATE ,
        P_IDPROVIDER  
from Product
WHERE STATE = 1 AND PRODUCTID = v_id;
END;
/
--Procedure listar Producto
create or replace  procedure sp_listar_StockProductos(productos out SYS_REFCURSOR)
IS
BEGIN
open productos for
select  T1.PRODUCTID ,
        T1.PURCHASEPRICE ,
        T1.STOCK ,
        T1.CRITICALSTOCK ,
        T1.PRODUCTNAME ,
        T1.PRODUCTDESCRIPTION ,
        T1.STATE ,
        T1.P_IDPROVIDER,
        t2.companyname
from Product T1 inner join provider T2 ON t1.p_idprovider=t2.idprovider
WHERE T1.STATE = 1;
END;
/

----------------------Menu Producto-------------------------------------------------------

create or replace procedure SP_AGREGAR_MENUPRODUCTO(v_recipe varchar2,v_cookingtime varchar2,v_menucost varchar2,v_menuprice varchar2,v_name varchar2,v_state varchar2,v_id out number, v_salida out number)
IS

BEGIN
        insert into menu (recipe,cookingtime,menucost,menuprice,name,state) 
        values (v_recipe,to_date(v_cookingtime, 'hh24-mi'),v_menucost,v_menuprice,v_name,v_state) 
        returning menuid into v_id;
        commit;
        v_salida:= 1;
        EXCEPTION
            WHEN OTHERS THEN
        v_salida:= -1;  

END;
/


--Procedure "eliminar" Orden
create or replace procedure sp_EliminarMenuProducto(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE menu
SET STATE=0
WHERE MENUID = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
        v_salida:= -1;      
end;
/
--Procedure "Listar" MENU Producto
create or replace  procedure sp_listar_MenusProducto(menus out SYS_REFCURSOR)
IS
BEGIN
open menus for 
select  MENUID,
        RECIPE,
        to_char(COOKINGTIME,'hh24:mi'), 
        TO_CHAR(menucost,'$999G999G999G999'),
        TO_CHAR(menuprice,'$999G999G999G999'),
        NAME,
        STATE  from menu
WHERE
    STATE = 1;
END;
/
--Procedure "listar" OrdenProductoDetalle
create or replace  procedure sp_listar_ProductoDetalle(v_id varchar2,menus out SYS_REFCURSOR)
IS
BEGIN
open menus for 
select m.menuid,pm.pmproductid,p.productname,pm.quantity,pm.total from 
MENU M inner join PRODUCTMENU PM
on M.MENUID = pm.pmmenuid inner join product p on p.productid = pm.pmproductid
where M.menuid = v_id and m.state=1;
END;
/


----------------------Tablero COCINA-------------------------------------------------------
----------------------Listar orden Cliente ------------------------------------------------
create or replace  procedure sp_listar_OrdenesClientes(ordenesCliente out SYS_REFCURSOR)
IS
BEGIN
open ordenesCliente for 
select DISTINCT 
oc.ORDECLIENTID ORDECLIENTID,
wa.WAITERID WAITERID,
c.CLIENTID CLIENTID,
rt.TABLEID TABLEID,
oc.ORDERHOUR ORDERHOUR,
oc.ORDERDATE ORDERDATE,
oc.STATE OrderClientState,
wa.NAME1 NAMEWAITER,
wa.LASTNAME1 LAASTNAMEWAITER,
c.NAME NAMEClient,
rt.TABLENUMBER TABLENUMBER
from menu Me inner join orderclientdetails ocd on Me.menuid = ocd.ocdmenuid inner join orderclient oc on oc.ordeclientid = ocd.ocdorderclientid
inner join waiter wa on wa.waiterid = oc.waiter_waiterid inner join client c on c.clientid= oc.client_clientid inner join restauranttable rt on rt.tableid= c.rt_tableid
where oc.STATE = 1 ORDER BY oc.ORDERHOUR asc,oc.ORDERDATE asc;
END;
/
----------------------Listar Detalles orden Cliente ------------------------------------------------
create or replace  procedure sp_listar_DetallesOrdenesClientes(v_id varchar2, Detallesordenes out SYS_REFCURSOR)
IS
BEGIN
open Detallesordenes for 
select
Me.NAME NAME,
ocd.QUIANTITY QUIANTITY
from menu Me inner join orderclientdetails ocd on Me.menuid = ocd.ocdmenuid inner join orderclient oc on oc.ordeclientid = ocd.ocdorderclientid
where oc.ORDECLIENTID = v_id; 
END;
/

--Procedure Confirmar OrdenCliente
create or replace procedure sp_ConfirmarOrdenCliente(v_id varchar2, v_salida out number)
IS

BEGIN

UPDATE orderclient
set STATE = 0
WHERE ordeclientid = v_id;
commit;
    v_salida:= 1;
EXCEPTION
    WHEN OTHERS THEN
    v_salida:= -1;      
end;
/
----------------------Totems-------------------------------------------------------
--Procedure Listar OrdenesClientes
create or replace  procedure sp_listar_MesasTotemCliente(v_Miembros number,listadoMesa out SYS_REFCURSOR)
IS
BEGIN
open listadoMesa for
select 
TABLEID,
TABLENUMBER,
TABLEMEMBERS,
AVIABLE,
STATE 
from restaurantTable 
WHERE STATE = 1 AND AVIABLE = 1 AND TABLEMEMBERS >= v_Miembros;
END;
/
--Procedure Agregar Cliente
create or replace procedure SP_AGREGAR_CLIENTE(v_NAME varchar2,v_MEMBERS varchar2,v_STATE varchar2,v_RT_TABLEID varchar2, v_salida out number)
IS

BEGIN
        insert into CLIENT (NAME,MEMBERS,STATE,RT_TABLEID) 
        values (v_NAME,v_MEMBERS,v_STATE,v_RT_TABLEID);
        commit;
        
        UPDATE restauranttable
        SET AVIABLE=0
        WHERE tableid = v_RT_TABLEID;
        v_salida:= 1;
        EXCEPTION
            WHEN OTHERS THEN
            
        UPDATE restauranttable
        SET AVIABLE=1
        WHERE tableid = v_RT_TABLEID;
        v_salida:= -1;  

END;
/
--Store Procedures Orden Cliente

create or replace procedure sp_Agregar_OrdenCliente(idMesero varchar2,idCliente varchar2,totalCarritoCliente varchar2,v_state varchar2,v_id out number, v_salida out number) 
IS
BEGIN
        insert into orderclient (ORDERHOUR,ORDERDATE,ORDERCLIENTTOTAL,STATE,CLIENT_CLIENTID,WAITER_WAITERID)
        values (sysdate,sysdate,totalCarritoCliente,v_state,idCliente,idMesero) returning ORDECLIENTID into v_id;
        commit;
        v_salida:= 1;
        EXCEPTION
        WHEN OTHERS THEN
        v_salida:= -1;
END;

/
--Mostrar Meseros Cliente

create or replace  procedure sp_listar_MeserosClienteIonic(v_idcliente number,listadoMeseros out SYS_REFCURSOR)
IS
BEGIN
open listadoMeseros for
select DISTINCT
w.WAITERID WAITERID,
cl.CLIENTID CLIENTID,
cl.NAME NAMECLIENT,
w.NAME1 NAMEWAITER,
w.LASTNAME1 LASTNAMEWAITER,
cl.STATE ESTADO_CLIENTE,
oc.STATE ESTADO_ORDENCLIENTE,
w.STATE ESTADO_MESERO
from orderClient oc inner join client cl on (cl.clientid = oc.client_clientid) inner join waiter w on (oc.waiter_waiterid = w.waiterid) 
where cl.CLIENTID = v_idcliente and cl.STATE = 1 and w.STATE = 1;
END;
/
--Mostrar Ordenes Cliente
create or replace  procedure sp_listar_OrdenesClientesIonic(v_idcliente number,listadoOrdenesCliente out SYS_REFCURSOR)
IS
BEGIN
open listadoOrdenesCliente for
select
oc.ordeclientid,
oc.CLIENT_CLIENTID CLIENT_CLIENTID,
oc.WAITER_WAITERID WAITER_WAITERID,
m.MENUID MENUID,
ocd.QUIANTITY QUIANTITY,
ocd.TOTAL TOTAL,
oc.ORDERCLIENTTOTAL ORDERCLIENTTOTAL,
m.NAME NAME,
oc.STATE STATEORDERCLIENT,
m.STATE STATEORDERSTATE
from orderClientDetails ocd 
inner join orderClient oc on (oc.ordeclientid = ocd.ocdorderclientid) 
inner join menu m on (m.menuid = ocd.ocdmenuid)WHERE m.STATE = 1 AND OC.CLIENT_CLIENTID=v_idcliente order by oc.ordeclientid asc;
END;
/
--Store Procedures Reportes

--Menus que se vendieron por dia
create or replace  procedure sp_Menus_vendidos_Dia(reporte out SYS_REFCURSOR)
IS
BEGIN
open reporte for 
SELECT  A.MENUID, A.NAME as NOMBRE, sum (b.quiantity) AS CANTIDAD_PEDIDO, to_char(C.ORDERDATE,'DD-MM-YYYY') as FECHA    
FROM MENU A inner JOIN ORDERCLIENTDETAILS B ON A.MENUID = B.OCDMENUID inner JOIN ORDERCLIENT C ON c.ordeclientid = b.ocdorderclientid  
GROUP BY  A.MENUID, A.NAME, to_char(C.ORDERDATE,'DD-MM-YYYY') order by to_char(C.ORDERDATE,'DD-MM-YYYY');
END;
/
--Producto que se ordenaron por dia
create or replace  procedure sp_Productos_ordenados_Dia(reporte out SYS_REFCURSOR)
IS
BEGIN
open reporte for 
SELECT P.PRODUCTID, PRO.COMPANYNAME AS PROVEEDOR, P.PRODUCTNAME AS PRODUCTO,sum (OPD.quantity) AS CANTIDAD_PEDIDO, to_char(OP.ORDERDATE,'DD-MM-YYYY') AS FECHA 
FROM ORDERpRODUCT OP 
INNER JOIN ORDERPRODUCTDETAILS OPD ON (OP.ORDERPRODUCTID = OPD.OPDORDERPRODUCTID) 
INNER JOIN PRODUCT P ON (P.PRODUCTID = OPD.OPDPRODUCTID) 
INNER JOIN PROVIDER PRO ON (PRO.IDPROVIDER=P.P_IDPROVIDER)
GROUP BY  
P.PRODUCTID, P.PRODUCTNAME, PRO.COMPANYNAME , to_char(OP.ORDERDATE,'DD-MM-YYYY') 
ORDER BY to_char(OP.ORDERDATE,'DD-MM-YYYY');
END;
/
--Ganancias Menu por dia
create or replace  procedure sp_Ganancia_Menu_Dia(reporte out SYS_REFCURSOR)
IS
BEGIN
open reporte for
SELECT A.MENUID, A.NAME, to_char(sum((A.MENUPRICE-A.MENUCOST)*b.quiantity),'$999g999g999') as Ganancia,sum(b.quiantity) as Cantidad, to_char(C.ORDERDATE,'DD-MM-YYYY') as fecha
FROM MENU A 
INNER JOIN ORDERCLIENTDETAILS B ON A.MENUID = b.ocdmenuid 
INNER JOIN ORDERCLIENT C ON b.ocdorderclientid = c.ordeclientid
group by to_char(C.ORDERDATE,'DD-MM-YYYY'), A.MENUID, A.NAME
order by to_char(C.ORDERDATE,'DD-MM-YYYY');
END;
/
--Boletas
create or replace  procedure sp_Boletas(reporte out SYS_REFCURSOR)
IS
BEGIN
open reporte for
SELECT A.ORDECLIENTID AS N_BOLETA, 
b.name1||' '||b.lastname1 Mesero, 
c.name as Cliente,  
TO_CHAR(a.orderclienttotal,'$999g999g999') AS MONTO, 
to_char(a.orderdate,'DD-MM-YYYY') AS FECHA 
FROM ORDERCLIENT A 
INNER JOIN WAITER B ON  a.waiter_waiterid = b.waiterid 
INNER JOIN CLIENT C ON a.CLIENT_CLIENTID = C.CLIENTID
;
END;

--Pagar orden producto
create or replace procedure sp_pagarOdenProducto(id_cliente varchar2,id_mesa varchar2, v_salida out number)
IS

BEGIN

UPDATE client
set state= 0 
WHERE CLIENTID = id_cliente;

UPDATE orderClient
set state= 0 
WHERE  CLIENT_CLIENTID = id_cliente;

UPDATE restaurantTable
set aviable = 1
WHERE tableid = id_mesa;
commit;
    v_salida:= 1;
EXCEPTION
     
    WHEN OTHERS THEN
    
    ROLLBACK;
    v_salida:= -1;      
end;






















