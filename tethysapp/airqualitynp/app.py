from tethys_sdk.base import TethysAppBase, url_map_maker


class Airqualitynp(TethysAppBase):
    """
    Tethys app class for Airqualitynp.
    """

    name = 'Air Quality - Nepal'
    index = 'airqualitynp:home'
    icon = 'airqualitynp/images/icon.gif'
    package = 'airqualitynp'
    root_url = 'airqualitynp'
    color = '#f39c12'
    description = 'Air Quality Watch'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """

        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='airqualitynp',
                controller='airqualitynp.controllers.home.home'
            ),
            UrlMap(
                name='aeronetData',
                url='airqualitynp/getGeoJSONofStations',
                controller='airqualitynp.controllers.viewer.getGeoJSONofStations',
            ),
            UrlMap(
                name='getGeoJsonForOneSatation',
                url='airqualitynp/getGeoJsonForOneSatation',
                controller='airqualitynp.controllers.viewer.getGeoJsonForOneSatation',
            ),
            UrlMap(
                name='getData',
                url='airqualitynp/getData',
                controller='airqualitynp.controllers.viewer.GetData',
            ),
            UrlMap(name='WMSProxy',
                   url='airqualitynp/WMSProxy/(?P<url>.*)',
                   # url='airqualitynp/WMSProxy/',
                   # url=r'airqualitynp/WMSProxy/(?P<variable_name>.*)$',
                   # regex=r'^[ A-Za-z0-9_@./#&+-]*$',
                   controller='airqualitynp.controllers.viewer.WMSProxy',
                   # regex='variable_name'
                   ),
            UrlMap(
                name='GeojsonRegion',
                url='airqualitynp/geojsonregion',
                controller='airqualitynp.controllers.viewer.GeojsonRegion',
            ),
            UrlMap(
                name='AOIPolygon',
                url='airqualitynp/aoipolygon',
                controller='airqualitynp.controllers.viewer.AOIPolygon',
            ),
            UrlMap(
                name='GetMapPNG',
                url='airqualitynp/getmapimage',
                controller='airqualitynp.controllers.viewer.GetMapIMAGE',
            ),  UrlMap(
                name='create_GIF_Map_IMAGE',
                url='airqualitynp/creategifmapimage',
                controller='airqualitynp.controllers.viewer.Create_GIF_Map_IMAGE',
            ), UrlMap(
                name='timeseriesmodeldata',
                url='airqualitynp/timeseriesmodeldata',
                controller='airqualitynp.controllers.viewer.TimeSeriesModelSata',
            ), UrlMap(
                name='downloadImage',
                url='airqualitynp/downloadImage',
                controller='airqualitynp.controllers.viewer.downloadImage',
            ), UrlMap(
                name='slicedfromcatalog',
                url='airqualitynp/slicedfromcatalog',
                controller='airqualitynp.controllers.viewer.SlicedFromCatalog',
            ), UrlMap(
                name='slicedfromcatalog',
                url='airqualitynp/getCityData',
                controller='airqualitynp.controllers.rest.getCityData',
            ),
        )

        return url_maps

