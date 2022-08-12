import redis
import json

from conf import port_for_redis, host, decode_response


class Redis:
    def __init__(self, port, host, decode_response):
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=decode_response
        )

    def get_value(self, keys: list):
        for key in keys:
            check_value = self.redis_client.get(key)
            try:
                if check_value is not None:
                    print('redis')
                    return json.loads(check_value)
            except Exception as ex:
                print(ex, 'get_value')

    def add_key(self, key, value):
        try:
            print('add redis')
            self.redis_client.set(key, json.dumps(value), ex=360)
        except Exception as ex:
            print(ex, 'add_key')

    def delete_key(self, key):
        try:
            self.redis_client.delete(key)
        except Exception as ex:
            print(ex, 'delete_key')

    def add_message_to_list_redis(self, user_id, id_messages: list):
        try:
            for message in id_messages:
                self.redis_client.rpush(f'messages:{user_id}', message)
        except Exception as ex:
            print(ex, 'add_message_to_list_redis')

    def get_messages_from_list(self, user_id):
        try:
            return self.redis_client.lrange(f"messages:{user_id}", 0, 1000)
        except Exception as ex:
            # print(ex)
            print(ex, 'get_messages_from_list')


r = Redis(port=port_for_redis, host=host, decode_response=decode_response)
