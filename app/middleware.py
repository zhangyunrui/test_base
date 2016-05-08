# -*- coding: utf-8 -*-
import re
import logging
import datetime
from django.conf import settings
from django.http.response import HttpResponse
import sys

logger = logging.getLogger('error_trace_back')


# class LoggerMiddleware(object):
#     """记录所有异常,并抛出友好错误页面"""
#
#     def process_response(self, request, response):
#         """
#         在response过程截取错误信息
#         :param request:
#         :param response:
#         :return:
#         """
#         now = datetime.datetime.now()
#         pattern_type = re.compile("<tr>\s*<th>Exception Type:</th>\s*<td>(?P<exception_type>.*?)</td>")
#         exception_type = pattern_type.search(str(response)).group('exception_type')
#         pattern_value = re.compile("<tr>\s*<th>Exception Value:</th>\s*<td><pre>(?P<exception_value>.*?)</pre></td>")
#         exception_value = pattern_value.search(str(response)).group('exception_value')
#         pattern_location = re.compile("<tr>\s*<th>Exception Location:</th>\s*<td>(?P<exception_location>.*?)</td>")
#         exception_location = pattern_location.search(str(response)).group('exception_location')
#
#         pattern_user = re.compile(
#             '<li class="frame user">.*?<code>(?P<file>.*?)</code>.*?<code>(?P<def>.*?)</code>.*?<ol.*?class="context-line".*?<pre>\s*(?P<line>.*?)</pre>',
#             re.DOTALL)
#         exception_users = pattern_user.findall(str(response))
#
#         exception_user_list = ""
#
#         for exception_user in exception_users:
#             exception_user_dict = """
#     file:  %s
#     define:%s
#     line:  %s
#             """ % (exception_user[0], exception_user[1], exception_user[2])
#             exception_user_list += exception_user_dict
#
#         exception = """
# begin-------------------------------------------------------------------------------------------------------------------
#
# time:               %s
# path:               %s
# exception_type:     %s
# exception_value:    %s
# exception_location: %s
# exception_user:
#     %s
# end---------------------------------------------------------------------------------------------------------------------
#             """ % (now, request.path, exception_type, exception_value, exception_location, exception_user_list)
#         logger.error(exception)
#         return HttpResponse(u'页面出错啦, <a href=' + str(settings.SITE_URL) + u'>返回首页</a>')


class LoggerMiddleware(object):
    """记录所有异常,并抛出友好错误页面"""

    def process_exception(self, request, exception):
        """
        在response过程截取错误信息
        :param request:
        :param exception:
        :return:
        """
        try:
            now = datetime.datetime.now()
            exception_header = """
--------------------------------------%s--------------------------------------------------------
""" % now
            exception_msg = 'Internal Server Error: %s'
            exception = exception_header + exception_msg

            logger.error(exception, request.path,
                exc_info=sys.exc_info(),
                extra={
                    'status_code': 500,
                    'request': request
                }
            )
        except Exception:
            exception_e = """
--------------------------------------LoggerMiddleware error------------------------------------------------------------
            """
            logger.error(exception_e)

        return HttpResponse(u'页面出错啦, <a href=' + str(settings.SITE_URL) + u'>返回首页</a>')
