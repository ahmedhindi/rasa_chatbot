## survay happy path
* greet
  - utter_greet
* how_it_works
  - utter_how_it_works
* who_wins
  - utter_who_wins


## path one
* greet
  - utter_greet
* how_it_works
  - utter_how_it_works
* returns
  - utter_returns
* goodbye
  - utter_goodbye


## path one
* greet
  - utter_greet
* who_wins
  - utter_who_wins
* returns
  - utter_returns
* goodbye
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot




## happy path1
* greet
  - utter_greet
  - q_how_it_works
* affirm
  - utter_how_it_works
  - utter_who_wins
  - utter_would_you_like_to_continue
* affirm
  - user_info
  - form{"name":"user_info"}
  - form{"name":null}
* goodbye
  - utter_goodbye



## happy path1 (with out_of_scope)
* greet
  - utter_greet
  - q_how_it_works
* affirm
  - utter_how_it_works
  - utter_who_wins
  - utter_would_you_like_to_continue
* affirm
  - user_info
  - form{"name":"user_info"}
  - form{"name":null}
* out_of_scope
  - utter_wanna_continue
* affirm
  - user_info
  - form{"name":null}
* goodbye
  - utter_goodbye

## sad path1
* greet
  - utter_greet
  - q_how_it_works
* deny
  - utter_goodbye

## sad path2
* greet
  - utter_greet
  - q_how_it_works
* affirm
  - utter_how_it_works
  - utter_who_wins
  - utter_would_you_like_to_continue
* deny
  - utter_goodbye