# Data Notes

## Health Facilities Location (The GRID3 NGA - Health Facilities v2.0)
- Source: https://data.grid3.org/datasets/a0ed9627a8b240ff8b315a84575754a4_0/explore?location=9.926774%2C11.494199%2C10
- Downloaded: 13-09-2026
- 107 Features, Points 
- Columns: `unique_id (Text), latitude (Decimal Number), longitude (Decimal Number), country (Text), iso (Text), state_stan (Text), lga_standa (Text), ward_stand (Text), ward_bdry (Text), ward_in_gr (Text), facility_n (Text), alt_name (Text), settlement (Text), facility_l (Text), facility_t (Text), facility_o (Text), facility_1 (Text), functional (Text), date_creat (Date), sett_ext_t (Text), mgrs_code (Text), input_data (Text), input_da_1 (Text), nhfr_facil (Text), gps_accura (Decimal Number), sett_ext_d (Decimal Number), dist_ward_ (Decimal Number), flag1 (Integer), flag2 (Integer), flag3 (Integer), flag4 (Integer), flag5 (Integer), flag6 (Integer), issues (Text), flag_count (Integer)`
- Yes: `alt_name — 58 nulls,   settlement — 107 nulls (all records are null), facility_l — 30 nulls, facility_t — 31 nulls, facility_o — 30 nulls, facility_1 — 36 nulls, functional — 30 nulls, date_creat — 55 nulls, sett_ext_t — 8 nulls, mgrs_code — 8 nulls, nhfr_facil — 101 nulls, issues — 66 nulls`
- Point
- Covers my LGA fully 

## Road and Path Network (Extracted Via QuickOSM)
- Query: highway=* Within Kaltungo LGA Extent 
- Extracted: 13-09-2026
- 1161 Features, Lines
- Columns: `full_id (Text), osm_id (Text), osm_type (Text), motor_vehi (Text), horse (Text), foot (Text), bicycle (Text), access (Text), intermitte (Text), ford (Text), source_url (Text), source_dat (Text), boundary (Text), admin_leve (Text), voltage (Text), power (Text), frequency (Text), cables (Text), is_in_coun (Text), waterway (Text), GNS_id (Text), GNS_dsg_st (Text), GNS_dsg_co (Text), name (Text), junction (Text), layer (Text), bridge (Text), surface (Text), ref (Text), oneway (Text), lanes (Text), highway (Text)`
- Yes: `motor_vehi — 1160 nulls, horse — 1160 nulls, foot — 1160 nulls, bicycle — 1160 nulls, access — 1161 nulls (all records are null), intermitte — 1158 nulls, ford — 1151 nulls, source_url — 1161 nulls (all records are null), source_dat — 1155 nulls, boundary — 1155 nulls, admin_leve — 1155 nulls, voltage — 1161 nulls (all records are null), power — 1161 nulls (all records are null), frequency — 1161 nulls (all records are null), cables — 1161 nulls (all records are null), is_in_coun — 1161 nulls (all records are null), waterway — 1153 nulls, GNS_id — 1161 nulls (all records are null), GNS_dsg_st — 1161 nulls (all records are null), GNS_dsg_co — 1161 nulls (all records are null), name — 1161 nulls (all records are null), junction — 1160 nulls, layer — 1149 nulls, bridge — 1149 nulls, surface — 1057 nulls, ref — 1148 nulls, oneway — 1150 nulls, lanes — 1155 nulls, highway — 14 nulls`
- Line
- Covers my LGA Fully

## Population Distribution Data
- Source: https://hub.worldpop.org/geodata/summary?id=74736
- Downloaded: 13-09-2026
- File Type: GeoTiff
- Covers my Full LGA

## Ward Boundaries 
- Source: https://data.grid3.org/datasets/0824aded5f5a4d39b10871c667aa8ccf_0/explore?filters=eyJsZ2FuYW1lIjpbIkthbHR1bmdvIl19&location=9.831131%2C11.496417%2C10
- Downloaded: 13-09-2026
- 10 Features, Polygon
- Columns: `globalid (Text), uniq_id (Text), timestamp (Text), editor (Text), wardname (Text), wardcode (Text), lganame (Text), lgacode (Text), statename (Text), statecode (Text), amapcode (Text), status (Text), source (Text), urban (Text)`
- No: No, null values
- Polygon
- Covers LGA Fully

## LGA Boundary
-Source: https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=8.415591%2C10.827624%2C7
- Downloaded: 13-09-2026
- 1 Feature, Polygon
- Columns: `wkt_geom (Text), globalid (Text), uniq_id (Text), timestamp (Text), editor (Text), lganame (Text), lgacode (Text), statename (Text), statecode (Text), source (Text), amapcode (Text)`
- No: No Null fields
- Polygon
- Covers my LGA Fully