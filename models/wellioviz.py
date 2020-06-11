from bokeh.core.properties import Dict, String, Any, Instance
from bokeh.models import LayoutDOM, ColumnDataSource


class WellIoVizPlot(LayoutDOM):
    __javascript__ = [None]
    __js_skip__ = {'none': None}
    __js_require__ = {'none': None}
    data = Dict(String, Any)
    data_sources = Dict(String, Instance(ColumnDataSource))