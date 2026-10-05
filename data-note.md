# Data Notes
**Week 2 Deliverables Author: Joshua Victor**
>This note describes the datasets used for the proposed GIS analysis. The layers are stored together in the GeoPackage committed to this repository. 

|S/N|Dataset|Source Link |Geometry Type |No. of Features |Key Columns |Comment |Date Processed|
|---|---|---|---|---|---|---|---|
|1|Health Facilities Location|[GRID3](https://data.grid3.org/datasets/a0ed9627a8b240ff8b315a84575754a4_0/explore?location=9.926774%2C11.494199%2C10)|Point|107|`unique_id, facility_n, latitude, longitude, state_stan, lga_standa, ward_stand, settlement, facility_t, functional`|30 of the health facilities have `Null` Owernership|13-09-2026|
|2|Road and Path Network | QuickOSM `Query: highway=* Within Kaltungo LGA Extent` | Line| 1161 | `full_id, name, highway, surface, lanes, oneway, motor_vehi, foot, bicycle, access, bridge, ford` | Made use of QuickOSM instead of initial GRID3 Source to extract the data as Instructed by the Tutor. Roads Align with Satellite Image reference, but many have no surface tag. | 13-09-2026 |
|3| Population Distribution Data|[WorldPop](https://hub.worldpop.org/geodata/summary?id=74736)|Raster|-|-| Covers my Full Study Area | 13-09-2026|
|4| Ward Boundaries | [GRID3](https://data.grid3.org/datasets/0824aded5f5a4d39b10871c667aa8ccf_0/explore?filters=eyJsZ2FuYW1lIjpbIkthbHR1bmdvIl19&location=9.831131%2C11.496417%2C10)| Polygon | 10 | `uniq_id, wardname, wardcode, lganame, lgacode, statename, statecode, urban`| The Data covers the study area, no `Null` values | 13-09-2026 |
|5|LGA Boundary|[GRID3](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=8.415591%2C10.827624%2C7)|Polygon|1|`uniq_id, lganame, lgacode, statename, statecode, wkt_geom`|Covers my Study Area fully|13-09-2026|

**Status:** Complete.
>Check [Week 3](data-preparation.md) Reprojection and quality checks
