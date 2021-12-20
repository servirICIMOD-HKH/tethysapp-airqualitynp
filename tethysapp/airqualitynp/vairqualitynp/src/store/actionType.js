// import {TethysAppName} from "../config";


let BaseUrl = null;

if (process.env.NODE_ENV === "production") {
    // BaseUrl = "http://localhost:8000";

    BaseUrl = 'http://smog.icimod.org';

} else {

    BaseUrl = "http://localhost:8000";
}

export let Action = {
    Base: BaseUrl,
    // Base : 'http://110.44.114.244:8001/',
    CityData: "apps/airqualitynp/getCityData",


    Aeronet: 'apps/airqualitynp/aeronetaodpm',
    USEmbassyAOD: 'apps/airqualitynp/usembassypm',
    getGeoJSONofStations: 'apps/airqualitynp/getGeoJSONofStations',
    getGeoJsonForOneSatation: 'apps/airqualitynp/getGeoJsonForOneSatation',
    getAllStationsID: 'apps/airqualitynp/getAllStationsID',


    commonAPI: 'apps/airqualitynp/getData/',
    RegionGeojson: 'apps/airqualitynp/geojsonregion',
    AOIPolygon: 'apps/airqualitynp/aoipolygon',
    GetMapImage: 'apps/airqualitynp/getmapimage/',
    GetImage: 'apps/airqualitynp/downloadImage',
    SlicedFromCatalog: 'apps/airqualitynp/slicedfromcatalog/',
    TimeSeriesRasterQuery: 'apps/airqualitynp/timeseriesmodeldata/',


};