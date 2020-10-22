## happy 1
* greet
  - utter_greet
  - utter_how_it_works_q
* affirm
  - utter_how_it_works
  - utter_how_u_win_q
* affirm
  - utter_who_wins
  - utter_would_you_like_to_continue
* affirm
  - user_info
  - form{"name":"user_info"}
  - form{"name":null}
  - utter_slots_values
  - utter_congrats_on_registering
  - utter_more_info
* affirm
  - utter_ask_payment_option  
  - utter_ask_for_postcode
* post_code  
  - utter_ask_buy_another
* affirm
  - utter_ask_if_share
* affirm
  - utter_ask_to_share_with_friends
* affirm
  - utter_thanks_for_using
  - utter_goodbye

## happy 2
* greet
  - utter_greet
  - utter_how_it_works_q
* affirm
  - utter_how_it_works
  - utter_how_u_win_q
* affirm
  - utter_who_wins
  - utter_would_you_like_to_continue
* affirm
  - user_info
  - form{"name":"user_info"}
  - form{"name":null}
  - utter_slots_values


## sad 1
* greet
  - utter_greet
  - utter_how_it_works_q
* affirm
  - utter_how_it_works
  - utter_how_u_win_q
* affirm
  - utter_who_wins
  - utter_would_you_like_to_continue
* affirm
  - user_info
  - form{"name":"user_info"}
  - form{"name":null}
  - utter_slots_values
  - utter_ask_payment_option
* out_of_scope
  - utter_wanna_continue
* deny
  - utter_goodbye



## sad 2
* greet
  - utter_greet
  - utter_how_it_works_q
* deny
  - utter_would_you_like_to_continue
* deny
  - utter_goodbye



## returns
* returns
 - utter_returns

## take to human
* talk_to_human
 - utter_talk_to_human_response

## bot check
* bot_challenge
 - utter_iamabot
