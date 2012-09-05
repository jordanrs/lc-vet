$(function () {
	var Event = Backbone.Model.extend()
	
	var Events = Backbone.Collection.extend({
		model: Event,
		url: '/api/v1/events/'
	});
	
	var EventsView = Backbone.View.extend({
		initialize: function(){
			_.bindAll(this);
			this.collection.bind('reset', this.addAll);
			this.collection.bind('add', this.addOne);
			this.collection.bind('change', this.change);
		},
		render: function(){
			$(this.el).fullCalendar({
				header: {
					left: 'prev,next today',
					center:'title',
					right: 'month,basicWeek,basicDay',
					ignoreTimezone: false
				},
				selectable: true,
				selectHelper: true,
				editable: true,
				select: this.select,
				eventClick: this.eventClick
			});
			console.log(this.collection)
			return this;
		},
		addAll: function(){
			$(this.el).fullCalendar('addEventSource', this.collection.toJSON());
		},
		select: function(startDate, endDate){
			var eventView = new EventView();
			eventView.collection = this.collection;
			eventView.model = new Event({start: startDate, end: endDate});
			eventView.render();
		},
		eventClick: function(fcEvent) {
			console.log(this, fcEvent, this.collection.get(fcEvent.resource_uri), this.collection )
			var eventView = new EventView();
			eventView.model = this.collection.get(fcEvent.resource_uri)
			eventView.render();
		},
		addOne: function(event) {
			$(this.el).fullCalendar('renderEvent', event.toJSON())
		},
		change: function(event) {
			console.log(event, $(this.el).fullCalendar('clientEvents'))
			// need to get the id out of the resource uri string
			// need to manipulate the string needs last index of / and second last and then split what is inbetween 
			// and pass this to the client events ID
			var fcEvent = $(this.el).fullCalendar('clientEvents', event.get('id'))[0];
			fcEvent.title = event.get('title');
			fcEvent.color = event.get('color');
			fcEvent.description = event.get('description');
			$(this.el).fullCalendar('updateEvent', fcEvent) 
		}
		
	});
	
	var EventView = Backbone.View.extend({
		el: $('#eventDialog'),
		initialize: function(){
			_.bindAll(this);
		},
		render: function() {
			$(this.el).dialog({
				modal: true,
				title: (this.model.isNew() ? 'New' : 'Edit') + 'Event',
				buttons: {'OK':this.save, 'Cancel': this.close},
				open: this.open
			})
			
			return this;
		},
		open: function(){
			this.$('#title').val(this.model.get('title'));
			this.$('#color').val(this.model.get('color'));
			this.$('#description').val(this.model.get('description'));
		},
		close: function(){
			$(this.el).dialog("close");
		},
		save: function(){
			this.model.set({'title': this.$('#title').val(), 'color': this.$('#color').val(), 'description': this.$('#description').val()})
			if(this.model.isNew()){
				this.collection.create(this.model, {success: this.close})
			} else {
				this.model.save({}, {success: this.close})
			}
		}
	});
	
	var events = new Events();
	new EventsView({el: $("#calendar"), collection: events}).render();
	events.fetch();
	
})
