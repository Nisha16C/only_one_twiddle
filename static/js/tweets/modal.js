const tweetBtn = document.getElementById('create-tweet');
const submitTweetBtn = document.getElementById('tweet-submit');
const tweetForm = document.getElementById('tweet-form');

const csrf_token = document.getElementsByName('csrfmiddlewaretoken');
// const body = document.getElementById('id_body');
// const photo = document.getElementById('tweet_photo');
// ----------------------------------------------------------------
const mentionBtn = document.getElementById('mention-button');
const mention = document.getElementById('id_mention');
const mentionForm = document.getElementById('mention-form');
const submitMentionBtn = document.getElementById('mention-submit');
// -----------------------------------------------------------------
const retweetBtn = document.getElementById('retweet-button');
const retweet = document.getElementById('id_retweet');
const retweetForm = document.getElementById('retweet-form');
const submitretweetBtn = document.getElementById('retweet-submit');
//-------------------------------------------------------------------
const deleteBtn = document.getElementById('delete-button');
const chatDeleteBtn = document.getElementById('delete-chat');

if (mentionForm !== null) {
    const tweetURL = mentionForm.getAttribute('data-tweet');
    // For mention
    mentionBtn.addEventListener('click', function (e) {
        e.preventDefault();
        toggleModal('mention-modal');
    })

    submitMentionBtn.addEventListener('click', function (e) {
        e.preventDefault;

        $.ajax({
            type: 'POST',
            url: `/compose/${tweetURL}/mention/`,
            data: {
                'csrfmiddlewaretoken': csrf_token[0].value,
                'mention': mention.value,
            },
            success: function (response) {
                toggleModal('mention-modal');
                window.location.reload();
                tweetForm.reset();
            },
            error: function (error) {
                alert("Oops something went wrong!");
            }
        })
    })
}
// ----------------------------------------------------------------
if (retweetForm !== null) {
    const tweetURL = retweetForm.getAttribute('data-tweet');
    // For retweet
    retweetBtn.addEventListener('click', function (e) {
        e.preventDefault();
        toggleModal('retweet-modal');
    })

    submitretweetBtn.addEventListener('click', function (e) {
        e.preventDefault;

        $.ajax({
            type: 'POST',
            url: `/compose/${tweetURL}/retweet/`,
            data: {
                'csrfmiddlewaretoken': csrf_token[0].value,
                'retweet': retweet.value,
            },
            success: function (response) {
                toggleModal('retweet-modal');
                window.location.reload();
                tweetForm.reset();
            },
            error: function (error) {
                alert("Oops something went wrong!");
            }
        })
    })
}
//-----------------------------------------------------------------
let likeUnlikeForms = document.getElementsByClassName('like-unlike');
likeUnlikeForms = Array.from(likeUnlikeForms);

const getCookieModal = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookieModal('csrftoken');

// For tweet
tweetBtn.addEventListener('click', function (e) {
    e.preventDefault();
    toggleModal('modal-id');
})




submitTweetBtn.addEventListener('click', function (e) {
    e.preventDefault();
    const formdata = new FormData(tweetForm);
    $.ajax({
        type: 'POST',
        url: '/compose/tweet/',
    
        data: formdata,
        processData: false,
        contentType: false,
        success: function (response) {
            if (response.status === 'ok') {
                toggleModal('modal-id');
                window.location.reload();
                tweetForm.reset();
            } else if (response.status === 'profanity') {
                alert("Your tweet contains profanity. Please use appropriate language.");
            }
        },
        error: function (error) {
            alert("Oops something went wrong!");
        }
    });
});



function toggleModal(modalID) {
    document.getElementById(modalID).classList.toggle("hidden");
    document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
    document.getElementById(modalID).classList.toggle("flex");
    document.getElementById(modalID + "-backdrop").classList.toggle("flex");
}


// For like button
likeUnlikeForms.forEach(form => form.addEventListener('submit', function (e) {
    e.preventDefault();
    const clickedId = e.target.getAttribute('data-like-id');
    const clickedBtn = document.getElementById(`like-unlike-${clickedId}`);
    const clickedType = e.target.getAttribute('data-type');
    

    $.ajax({
        type: 'POST',
        url: "/compose/like-unlike/",
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'pk': clickedId,
            'type': clickedType,
        },
        success: function (response) {
            clickedBtn.classList.toggle('text-red-800');
            clickedBtn.nextElementSibling.innerHTML = response.like_count;
        },
        error: function (error) {
            alert('Oops! something went wrong!');
        },

    })
}))


deleteBtn.addEventListener('click', function (e) {
    const tweetId = deleteBtn.getAttribute('data-id');

    $.ajax({
        type: 'POST',
        url: "/compose/delete/",
        data: {
            'csrfmiddlewaretoken': csrf_token[0].value,
            'pk': tweetId,
        },
        success: function (response) {
            origin = window.location.origin
            window.location.href = `${origin}/my/${response.url}/`;
        },
        error: function (error) {
            alert('Oops! something went wrong!');
        }
    })
})


