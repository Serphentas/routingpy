# -*- coding: utf-8 -*-
# Copyright (C) 2019 GIS OPS UG
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

"""
Core client functionality, common across all API requests.
"""
from .base import Router
from routingpy import convert

class Graphhopper(Router):
    """Performs requests to the Graphhopper API services."""

    _DEFAULT_BASE_URL = "https://graphhopper.com/api"
    _DEFAULT_API_VERSION = "1"
    def __init__(self, key=None, base_url=_DEFAULT_BASE_URL, version=_DEFAULT_API_VERSION, user_agent=None, timeout=None,
                 retry_timeout=None, requests_kwargs={}, retry_over_query_limit=False):

        """
        Initializes an graphhopper client.

        :param key: GH API key. Required if https://graphhopper.com/api is used.
        :type key: str

        :param base_url: The base URL for the request. Defaults to the GH API
            server. Should not have a trailing slash.
        :type base_url: str

        :param timeout: Combined connect and read timeout for HTTP requests, in
            seconds. Specify "None" for no timeout.
        :type timeout: int

        :param retry_timeout: Timeout across multiple retriable requests, in
            seconds.
        :type retry_timeout: int

        :param requests_kwargs: Extra keyword arguments for the requests
            library, which among other things allow for proxy auth to be
            implemented. See the official requests docs for more info:
            http://docs.python-requests.org/en/latest/api/#main-interface
        :type requests_kwargs: dict

        :param queries_per_minute: Number of queries per second permitted.
            If the rate limit is reached, the client will sleep for the
            appropriate amount of time before it runs the current query.
            Note, it won't help to initiate another client. This saves you the
            trouble of raised exceptions.
        :type queries_per_minute: int
        """

        if base_url == self._DEFAULT_BASE_URL and key is None:
            raise KeyError("API key must be specified.")
     
        super(Graphhopper, self).__init__(base_url, key, user_agent, timeout, retry_timeout, requests_kwargs, retry_over_query_limit)

    def directions(self, coordinates, profile, type=None, optimize=None, instructions=None, locale=None,
                   elevation=None, points_encoded=None, calc_points=None, debug=None,
                   gpx_track=None, gpx_route=None, gpx_waypoints=None, point_hint=None, details=None, ch_disable = None, 
                   weighting=None, heading=None, heading_penalty=None, 
                   pass_through=None, block_area=None, avoid=None, algorithm=None, round_trip_distance=None, round_trip_seed = None,
                   alternative_route_max_paths = None, alternative_route_max_weight_factor = None, 
                   alternative_route_max_share_factor = None, dry_run=None):
        """Get directions between an origin point and a destination point.

        For more information, visit https://openrouteservice.org/documentation/.

        :param coordinates: The coordinates tuple the route should be calculated
            from in order of visit.
        :type coordinates: list, tuple

        :param profile: The vehicle for which the route should be calculated. 
            Default "car".
            Other vehicle profiles are listed here: 
            https://graphhopper.com/api/1/docs/supported-vehicle-profiles/
        :type profile: str

        :param type: Specifies the resulting format of the route, for json the content type will be application/json. 
            Or use gpx, the content type will be application/gpx+xml. Default "json".
        :type format: str

        :param language: Language for routing instructions. The locale of the resulting turn instructions. 
            E.g. pt_PT for Portuguese or de for German. Default "en".
        :type language: str

        :param optimize: If false the order of the locations will be identical to the order of the point parameters. 
            If you have more than 2 points you can set this optimize parameter to true and the points will be sorted 
            regarding the minimum overall time - e.g. suiteable for sightseeing tours or salesman. 
            Keep in mind that the location limit of the Route Optimization API applies and the credit costs are higher! 
            Note to all customers with a self-hosted license: this parameter is only available if your package includes 
            the Route Optimization API. Default False.
        :type geometry: bool

        :param instructions: Specifies whether to return turn-by-turn instructions.
            Default True.
        :type instructions: bool

        :param elevation: If true a third dimension - the elevation - is included in the polyline or in the GeoJson. 
            IMPORTANT: If enabled you have to use a modified version of the decoding method or set points_encoded to false. 
            See the points_encoded attribute for more details. Additionally a request can fail if the vehicle does not 
            support elevation. See the features object for every vehicle.
            Default False.
        :type elevation: bool

        :param points_encoded: If false the coordinates in point and snapped_waypoints are returned as array using the order 
            [lon,lat,elevation] for every point. If true the coordinates will be encoded as string leading to less bandwith usage. 
            Default True
        :type elevation: bool

        :param calc_points: If the points for the route should be calculated at all printing out only distance and time.
            Default True
        :type elevation: bool

        :param debug: If true, the output will be formated.
            Default False
        :type elevation: bool
        
        :param point_hint: Optional parameter. Specifies a hint for each point parameter to prefer a certain street for the 
            closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control 
            for which street the closest location is looked up.
        :type point_hint: bool

        :param details: Optional parameter. Optional parameter to retrieve path details. You can request additional details for the 
            route: street_name and time. For all motor vehicles we additionally support max_speed, toll (no, all, hgv), 
            road_class (motorway, primary, ...), road_environment, and surface. The returned format for one details 
            is [fromRef, toRef, value]. The ref references the points of the response. Multiple details are possible 
            via multiple key value pairs details=time&details=toll
        :type details: bool            

        :param ch_disable: Always use ch_disable=true in combination with one or more parameters of this table. 
            Default False.
        :type ch_disable: bool

        :param weighting: Which kind of 'best' route calculation you need. Other options are shortest 
            (e.g. for vehicle=foot or bike) and short_fastest if not only time but also distance is expensive.
            Default "fastest".
        :type weighting: str           
        
        :param heading: Optional parameter. Favour a heading direction for a certain point. Specify either one heading for the start point or as
            many as there are points. In this case headings are associated by their order to the specific points. 
            Headings are given as north based clockwise angle between 0 and 360 degree. 
        :type heading: list of int   

        :param heading_penalty: Optional parameter. Penalty for omitting a specified heading. The penalty corresponds to the accepted time 
            delay in seconds in comparison to the route without a heading.
            Default 120.
        :type heading_penalty: int

        :param pass_through: Optional parameter. If true u-turns are avoided at via-points with regard to the heading_penalty.
            Default False.
        :type pass_through: bool

        :param block_area: Optional parameter. Block road access via a point with the format 
            latitude,longitude or an area defined by a circle lat,lon,radius or a rectangle lat1,lon1,lat2,lon2.
        :type block_area: str

        :param avoid: Optional semicolon separated parameter. Specify which road classes you would like to avoid 
            (currently only supported for motor vehicles like car). Possible values are ferry, motorway, toll, tunnel and ford.
        :type avoid: str
        
        :algorithm: Optional parameter. round_trip or alternative_route.
        :type algorithm: str 

        :round_trip_distance: If algorithm=round_trip this parameter configures approximative length of the resulting round trip.
            Default 10000.
        :type round_trip_distance: int

        :round_trip_seed: If algorithm=round_trip this parameter introduces randomness if e.g. the first try wasn't good.
            Default 0.
        :type round_trip_seed: int

        :round_trip_seed: If algorithm=round_trip this parameter introduces randomness if e.g. the first try wasn't good.
            Default 0.
        :type round_trip_seed: int

        :alternative_route_max_paths: If algorithm=alternative_route this parameter sets the number of maximum paths 
            which should be calculated. Increasing can lead to worse alternatives.
            Default 2.
        :type alternative_route_max_paths: int

        :alternative_route_max_weight_factor: If algorithm=alternative_route this parameter sets the factor by which the alternatives 
            routes can be longer than the optimal route. Increasing can lead to worse alternatives.
            Default 1.4.
        :type alternative_route_max_weight_factor: int

        :alternative_route_max_share_factor: If algorithm=alternative_route this parameter specifies how much alternatives 
            routes can have maximum in common with the optimal route. Increasing can lead to worse alternatives.
            Default 0.6.
        :type alternative_route_max_share_factor: int
       
        :param dry_run: Print URL and parameters without sending the request.
        :param dry_run: bool

        :returns: raw JSON response
        :rtype: dict
        """

        params = {"point": coordinates,
                  "profile": profile}

        if type:
            params['type'] = type

        if self._authorization_key is not None:
            params["key"] = self._authorization_key

        if optimize is not None:
            params["optimize"] = optimize

        if instructions is not None:
            params["instructions"] = instructions

        if locale is not None:
            params["locale"] = locale

        if elevation is not None:
            params["elevation"] = elevation

        if points_encoded is not None:
            params["points_encoded"] = points_encoded

        if calc_points is not None:
            params["calc_points"] = calc_points

        if debug is not None:
            params["debug"] = debug

        if point_hint is not None:
            params["point_hint"] = point_hint

        if details is not None:
            params["details"] = details

        # if gpx_track is not None:
        #     params["gpx.track"] = gpx_track

        # if gpx_route is not None:
        #     params["gpx.route"] = gpx_route

        # if gpx_waypoints is not None:
        #     params["gpx.waypoints"] = gpx_waypoints

        ### all below params will only work if ch is disabled
        if ch_disable is not None:
            params["ch.disable"] = ch_disable

        if weighting is not None:
            params["weighting"] = weighting

        if heading is not None:
            params["heading"] = heading

        if heading_penalty is not None:
            params["heading_penalty"] = heading_penalty

        if pass_through is not None:
            params["pass_through"] = pass_through

        if block_area is not None:
            params["block_area"] = block_area

        if avoid is not None:
            params["avoid"] = avoid

        if algorithm is not None:

            if algorithm == 'round_trip':

                if round_trip_distance is not None:
                    params["round_trip.distance"] = round_trip_distance

                if round_trip_seed is not None:
                    params["round_trip.seed"] = round_trip_seed

            if algorithm == 'alternative_route':

                if alternative_route_max_paths is not None:
                    params["alternative_route.max_paths"] = alternative_route_max_paths

                if alternative_route_max_weight_factor is not None:
                    params["alternative_route.max_weight_factor"] = alternative_route_max_weight_factor

                if alternative_route_max_weight_factor is not None:
                    params["alternative_route.max_weight_factor"] = alternative_route_max_weight_factor

        return self._request("/" + self._DEFAULT_API_VERSION + '/route', get_params=self.gh_get_params(params), dry_run=dry_run)

    def isochrones(self, coordinates, profile, distance_limit=None, time_limit=None, 
                    buckets=None, reverse_flow=None, debug=None, dry_run=None):
        """Gets isochrones or equidistants for a range of time/distance values around a given set of coordinates.

        :param coordinates: One coordinate pair denoting the location.
        :type coordinates: tuple

        :param profile: Specifies the mode of transport. 
            One of bike, car, foot or 
            https://graphhopper.com/api/1/docs/supported-vehicle-profiles/Default.
            Default "car".
        :type profile: str

        :param distance_limit: Specify which time the vehicle should travel. In seconds.
            Default 600.
        :type distance_limit: int

        :param time_limit: Instead of time_limit you can also specify the distance 
            the vehicle should travel. In meter.
        :type time_limit: int

        :param buckets: For how many sub intervals an additional polygon should be calculated.
            Default 1.
        :type buckets: int
    
        :param reverse_flow: If false the flow goes from point to the polygon,
            if true the flow goes from the polygon "inside" to the point. 
            Default False.
        :param reverse_flow: bool
        
        :param debug: If true, the output will be formatted.
            Default False
        :type debug: bool
    
        :param dry_run: Print URL and parameters without sending the request.
        :param dry_run: bool

        :returns: raw JSON response
        :rtype: dict
        """

        # params = {
        #     "point": coordinates,
        #     "profile": profile
        # }
        #
        # if self._authorization_key is not None:
        #     params["key"] = self._authorization_key
        #
        # if distance_limit is not None:
        #     params['distance_limit'] = distance_limit
        #
        # if time_limit is not None:
        #     params['time_limit'] = time_limit
        #
        # if buckets is not None:
        #     params['buckets'] = buckets
        #
        # if reverse_flow is not None:
        #     params['reverse_flow'] = reverse_flow
        #
        # if debug is not None:
        #     params['debug'] = debug
        #
        # if dry_run is not None:
        #     params['dry_run'] = dry_run

        params = [
            ['point', coordinates],
            ['profile', profile]
        ]

        if self._authorization_key is not None:
            params.append(["key", self._authorization_key])

        if distance_limit is not None:
            params.append(['distance_limit', distance_limit])

        if time_limit is not None:
            params.append(['time_limit', time_limit])

        if buckets is not None:
            params.append(['buckets', buckets])

        if reverse_flow is not None:
            params.append(['reverse_flow', reverse_flow])

        if debug is not None:
            params.append(['debug', debug])

        if dry_run is not None:
            params.append(['dry_run', dry_run])

        return self._request("/" + self._DEFAULT_API_VERSION + '/isochrone', get_params=params, dry_run=dry_run)

    def distance_matrix(self, profile, coordinates=None, from_coordinates=None, to_coordinates=None, out_array=None, debug=None, dry_run=None):
        """ Gets travel distance and time for a matrix of origins and destinations.

        :param coordinates: Specifiy multiple points for which the weight-, route-, time- or distance-matrix should be calculated. 
            In this case the starts are identical to the destinations. 
            If there are N points, then NxN entries will be calculated. 
            The order of the point parameter is important. Specify at least three points. 
            Cannot be used together with from_point or to_point. Is a string with the format latitude,longitude.
        :type coordinates: list, tuple

        :param profile: Specifies the mode of transport. 
            One of bike, car, foot or
            https://graphhopper.com/api/1/docs/supported-vehicle-profiles/Default.
            Default "car".
        :type profile: str

        :param from_coordinates: The starting points for the routes. 
            E.g. if you want to calculate the three routes A->1, A->2, A->3 then you have one 
            from_point parameter and three to_point parameters. Is a string with the format latitude,longitude.
        :type from_coordinates: list, tuple

        :param to_coordinates: The destination points for the routes. Is a string with the format latitude,longitude.
        :type to_coordinates: list, tuple

        :param out_array: Specifies which arrays should be included in the response. Specify one or more of the following 
            options 'weights', 'times', 'distances'. To specify more than one array use e.g. out_array=times&out_array=distances. 
            The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ 
            for different vehicles or versions of this API.
            Default "weights".
        :type out_array: list           
    
        :param dry_run: Print URL and parameters without sending the request.
        :param dry_run: bool

        :returns: raw JSON response
        :rtype: dict
        """

        params = {
            "point": coordinates,
            "profile": profile
        }

        if self._authorization_key is not None:
            params["key"] = self._authorization_key

        if coordinates is not None:
            params['point'] = coordinates

        else:
            if from_coordinates is not None:
                params['from_point'] = from_coordinates
            if to_coordinates is not None:
                params['to_point'] = to_coordinates

        if debug is not None:
            params['debug'] = debug

        if out_array is not None:
            params['out_array'] = out_array
    
        return self._request("/" + self._DEFAULT_API_VERSION + '/matrix', get_params=self.gh_get_params(params), dry_run=dry_run)

    def optimization(self):
        pass

    def map_matching(self):
        pass

    # @staticmethod
    # def gh_get_params(params):
    #     """ Graphhopper uses duplicate get parameters which are generated here.
    #
    #     :param params: GET params previously added.
    #     :param params: dict
    #
    #     :returns: list of GET params
    #     :rtype: list
    #      """
    #
    #     dup_dict = {}
    #     for dup_key in ('point', 'to_point', 'from_point', 'out_array'):
    #         if dup_key in params:
    #             dup_dict[dup_key] = params.pop(dup_key)
    #
    #     params = sorted(dict(**params).items())
    #
    #     for k, v in dup_dict.items():
    #
    #         for e in v:
    #
    #             # if coordinate
    #             if isinstance(e, (list,)):
    #                 e.reverse()
    #                 params.append([k, ",".join(str(coord) for coord in e)])
    #             else:
    #                 params.append([k, e])
    #
    #     return params

