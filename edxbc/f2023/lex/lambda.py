from datetime               import datetime
from dateutil.relativedelta import relativedelta

def parse_int (n):
	"""Convert a non integer value to an integer value securely."""
	try:
		return int(n)
	except ValueError:
		return float('nan')

def build_validation_result (is_valid,
                             violated_slot,
														 message_content) -> dict:
	"""Define a result message structured as Lex response."""
	if message_content is None:
		return {
			'isValid'      : is_valid,
			'violatedSlot' : violated_slot,
		}
	return {
		'isValid'      : is_valid,
		'violatedSlot' : violated_slot,
		'message'      : {
			'contentType' : 'PlainText',
			'content'     : message_content,
		},
	}

def get_slots (intent_request : dict):
	"""Fetch slots and their values from the current intent."""
	return intent_request['currentIntent']['slots']

def elicit_slot (session_attributes,
                 intent_name,
								 slots,
								 slot_to_elicit,
								 message) -> dict:
	"""Defines an elicit slot type response."""
	return {
    'sessionAttributes' : session_attributes,
		'dialogAction'      : {
			'type'         : 'ElicitSlot',
			'intentName'   : intent_name,
			'slots'        : slots,
			'slotToElicit' : slot_to_elicit,
			'message'      : message,
		},
	}

def delegate (session_attributes,
              slots) -> dict:
	"""Defines a delegate slot type response."""
	return {
		'sessionAttributes' : session_attributes,
		'dialogAction'      : {
      'type'  : 'Delegate',
			'slots' : slots
		},
	}

def close (session_attributes,
           fulfillment_state,
					 message) -> dict:
	"""Defines a close slot type response."""
	return {
		'sessionAttributes' : session_attributes,
		'dialogAction'      : {
			'type'             : 'Close',
			'fulfillmentState' : fulfillment_state,
			'message'          : message,
		},
	}

def validate_data (age,
                   investment_amount,
									 intent_request):
	"""Validate user input data."""
	if age is not None:
		age = parse_int(age)
		if   age < 0:
			return build_validation_result(False, 'age', 'Your age is invalid. Provide an age greater than zero.')
		elif age >= 65:
			return build_validation_result(False, 'age', 'The maximum age to contract this service is 64.')
	if investment_amount is not None:
		investment_amount = parse_int(investment_amount)
		if investment_amount < 5_000:
			return build_validation_result(False, 'investmentAmount', 'The minimum investment amount is $5,000. Provide an amount that meets this requirement.')
	return build_validation_result(True, None, None)

def get_investment_recommendation (risk_level : str) -> str:
	"""Return an initial investment recommendation based on the risk profile."""
	risk_levels = {
		'none'   : "100% bonds (AGG), 0% equities (SPY)",
		'low'    :  "60% bonds (AGG), 40% equities (SPY)",
    'medium' :  "40% bonds (AGG), 60% equities (SPY)",
		'high'   :  "20% bonds (AGG), 80% equities (SPY)",
	}
	return risk_levels[risk_level.lower()]

def recommend_portfolio (intent_request : dict) -> dict:
	"""Performs dialog management and fulfillment for recommending a portfolio."""
	first_name        = get_slots(intent_request)['firstName']
	age               = get_slots(intent_request)['age']
	investment_amount = get_slots(intent_request)['investmentAmount']
	risk_level        = get_slots(intent_request)['riskLevel']
	source            = get_slots(intent_request)['invocationSource']

	if source == 'DialogCodeHook':
		slots             = get_slots(intent_request)
		validation_result = validate_data(age, investment_amount, intent_request)
		if not validation_result['isValid']:
			slots[validation_result['violatedSlot']] = None # clean invalid slot
			return elicit_slot(
        intent_request['sessionAttributes'],
        intent_request['currentIntent']['name'],
				slots,
				validation_result['violatedSlot'],
				validation_result['message'],
			)
		output_session_attributes = intent_request['sessionAttributes'] # fetch the current session attributes
		return delegate(output_session_attributes, get_slots(intent_request))
	
	initial_recommendation = get_investment_recommendation(risk_level)
	return close(
		intent_request['sessionAttributes'],
		'Fulfilled',
		{
			'contentType' : 'PlainText',
			'content'     : f'Thank you for your information {first_name}. Based on your risk tolerance, my recommendation is to choose an investment portfolio with {initial_recommendation}.'
		}
	)

def dispatch (intent_request : dict):
	"""Called when the user specifies an intent for this bot."""
	intent_name = intent_request['currentIntent']['name']
	if intent_name == 'recommendPortfolio':
		return recommend_portfolio(intent_request)
	raise Exception(f'Intent with name {intent_name} not supported.')

def lambda_handler (event : dict,
                    context):
	"""Route the incoming request based on intent. The JSON body of the request is provided in the event slot."""
	return dispatch(event)