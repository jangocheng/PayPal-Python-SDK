# This class was generated on Sat, 27 Jan 2018 14:34:13 CST by version 0.1.0-dev+30efd2 of Braintree SDK Generator
# plan_create_request.py
# @version 0.1.0-dev+30efd2
# @type request
# @data H4sIAAAAAAAC/+xdX2/bOBJ/v08x0B5wW8Cx03b/5i2XpKj32iSXuItb9AqblkYWtxSpJakkxqLf/TCkJEuWvE16qZEHPrUeUdQMZ/ibP+Qgf0bnLMfoKCoEk+NYI7MYjaJTNLHmheVKRkfRiSMbYLDkQnC5AjcaphJshvDL9cU5aPyjRGNhqZL1CLiMRZmge0xjIUHLuDBjOPa/89LYZhSzIJAZC0oiaFyVgmko2DpHaSHBlEtOnACTyQiU44oJsR4BA6s5EwNjx3DG4mxoElNgzFPeFQc1V8kIbjMeZ8Qr6pxLNJCpW1CpRfdtSJV2FKHkyokWl8aqHDVwA3HG9AqTRsKY1d9aA4OU32ECSgOXjhMEWeZL1KDShsl4HQv0S9Rnm6bbiN7MbDJeFCRCiuh4tOwOWK5Kac0YZhnSHKwUFoxlFulzDCTeeh65gcXJ1dnx7Ox0MYZ/Yqo0wlqV7mveGIBJYCuN6BhKtcqBuZdHbqDTI4stv6GxjbqXayiLhFnijFsDC/f1BVgFi+OT2fTXs8U4GkX/LlGvL5lmOS25iY7efxhFr5ElqLepr5TOt2mXzGbbtCtvh7N1gdHRn5H/N7oUTEaj6FemOVsKbNl8NIr+hesuoWv9x1tW/1u1Pktm0Fms0pDTwjXLZMAZq18XvyIk7bHWbO0ZOiRGWXIhxTo6Spkw6DnnGpOGcKlVgdpyJNEaUYzVXK76wnh1zS3PsSNTl94VzdmHV3ICNAJuM5QbNd4yU5lBQnsa3k+lRS3Rbr2VKp0z++HbzNrCHE0mVilhxhxtOlZ6NclsLiY6jV++fPnzNwZj+vrB9+Mfnv2/qyJLIT6NPrs0SUvo9tJ06f2lqZCrIY/hLbvjeZmDQLmyGe2f5y9+BMPlSuDBck1rIoqMyTJHzWOHCSwm43yQpFaXXyYoTzryuZ99saanBAO1kh9ZB2+4/Aitb8LF8neMbZ9XweVH02G3pmxtPwmM2COeKydzoFGQTcL718ezs4vja3Cvfvh2kqjYTFjBJ+oG9Q3H28k3GbOomDlwQ7Yt7ofH34eZxrQjVkXo6yFWeSGQYJM8h4V3V2/GMFOQs48eSmsxYybEiIYvufRPcrSZSuCW2wxsxo1bAL9F311NwWJe0Kv33Zg/fP/j4TPy5xuvvfj7YgSLbxcjt8sXzxYtY3aOsNB4UGgVoyHz975mQbIuaFvQFB9xDbWCSFYlyYXYjNw9KQNYswReRi8PA1MuDWmafCITYk8o4de0o7qG1Ffe69nsslaDrr5O7m1QeXuSQKPosO9/93l/T8vvGaQdatcFftZEvv/5p58a7P7uWR0rGdQ3FEoZ8nfTU2cZzKnXK7qULF/yValKI9YVli7R24fBnEnLY1PDEb02hmtEeO9g5Kri0Gy4u729HXMmmeONGcNX0nncCb17UIu0/XN8R2I8jrv50FLEW9RxxqSFS40papQxmiHD8qPmRWdU28wGB/QVVw+E1sBqyeuI3O1gH7jmZZwBtxArYw3ZpkELZeGWuolVRu7nu6s3hny/xm5cS3EOKwqtblyYEzMZoxiaIK8c4yaqZUKoW0wgZVxg0oS0zBI4WUMGhDZDDZdsfckEsNKqnFkeu/iWQi5vJaq0xjKZUAC2ZII4IJyjRxLvbBOcuejZo5Xjz1kq8LQj0D8MuIC6lTOkLi/56uEZi2MsLCbz6rtz2nUdK9g1YiAuqVinAcbvM0bxZzWBswjnFbxRkCgHSoq1WxyNbs/6UWlpS41QGtwTRJGW56SyuU9SuivQf9gVfioTHrtU9GsYj/dhg6/42ayy9C3HmzNxuaadeMM9ulWWbuIMk7Jl82YMvzJR0jRH/y0PD1/GpXD/ov8lePtXrBL/Pzy/8JTJhjSuBU4UGpDKDkje3cE7VmEMp1VeyA3c58MVpcvrLs5/O7vezfouXX2W5UEW6qXcj/l6AJyXuutoO+T+fn139WYXuA4h6n5yBQrn5ga7O7BFHIhX6wDQOZInDDIVxM9pQ1ZQMvf+oJse/dWwvvgP9ChftudPLs5n0/N3ZwPbZ9a2EdCYMy5NXWOo3d62t/VYxQ2wJPEB6k5AmKZuax7UmMgNoKRVTUaPDLMt6FnUAi8ehjAnx+cnZ296q1QzGlcVy86+gmVpyXSNK0n5ephVUKBnvJSW+524rdBYINPGrdDuxz4OqidrfRRjlWOtqJ2TOKPZNQc3FVBgMrxMk651LYWKP/5RKottqrFayVUF8cpiZZiTNr2pbpWmygMN2rKYp4gLuHEWzUxHgMrEyLI0X60q/F7s3lyNpre53FOax+4qpqpItBuKDzwdiMMfGu12bf5wUadP7jWzKQrven0/SyOV5em659065Ht7N+7iE55ygh0KUbt7sVVafFrOQ6MttewtQof8IBdf509f0ceflJqSwXVfmmb3doRpU/uy+MK2K9v55FIISLlkMqb97kCgqcClHEViRmAo12SmRv/R5gijrJIyo0Dtowy+WYpWWLMhDlRDbKYRDzbRzfT64uC7F89/hPo1IAezqUEkeIOCeBoXbF0wMY5V7iuPXFpcaVdzmCRcY2wnGo2d1BMd0ERm8mw/EZ7TVGcdaspAbFeL6oaM4S1fZeS7gElwUqF2tlCN42hA8I8Iv1z+tklAKR+x66IKD1Lt8Z4JcBWKBGOeM9HQB+ebnZ9u5jPlMuE3nAIXLl3ookrDZGIzM4ZXSld1tqr4tgHj+kuFYJsCSUeZIzCI8H56fQGk6a36klGuvMSNmmQqx4mLbZhOTKPIuVPkOLP5o+jyQ6eqtBOe2dbRTkXYcXBBTx/X0C6rPX3aHEsOnKlVxYvN0WXXwQ4/3z5x6x+APtLhbFMg8yGMRX1DMYytZt/xno/L/I8q4PGgVp/Ids5hTX0Qi+bxjht2Q/xQIWW4fBLAPYB7APf9g3srUPMQ8lYl7mhmoCSzwnlOT02vLtN+svuINABRAKIARAGIPgNEj3WDpIqJHDDtKUHvHZztPCdrM+cOy+ogkht3T07pBi4f/Wh4J3K4S35d3KhJfQl2XxJ81b5LSPG+qW9P7L5AOXKF+4Wfwl/GO1zsSWupu7uzDZltal/65mlzX6kSydWWuWnf99yzFPM6dxgWp/24L9e98476ECFmklBvibByJTPCJCbh+QvIlSSc2tO5ykOvl/Wv5e6pkHn/TLl/0/bBefM+oGyATxpbX3NurlRn7OZr3qcevEf9BXn4vtDWHfJ0S5926IZ7UzShx+Vj76cZ6nzgXpCtyC31V5Td4b0b8Rhnr18xA5hrJlc4kAc0D0I2ELKBkA08/WxgWa5RzzHhlogdtfYefe6mVu9cjN71h2LVJYUqqCOIe6IBjUPfR+ZtN5rm7G5e3ZwYui03+Dgga0DWgKxPH1lVXH18qxbQpf9VQcDyvL78myuJa9+ThlCUQmACSUkf3jui3j+jIaZ8DrOvZOAB2RalAj6/GnZk/QTJ1Bfe3Ls+Dau6Pjc669Rstgo6X3Rd8NX0P2enO+4KVoyYAT62vv2gm3fT81fT8+ns7HNfrQUdkdTbkxz23h7di6nJl1z3/WLIdS2sAy2VXfrDWyr9+0+4pfLDJxplCiUN3quTtrM8oYM2dNCGDtrQQRs6aEMHbeigDR20oYM2dNCGDtrQQRs6aEMHbeigDR20oYM2dNCGDtrQQRs6aEMHbeigDWfu4cw9nLmHDtrQQRsa1wK4B3AP4B46aAMQBSAKQBQ6aEMHbeigDR20oYM2dNCGDtrQQRs6aEMHbcgGQjYQOmhDB23ooA3IGpA1dNCGDtrQQRs6aEMH7VPsoD1R0qKs/hRtxIpC0D4gX/i7cQf/r60t3voGqaPo8uJ6Fvm/aRsdRZOb55P68vukilEOXJFyEo2is7sCY4vJtcu1T1SC0dGLw+ef/vY/AAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class PlanCreateRequest:
    """
    Creates a billing plan. In the JSON request body, include the plan details. A plan must include at least one regular payment definition and, optionally, a trial payment definition. Each payment definition specifies a billing period, which determines how often and for how long the customer is charged. A plan can specify a fixed or infinite number of payment cycles. A payment definition can optionally specify shipping fee and tax amounts. The default state of a new plan is `CREATED`. Before you can create an agreement from a plan, you must activate the plan by updating its `state` to `ACTIVE`.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/payments/billing-plans/?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, plan):
        self.body = plan
        return self
