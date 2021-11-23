import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:semear/components/bootom_menu.dart';
import 'package:semear/components/oficina_item.dart';
import 'package:semear/pages/home/home.service.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<dynamic> oficinas = [];

  void getOficinasOnState() async {
    oficinas = await getOficinas();
    setState(() {});
  }

  @override
  void initState() {
    super.initState();
    getOficinasOnState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.all(30),
          child: Column(
            children: [
              Container(
                width: MediaQuery.of(context).size.width,
                margin: EdgeInsets.only(bottom: 40),
                child: Text(
                  "Suas oficinas",
                  style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
                ),
              ),
              Expanded(
                child: ListView.builder(
                  itemCount: oficinas.length,
                  itemBuilder: (BuildContext ctx, int i) {
                    return OficinaItemComponent(oficina: oficinas[i]);
                  },
                ),
              ),
            ],
          ),
        ),
      ),
      bottomNavigationBar: BottomMenuComponent(),
    );
  }
}
