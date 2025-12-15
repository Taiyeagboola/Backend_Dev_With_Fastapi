def test_vote_on_post(authorized_client, test_posts, test_user):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})

    assert res.status_code == 201

def test_vote_on_post_twice(authorized_client, test_posts, test_user):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})

    assert res.status_code == 409