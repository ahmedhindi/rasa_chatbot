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
  - utter_ask_payment_option
* goodbye
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
  - utter_ask_payment_option  
* out_of_scope
  - utter_wanna_continue
* affirm
  - user_info
  - form{"name":null}
  - utter_slots_values
  - utter_ask_payment_option
* goodbye
  - utter_goodbye




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
 - utter_iamabot -->
