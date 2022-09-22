from rest_framework.authentication import TokenAuthentication


class CustomAuthentication(TokenAuthentication):
    keyword = "Bearer"
