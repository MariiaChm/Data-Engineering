# coding=utf-8
from __init__ import *


@app.route('/', methods=['POST'])
def handle_post_request() -> str:
    # get data from post request
    data: dict = request.json

    raw_dir: str = data.get('raw_dir')
    if not raw_dir:
        abort(400, 'raw_dir is not set')

    dt: str = data.get('date')
    if not dt:
        abort(400, 'date is not set')

    create_or_clear_directory(raw_dir)

    file_name_to_create = f"sales_{dt}.json"
    with open(os.path.join(raw_dir, file_name_to_create), "w") as file1:
        # reading all pages
        response_code, i = 0, 0
        while response_code != 404:
            i += 1
            response = requests.get(
                url=URL,
                params={'date': dt, 'page': i},
                headers={'Authorization': AUTH_TOKEN},
            )
            print("Response status code:", response.status_code)

            response_code = response.status_code

            if response.status_code == 200:
                for ln in response.json():
                    file1.write(json.dumps(ln) + '\n')

    return 'data extracted'


if __name__ == '__main__':
    app.run(port=8081)
