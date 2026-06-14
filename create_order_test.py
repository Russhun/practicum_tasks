import sender_stand_request as ssr

def positive_assert_200(resp):
    assert resp.status_code == 200

def test_get_order_by_track_success_response():
    resp = ssr.post_new_order()
    track_num = resp.json()["track"]
    resp = ssr.get_order_by_track(track_num)
    positive_assert_200(resp)