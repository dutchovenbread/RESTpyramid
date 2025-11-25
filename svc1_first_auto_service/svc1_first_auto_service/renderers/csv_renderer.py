from svc1_first_auto_service.data.car import Car

class CSVRendererFactory:
  def __call(self, info):
    return self._render
  
  def _render(self, value, system):

    request = system.get('request')
    request.response.content_type = 'text/csv'
    if not value:
      return ''
    
    if isinstance(value, dict):
      value = [value]

    if isinstance(value, Car):
      value = [value.to_dict()]

    if isinstance(value, list):
      for idx, item in enumerate(value):
        if isinstance(item, Car):
          value[idx] = item.to_dict()

    if not isinstance(value, list):
      raise ValueError("CSV renderer can only render dict or list of dicts.")
    
    first = value[0]
    headers = first.keys()

    response_rows = [','.join(headers)]
    for row in value:
      line_data = []
      for k in headers:
        line_data.append(row[k])
      line = ','.join(str(i) for i in line_data)
      response_rows.append(line)
    
    return '\n'.join(response_rows)

  def add_adapter(self, cls, method):
    self.adapters[cls] = method