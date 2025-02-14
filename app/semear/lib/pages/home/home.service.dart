import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';
import 'package:shared_preferences/shared_preferences.dart';

Future<List<dynamic>> getOficinas() async {
  SharedPreferences prefs = await SharedPreferences.getInstance();

  http.Response request = await http.post(
    Uri.parse(url_semear + '/api/oficinasaluno/getalunooficinas/'),
    body: jsonEncode({'id': prefs.getInt('id_aluno') ?? 0}),
    headers: {
      'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
      'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
    },
  );

  Map<String, dynamic> dataJson = jsonDecode(request.body);

  return dataJson['oficinas'] as List<dynamic>;
}
